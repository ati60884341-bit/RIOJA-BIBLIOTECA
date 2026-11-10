from typing import List
from database.conexion_bd import ConexionBD
from models.entities.rol import Rol
from exceptions.biblioteca_exceptions import BibliotecaException

class RolModel:
    """Capa DAO: Responsable exclusivo de la persistencia para el catálogo de Roles."""

    @staticmethod
    def listar() -> List[Rol]:
        """Ejecuta 'sp_roles_listar' y retorna la colección completa de roles."""
        conexion = None
        cursor = None
        lista_roles: List[Rol] = []

        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)

            cursor.callproc('sp_roles_listar')

            for resultado in cursor.stored_results():
                filas = resultado.fetchall()
                for fila in filas:
                    rol = Rol(
                        id_rol=fila['id_rol'],
                        nombre_rol=fila['nombre_rol']
                    )
                    lista_roles.append(rol)

            return lista_roles

        except Exception as error_persistencia:
            raise BibliotecaException(f"Error en la capa DAO al listar roles: {error_persistencia}")

        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()
