from typing import Optional
from src.database.conexion_bd import ConexionBD
from src.models.entities.usuario import Usuario
from src.exceptions.biblioteca_exceptions import BibliotecaException

class UsuarioModel:
    """Capa DAO: Responsable exclusivo del acceso a datos para la entidad Usuario."""

    @staticmethod
    def buscar_por_nombre_usuario(nombre_usuario: str) -> Optional[Usuario]:
        """Consulta 'sp_obtener_usuario_por_username' y mapea el resultado a la entidad Usuario."""
        conexion = None
        cursor = None
        usuario_encontrado: Optional[Usuario] = None

        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)

            # Invocación paramétrica protegida contra SQL Injection[cite: 2]
            cursor.callproc('sp_obtener_usuario_por_username', (nombre_usuario,))

            for resultado in cursor.stored_results():
                fila = resultado.fetchone()
                if fila:
                    usuario_encontrado = Usuario(
                        id_usuario=fila['id_usuario'],
                        nombre_usuario=fila['username'],
                        nombre_completo=fila['nombre_completo'],
                        rol=fila['rol'],
                        estado='Activo' if fila['es_activo'] == 1 else 'Inactivo',
                        clave_hash=fila['password_hash']
                    )

            return usuario_encontrado

        except Exception as error_persistencia:
            raise BibliotecaException(f"Error en la capa de datos de autenticación: {error_persistencia}")

        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()