class Usuario:
    """Clase pura de dominio que representa a la persona autenticada en el sistema."""

    def __init__(
        self,
        id_usuario: int = None,
        nombre_usuario: str = "",
        nombre_completo: str = "",
        rol: str = "",
        estado: str = "Activo",
        clave_hash: str = ""
    ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.nombre_completo = nombre_completo
        self.rol = rol
        self.estado = estado
        self.clave_hash = clave_hash  # Hash BCrypt de 60 caracteres entregado por la BD

    def __repr__(self) -> str:
        return f"<Usuario id={self.id_usuario} usuario='{self.nombre_usuario}' rol='{self.rol}'>"