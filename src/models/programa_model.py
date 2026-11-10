from typing import List
from database.conexion_bd import ConexionBD
from models.entities.programa_estudio import ProgramaEstudio
from exceptions.biblioteca_exceptions import BibliotecaException

class ProgramaModel:
    """Capa DAO: Responsable exclusivo de la persistencia para Programas de Estudio."""

    @staticmethod
    def listar_todos() -> List[ProgramaEstudio]:
        """Ejecuta 'sp_programas_listar' y retorna la colección completa de programas."""
        conexion = None
        cursor = None
        lista_programas: List[ProgramaEstudio] = []

        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)

            cursor.callproc('sp_programas_listar')

            for resultado in cursor.stored_results():
                filas = resultado.fetchall()
                for fila in filas:
                    programa = ProgramaEstudio(
                        id_programa=fila['id_programa'],
                        codigo_programa=fila['codigo_programa'],
                        nombre_programa=fila['nombre_programa'],
                        estado=fila['estado'],
                        creado_en=fila['creado_en']
                    )
                    lista_programas.append(programa)

            return lista_programas

        except Exception as error_persistencia:
            raise BibliotecaException(f"Error en la capa DAO al listar programas: {error_persistencia}")

        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def buscar_por_criterio(criterio: str) -> List[ProgramaEstudio]:
        """Ejecuta 'sp_programas_buscar' con parámetro defensivo para evitar inyección SQL."""
        conexion = None
        cursor = None
        lista_resultados: List[ProgramaEstudio] = []

        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)

            # Paso de parámetro en tupla estricta (criterio,)
            criterio_sanitizado = criterio.strip() if criterio else ""
            cursor.callproc('sp_programas_buscar', (criterio_sanitizado,))

            for resultado in cursor.stored_results():
                filas = resultado.fetchall()
                for fila in filas:
                    programa = ProgramaEstudio(
                        id_programa=fila['id_programa'],
                        codigo_programa=fila['codigo_programa'],
                        nombre_programa=fila['nombre_programa'],
                        estado=fila['estado'],
                        creado_en=fila['creado_en']
                    )
                    lista_resultados.append(programa)

            return lista_resultados

        except Exception as error_persistencia:
            raise BibliotecaException(f"Error en la capa DAO al buscar programas: {error_persistencia}")

        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None and conexion.is_connected():
                conexion.close()