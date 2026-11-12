from typing import List, Dict, Any, Optional
from database.conexion_bd import ConexionBD
from models.entities.empleado import Empleado
from exceptions.biblioteca_exceptions import BibliotecaException

class EmpleadoModel:
    """Capa DAO: Responsable exclusivo del acceso a datos para la entidad Empleado."""

    @staticmethod
    def registrar(empleado: Empleado) -> int:
        """Invoca sp_empleado_registrar dentro de una transacción atómica."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            parametros = (
                empleado.numero_documento,
                empleado.nombres,
                empleado.apellidos,
                empleado.nombre_usuario,
                empleado.clave_hash,
                empleado.rol_id,
                empleado.codigo_empleado,
                empleado.cargo,
                empleado.turno,
                0  # Receptor del parámetro de salida p_id_generado
            )
            resultado = cursor.callproc('sp_empleado_registrar', parametros)
            return resultado[9]
        except Exception as error:
            raise BibliotecaException(f"Error transaccional al registrar empleado: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(id_usuario: int) -> Optional[Dict[str, Any]]:
        """Ejecuta sp_empleado_obtener_por_id y retorna un diccionario con los datos."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_empleado_obtener_por_id', (id_usuario,))
            for resultado in cursor.stored_results():
                return resultado.fetchone()
            return None
        except Exception as error:
            raise BibliotecaException(f"Error al consultar colaborador por ID: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(empleado: Empleado) -> bool:
        """Ejecuta sp_empleado_actualizar bajo control transaccional ACID."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            parametros = (
                empleado.id_usuario,
                empleado.numero_documento,
                empleado.nombres,
                empleado.apellidos,
                empleado.nombre_usuario,
                empleado.clave_hash,  # Cadena vacía si no se modificó
                empleado.rol_id,
                empleado.codigo_empleado,
                empleado.cargo,
                empleado.turno
            )
            cursor.callproc('sp_empleado_actualizar', parametros)
            return True
        except Exception as error:
            raise BibliotecaException(f"Falla transaccional al actualizar: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def listar(criterio: str = "") -> List[Dict[str, Any]]:
        """Consulta el catálogo filtrado con límite de seguridad (Top 20)."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_empleados_listar', (criterio,))
            for resultado in cursor.stored_results():
                return resultado.fetchall()
            return []
        except Exception as error:
            raise BibliotecaException(f"Error al listar empleados: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    # S23 - Paso 5.2: Eliminación lógica / física con control de integridad (1451)
    @staticmethod
    def eliminar(id_usuario: int, logico: bool = True) -> bool:
        """Ejecuta borrado lógico (es_activo=0) o físico controlando restricciones FK."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            if logico:
                cursor.callproc('sp_empleado_eliminar_logico', (id_usuario,))
            else:
                cursor.callproc('sp_empleado_eliminar_fisico', (id_usuario,))
            # El SP lógico no abre transacción propia: confirmamos el UPDATE
            # (mysql-connector trabaja con autocommit desactivado).
            conexion.commit()
            return True
        except Exception as error:
            if "1451" in str(error) or "foreign key" in str(error).lower():
                raise BibliotecaException(
                    "Integridad Referencial: No se puede eliminar físicamente porque el empleado "
                    "tiene operaciones históricas vinculadas. Utilice la baja lógica."
                )
            raise BibliotecaException(f"Error al eliminar colaborador: {error}")
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()
