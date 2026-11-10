from typing import List
from models.programa_model import ProgramaModel
from models.entities.programa_estudio import ProgramaEstudio
from exceptions.biblioteca_exceptions import BibliotecaException

class ProgramaController:
    """Controlador que orquesta la lógica de negocio para Programas de Estudio."""

    def __init__(self):
        self._modelo_programa = ProgramaModel()

    def obtener_todos(self) -> List[ProgramaEstudio]:
        """Solicita al DAO la lista íntegra de programas registrados."""
        try:
            return self._modelo_programa.listar_todos()
        except BibliotecaException as error:
            raise error
        except Exception as error_inesperado:
            raise BibliotecaException(f"Falla inesperada al listar programas: {error_inesperado}")

    def buscar_programas(self, criterio_ingresado: str) -> List[ProgramaEstudio]:
        """Sanitiza el criterio de búsqueda y consulta al DAO."""
        try:
            criterio_limpio = criterio_ingresado.strip() if criterio_ingresado else ""
            return self._modelo_programa.buscar_por_criterio(criterio_limpio)
        except BibliotecaException as error:
            raise error
        except Exception as error_inesperado:
            raise BibliotecaException(f"Falla inesperada al buscar programas: {error_inesperado}")