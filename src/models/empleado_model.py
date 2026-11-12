from database.conexion_bd import ConexionBD
from models.entities.empleado import Empleado
from exceptions.biblioteca_exceptions import BibliotecaException


class EmpleadoModel:
    """Capa DAO: Responsable exclusivo del acceso a datos para la entidad Empleado."""

    # ---------------------------------------------------------------
    # Paso 1.1: Listar / Buscar
    # ---------------------------------------------------------------
    @staticmethod
    def listar(criterio: str = "") -> list:
        """Consulta el catálogo de empleados ejecutando el SP de búsqueda."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            # Pasamos el criterio como tupla defensiva contra Inyección SQL
            cursor.callproc('sp_empleados_listar', (criterio,))
            for resultado in cursor.stored_results():
                return resultado.fetchall()
            return []
        except Exception as error:
            raise BibliotecaException(f"Error al listar empleados: {error}")
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    # ---------------------------------------------------------------
    # Paso 3.1: Registrar
    # ---------------------------------------------------------------
    @staticmethod
    def registrar(empleado: Empleado) -> int:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            parametros = (
                empleado.numero_documento, empleado.nombres, empleado.apellidos,
                empleado.nombre_usuario, empleado.clave_hash, empleado.rol_id,
                empleado.codigo_empleado, empleado.cargo, empleado.turno, 0
            )
            resultado = cursor.callproc('sp_empleado_registrar', parametros)
            return resultado[9] # Retorna el ID autogenerado
        except Exception as error:
            raise BibliotecaException(str(error))
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    # ---------------------------------------------------------------
    # Paso 4.1: Obtener por ID y Actualizar
    # ---------------------------------------------------------------
    @staticmethod
    def obtener_por_id(id_usuario: int) -> dict:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_empleado_obtener_por_id', (id_usuario,))
            for r in cursor.stored_results():
                return r.fetchone()
        except Exception as e:
            raise BibliotecaException(str(e))
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    @staticmethod
    def actualizar(empleado: Empleado) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            parametros = (
                empleado.id_usuario, empleado.numero_documento, empleado.nombres,
                empleado.apellidos, empleado.nombre_usuario, empleado.clave_hash,
                empleado.rol_id, empleado.codigo_empleado, empleado.cargo, empleado.turno
            )
            cursor.callproc('sp_empleado_actualizar', parametros)
            return True
        except Exception as e:
            raise BibliotecaException(str(e))
        finally:
            if cursor: cursor.close()
            if conexion and conexion.is_connected(): conexion.close()

    # ---------------------------------------------------------------
    # Paso 5.2: Eliminar (lógico / físico) con control de FK (1451)
    # ---------------------------------------------------------------
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
