class Usuario:
    """Clase base de dominio: refleja la tabla `usuarios` (datos de identidad y acceso).

    Es la clase PADRE de Empleado (y en el futuro de Estudiante), igual que en la
    base de datos `empleados.usuario_id` y `estudiantes.usuario_id` apuntan a
    `usuarios.id_usuario` (herencia 1 a 1).
    """

    def __init__(
        self,
        id_usuario: int = None,
        numero_documento: str = "",
        nombres: str = "",
        apellidos: str = "",
        nombre_usuario: str = "",
        clave_hash: str = "",
        rol_id: int = None,
        rol: str = "",
        estado: str = "Activo",
        nombre_completo: str = ""
    ):
        self.id_usuario = id_usuario
        self.numero_documento = numero_documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.nombre_usuario = nombre_usuario      # columna `username`
        self.clave_hash = clave_hash              # columna `password_hash` (BCrypt, 60 caracteres)
        self.rol_id = rol_id                      # FK hacia `roles.id_rol`
        self.rol = rol                            # nombre del rol (solo lectura, viene del JOIN)
        self.estado = estado                      # 'Activo' / 'Inactivo' (columna `es_activo`)
        self._nombre_completo = nombre_completo

    @property
    def nombre_completo(self) -> str:
        """Usa el valor recibido de la BD (login) o lo arma con nombres + apellidos."""
        if self._nombre_completo:
            return self._nombre_completo
        return f"{self.nombres} {self.apellidos}".strip()

    @nombre_completo.setter
    def nombre_completo(self, valor: str):
        self._nombre_completo = valor

    @property
    def es_activo(self) -> bool:
        return self.estado == "Activo"

    def __repr__(self) -> str:
        return f"<Usuario id={self.id_usuario} usuario='{self.nombre_usuario}' rol='{self.rol}'>"
