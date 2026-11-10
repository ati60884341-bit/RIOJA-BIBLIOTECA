from typing import List
from models.rol_model import RolModel
from models.entities.rol import Rol
from exceptions.biblioteca_exceptions import BibliotecaException

class RolController:
    """Controlador que orquesta la lógica de negocio para el catálogo de Roles."""

    def __init__(self):
        self._modelo_rol = RolModel()

    def obtener_roles(self) -> List[Rol]:
        """Solicita al DAO la lista íntegra de roles institucionales registrados."""
        try:
            return self._modelo_rol.listar()
        except BibliotecaException as error:
            raise error
        except Exception as error_inesperado:
            raise BibliotecaException(f"Falla inesperada al listar roles: {error_inesperado}")
