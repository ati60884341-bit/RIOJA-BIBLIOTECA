from typing import List, Optional
from models.programa_model import ProgramaModel
from models.entities.programa_estudio import ProgramaEstudio
from exceptions.biblioteca_exceptions import BibliotecaException, ValidacionDatosError

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

    def obtener_programa_por_id(self, id_programa: int) -> Optional[ProgramaEstudio]:
        """Valida el identificador y recupera un programa concreto."""
        if id_programa is None or id_programa <= 0:
            raise ValidacionDatosError("Identificador de programa no válido.")
        return self._modelo_programa.obtener_por_id(id_programa)

    def registrar_programa(self, codigo: str, nombre: str) -> bool:
        """Valida los datos del formulario y registra un nuevo programa."""
        cod = codigo.strip().upper() if codigo else ""
        nom = nombre.strip().upper() if nombre else ""

        if not cod or not nom:
            raise ValidacionDatosError("El código y el nombre del programa son obligatorios.")
        if len(cod) > 10:
            raise ValidacionDatosError("El código no debe exceder 10 caracteres.")
        if len(nom) > 120:
            raise ValidacionDatosError("El nombre no debe exceder 120 caracteres.")

        nuevo = ProgramaEstudio(codigo_programa=cod, nombre_programa=nom)
        return self._modelo_programa.registrar(nuevo)

    def actualizar_programa(self, id_programa: int, codigo: str, nombre: str, estado: str) -> bool:
        """Valida los datos del formulario y actualiza un programa existente."""
        if id_programa is None or id_programa <= 0:
            raise ValidacionDatosError("Identificador de programa no válido.")

        cod = codigo.strip().upper() if codigo else ""
        nom = nombre.strip().upper() if nombre else ""

        if not cod or not nom:
            raise ValidacionDatosError("El código y el nombre del programa son obligatorios.")
        if len(cod) > 10:
            raise ValidacionDatosError("El código no debe exceder 10 caracteres.")
        if len(nom) > 120:
            raise ValidacionDatosError("El nombre no debe exceder 120 caracteres.")
        if estado not in ("Activo", "Inactivo"):
            raise ValidacionDatosError("El estado debe ser 'Activo' o 'Inactivo'.")

        modificado = ProgramaEstudio(
            id_programa=id_programa,
            codigo_programa=cod,
            nombre_programa=nom,
            estado=estado
        )
        return self._modelo_programa.actualizar(modificado)

    def eliminar_programa(self, id_programa: int, logico: bool = True) -> bool:
        """Valida el identificador y solicita la baja del programa al DAO."""
        if id_programa is None or id_programa <= 0:
            raise ValidacionDatosError("Identificador de programa no válido.")
        return self._modelo_programa.eliminar(id_programa, logico)
