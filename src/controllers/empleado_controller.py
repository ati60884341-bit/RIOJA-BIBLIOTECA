import bcrypt
from models.empleado_model import EmpleadoModel
from models.entities.empleado import Empleado
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class EmpleadoController:
    """Controlador que valida reglas de negocio y orquesta la persistencia."""

    def __init__(self):
        self._modelo_empleado = EmpleadoModel()

    # ---------------------------------------------------------------
    # Paso 1.2: Listar / Buscar
    # ---------------------------------------------------------------
    def listar_empleados(self, criterio: str = "") -> list:
        """Limpia el texto ingresado y solicita la lista al DAO."""
        return self._modelo_empleado.listar(criterio.strip())

    # ---------------------------------------------------------------
    # Paso 3.2: Registrar (cifrado bcrypt)
    # ---------------------------------------------------------------
    def registrar_empleado(
        self, documento: str, nombres: str, apellidos: str,
        username: str, clave_plana: str, rol_id: int,
        codigo: str, cargo: str, turno: str
    ) -> int:

        if not clave_plana or len(clave_plana) < 6:
            raise ValidacionDatosError("La contraseña debe tener mínimo 6 caracteres.")

        # Cifrado con BCrypt (Costo 12)
        sal = bcrypt.gensalt(rounds=12)
        clave_hash = bcrypt.hashpw(clave_plana.encode('utf-8'), sal).decode('utf-8')

        nuevo = Empleado(
            numero_documento=documento, nombres=nombres, apellidos=apellidos,
            nombre_usuario=username, clave_hash=clave_hash, rol_id=rol_id,
            codigo_empleado=codigo, cargo=cargo, turno=turno
        )
        return self._modelo_empleado.registrar(nuevo)

    # ---------------------------------------------------------------
    # Paso 4.2: Obtener por ID y Actualizar
    # ---------------------------------------------------------------
    def obtener_empleado_por_id(self, id_usuario: int) -> dict:
        return self._modelo_empleado.obtener_por_id(id_usuario)

    def actualizar_empleado(
        self, id_usuario: int, documento: str, nombres: str, apellidos: str,
        username: str, clave_plana: str, rol_id: int,
        codigo: str, cargo: str, turno: str
    ) -> bool:

        # Si deja la clave vacía, no calculamos el hash
        clave_hash = ""
        if clave_plana.strip():
            sal = bcrypt.gensalt(rounds=12)
            clave_hash = bcrypt.hashpw(clave_plana.encode('utf-8'), sal).decode('utf-8')

        emp_modificado = Empleado(
            id_usuario=id_usuario, numero_documento=documento, nombres=nombres,
            apellidos=apellidos, nombre_usuario=username, clave_hash=clave_hash,
            rol_id=rol_id, codigo_empleado=codigo, cargo=cargo, turno=turno
        )
        return self._modelo_empleado.actualizar(emp_modificado)

    # ---------------------------------------------------------------
    # Paso 5.3: Eliminar (protege al Administrador Principal)
    # ---------------------------------------------------------------
    def eliminar_empleado(self, id_usuario: int, logico: bool = True) -> bool:
        if id_usuario is None or id_usuario <= 0:
            raise ValidacionDatosError("Identificador de empleado no válido.")
        if id_usuario == 1:
            raise ValidacionDatosError("Operación denegada: No se puede eliminar al Administrador Principal del sistema.")
        return self._modelo_empleado.eliminar(id_usuario, logico)
