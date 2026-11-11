from typing import List
from models.rol_model import RolModel
from models.entities.rol import Rol
from exceptions.biblioteca_exceptions import BibliotecaException, ValidacionDatosError


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

    def buscar_roles(self, criterio: str = "") -> List[Rol]:
        return self._modelo_rol.buscar((criterio or "").strip())

    def obtener_rol_por_id(self, id_rol: int) -> Rol:
        if id_rol is None or id_rol <= 0:
            raise ValidacionDatosError("Identificador de rol no válido.")
        rol = self._modelo_rol.obtener_por_id(id_rol)
        if rol is None:
            raise ValidacionDatosError("El rol seleccionado ya no existe.")
        return rol

    def registrar_rol(self, nombre: str, descripcion: str) -> int:
        nombre, descripcion = self._validar(nombre, descripcion)
        return self._modelo_rol.registrar(Rol(nombre_rol=nombre, descripcion=descripcion))

    def actualizar_rol(self, id_rol: int, nombre: str, descripcion: str) -> bool:
        if id_rol is None or id_rol <= 0:
            raise ValidacionDatosError("Identificador de rol no válido.")
        nombre, descripcion = self._validar(nombre, descripcion)
        return self._modelo_rol.actualizar(Rol(id_rol=id_rol, nombre_rol=nombre, descripcion=descripcion))

    def eliminar_rol(self, id_rol: int) -> bool:
        if id_rol is None or id_rol <= 0:
            raise ValidacionDatosError("Identificador de rol no válido.")
        return self._modelo_rol.eliminar(id_rol)

    @staticmethod
    def _validar(nombre: str, descripcion: str):
        """Reglas de negocio: nombre obligatorio (3-50) y descripción máx. 150."""
        nombre = " ".join((nombre or "").split())
        descripcion = (descripcion or "").strip()

        if not nombre:
            raise ValidacionDatosError("El nombre del rol es obligatorio.")
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValidacionDatosError("El nombre del rol debe tener entre 3 y 50 caracteres.")
        if len(descripcion) > 150:
            raise ValidacionDatosError("La descripción no puede superar los 150 caracteres.")
        return nombre, descripcion
