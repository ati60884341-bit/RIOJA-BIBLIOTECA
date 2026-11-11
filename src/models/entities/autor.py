class Autor:
    """Entidad pura: Autor."""

    def __init__(self, nombre: str, nacionalidad: str = "Desconocida", id_autor: int = None):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del autor es obligatorio.")
            
        self._id_autor: int = id_autor
        self._nombre: str = nombre.strip()
        self._nacionalidad: str = nacionalidad.strip()

    @property
    def id_autor(self) -> int:
        return self._id_autor

    @id_autor.setter
    def id_autor(self, valor: int):
        self._id_autor = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def nacionalidad(self) -> str:
        return self._nacionalidad