import bcrypt
from models.usuario_model import UsuarioModel
from models.entities.usuario import Usuario
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException

class AuthController:
    """Controlador que orquesta las reglas de negocio de autenticación y verificación BCrypt."""

    def __init__(self):
        self._modelo_usuario = UsuarioModel()

    def iniciar_sesion(self, usuario_ingresado: str, clave_ingresada: str) -> Usuario:
        """Valida entradas, recupera la entidad y verifica el hash criptográfico."""
        usuario_limpio = usuario_ingresado.strip()
        clave_limpia = clave_ingresada.strip()

        # 1. Regla de validación: Campos obligatorios
        if not usuario_limpio or not clave_limpia:
            raise ValidacionDatosError("Debe ingresar tanto el usuario como la contraseña.")

        # 2. Recuperación de la entidad desde MySQL vía DAO
        usuario = self._modelo_usuario.buscar_por_nombre_usuario(usuario_limpio)

        # 3. Regla defensiva: Rechazar si el usuario no existe o está inactivo
        if not usuario or usuario.estado != "Activo":
            raise ValidacionDatosError("Credenciales incorrectas o usuario inactivo.")

        # 4. Transformación obligatoria a secuencias de bytes (UTF-8) para BCrypt
        clave_bytes = clave_limpia.encode('utf-8')
        hash_guardado_bytes = usuario.clave_hash.encode('utf-8')

        try:
            # checkpw realiza el cómputo adaptativo en RAM extrayendo el Salt del hash guardado
            clave_es_válida = bcrypt.checkpw(clave_bytes, hash_guardado_bytes)
        except Exception as error_criptografico:
            raise BibliotecaException(f"Falla en el motor de seguridad criptográfica: {error_criptografico}")

        if not clave_es_válida:
            raise ValidacionDatosError("Credenciales incorrectas o usuario inactivo.")

        return usuario