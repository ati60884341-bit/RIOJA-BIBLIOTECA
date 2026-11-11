class Rol:
    """Clase pura de dominio que representa un Rol institucional asignable a un colaborador."""

    def __init__(self, id_rol: int = None, nombre_rol: str = "",
                 descripcion: str = "", total_usuarios: int = 0):
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.descripcion = descripcion or ""
        self.total_usuarios = total_usuarios or 0

    def __repr__(self) -> str:
        return f"<Rol id={self.id_rol} nombre='{self.nombre_rol}'>"
