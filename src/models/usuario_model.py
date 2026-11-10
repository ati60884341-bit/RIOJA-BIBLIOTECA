from typing import Optional
from database.conexion_bd import ConexionBD
from models.entities.usuario import Usuario
from exceptions.biblioteca_exceptions import BibliotecaException

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

            # Invocación paramétrica protegida contra SQL Injection
            cursor.callproc('sp_obtener_usuario_por_username', (nombre_usuario,))