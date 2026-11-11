from typing import List, Optional
from database.conexion_bd import ConexionBD
from models.entities.rol import Rol
from exceptions.biblioteca_exceptions import BibliotecaException


class RolModel:
    """Capa DAO: Responsable exclusivo de la persistencia para el catálogo de Roles."""

    @staticmethod
    def _mapear(fila) -> Rol:
        return Rol(
            id_rol=fila['id_rol'],
            nombre_rol=fila['nombre_rol'],
            descripcion=fila.get('descripcion'),
            total_usuarios=fila.get('total_usuarios', 0)
        )

    @staticmethod
    def listar() -> List[Rol]:
        """Ejecuta 'sp_roles_listar' (usado por el combo del formulario de empleados)."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_roles_listar')
            lista_roles: List[Rol] = []
            for resultado in cursor.stored_results():
                lista_roles.extend(RolModel._mapear(f) for f in resultado.fetchall())
            return lista_roles
        except Exception as error_persistencia:
            raise BibliotecaException(f"Error en la capa DAO al listar roles: {error_persistencia}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def buscar(criterio: str = "") -> List[Rol]:
        """Ejecuta 'sp_roles_buscar' e incluye el conteo de usuarios por rol."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_roles_buscar', (criterio,))
            lista_roles: List[Rol] = []
            for resultado in cursor.stored_results():
                lista_roles.extend(RolModel._mapear(f) for f in resultado.fetchall())
            return lista_roles
        except Exception as error:
            raise BibliotecaException(f"Error al buscar roles: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def obtener_por_id(id_rol: int) -> Optional[Rol]:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_rol_obtener_por_id', (id_rol,))
            for resultado in cursor.stored_results():
                fila = resultado.fetchone()
                if fila:
                    return RolModel._mapear(fila)
            return None
        except Exception as error:
            raise BibliotecaException(f"Error al consultar el rol: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def registrar(rol: Rol) -> int:
        """Ejecuta 'sp_rol_registrar' y devuelve el id generado (parámetro OUT)."""
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            resultado = cursor.callproc('sp_rol_registrar', (rol.nombre_rol, rol.descripcion, 0))
            conexion.commit()  # mysql-connector no confirma cambios automáticamente
            return resultado[2]
        except Exception as error:
            raise BibliotecaException(f"Error al registrar el rol: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def actualizar(rol: Rol) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            cursor.callproc('sp_rol_actualizar', (rol.id_rol, rol.nombre_rol, rol.descripcion))
            conexion.commit()  # mysql-connector no confirma cambios automáticamente
            return True
        except Exception as error:
            raise BibliotecaException(f"Error al actualizar el rol: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar(id_rol: int) -> bool:
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            cursor.callproc('sp_rol_eliminar', (id_rol,))
            conexion.commit()  # mysql-connector no confirma cambios automáticamente
            return True
        except Exception as error:
            raise BibliotecaException(f"Error al eliminar el rol: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()
