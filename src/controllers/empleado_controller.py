import re
import bcrypt
from typing import List, Dict, Any
from models.empleado_model import EmpleadoModel
from models.entities.empleado import Empleado
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException

class EmpleadoController:
    """Controlador que valida reglas de negocio y orquesta la persistencia."""

    def __init__(self):
        self._modelo_empleado = EmpleadoModel()

    def registrar_empleado(
        self, documento: str, nombres: str, apellidos: str,
        username: str, clave_plana: str, rol_id: int,
        codigo: str, cargo: str, turno: str
    ) -> int:
        """Sanitiza campos, valida unicidad/formato, calcula hash y registra."""
        doc, nom, ape, user, cod, car = self._sanitizar_campos(
            documento, nombres, apellidos, username, codigo, cargo
        )

        if not all([doc, nom, ape, user, clave_plana, cod, car]):
            raise ValidacionDatosError("Todos los campos marcados son obligatorios.")

        self._validar_reglas_comunes(doc, user, rol_id)

        if len(clave_plana) < 6:
            raise ValidacionDatosError("La contraseña debe tener una longitud mínima de 6 caracteres.")

        # Cifrado adaptativo con factor de costo 12
        clave_bytes = clave_plana.encode('utf-8')
        sal_segura = bcrypt.gensalt(rounds=12)
        clave_hash = bcrypt.hashpw(clave_bytes, sal_segura).decode('utf-8')

        nuevo_empleado = Empleado(
            numero_documento=doc,
            nombres=nom,
            apellidos=ape,
            nombre_usuario=user,
            clave_hash=clave_hash,
            rol_id=rol_id,
            codigo_empleado=cod,
            cargo=car,
            turno=turno
        )
        return self._modelo_empleado.registrar(nuevo_empleado)

    def actualizar_empleado(
        self, id_usuario: int, documento: str, nombres: str, apellidos: str,
        username: str, clave_plana: str, rol_id: int,
        codigo: str, cargo: str, turno: str
    ) -> bool:
        """Valida entradas y actualiza. Procesa la clave solo si fue ingresada."""
        if id_usuario is None or id_usuario <= 0:
            raise ValidacionDatosError("Identificador relacional de colaborador no válido.")

        doc, nom, ape, user, cod, car = self._sanitizar_campos(
            documento, nombres, apellidos, username, codigo, cargo
        )

        if not all([doc, nom, ape, user, cod, car]):
            raise ValidacionDatosError("Todos los campos marcados son obligatorios.")

        self._validar_reglas_comunes(doc, user, rol_id)

        # Evaluación condicional de la contraseña
        clave_hash = ""
        if clave_plana.strip():
            if len(clave_plana) < 6:
                raise ValidacionDatosError("La nueva contraseña debe tener un mínimo de 6 caracteres.")
            clave_bytes = clave_plana.encode('utf-8')
            sal_segura = bcrypt.gensalt(rounds=12)
            clave_hash = bcrypt.hashpw(clave_bytes, sal_segura).decode('utf-8')

        empleado_actualizado = Empleado(
            id_usuario=id_usuario,
            numero_documento=doc,
            nombres=nom,
            apellidos=ape,
            nombre_usuario=user,
            clave_hash=clave_hash,
            rol_id=rol_id,
            codigo_empleado=cod,
            cargo=car,
            turno=turno
        )
        return self._modelo_empleado.actualizar(empleado_actualizado)

    def obtener_empleado_por_id(self, id_usuario: int) -> Dict[str, Any]:
        """Obtiene la entidad de MySQL para transferirla al formulario modal."""
        if id_usuario is None or id_usuario <= 0:
            raise ValidacionDatosError("Identificador no válido.")
        datos = self._modelo_empleado.obtener_por_id(id_usuario)
        if not datos:
            raise BibliotecaException("El colaborador no fue encontrado en la base de datos.")
        return datos

    def listar_empleados(self, criterio: str = "") -> List[Dict[str, Any]]:
        """Recupera la lista general de colaboradores."""
        return self._modelo_empleado.listar(criterio.strip())

    def _sanitizar_campos(self, doc, nom, ape, user, cod, car):
        return (
            doc.strip(),
            nom.strip(),
            ape.strip(),
            user.strip().lower(),
            cod.strip().upper(),
            car.strip()
        )

    def _validar_reglas_comunes(self, doc: str, user: str, rol_id: int):
        if len(doc) != 8 or not doc.isdigit():
            raise ValidacionDatosError("El DNI debe contener exactamente 8 dígitos numéricos.")
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron_correo, user):
            raise ValidacionDatosError("El formato del usuario/correo electrónico no es válido.")
        if rol_id is None or rol_id <= 0:
            raise ValidacionDatosError("Debe seleccionar un Rol válido del catálogo institucional.")