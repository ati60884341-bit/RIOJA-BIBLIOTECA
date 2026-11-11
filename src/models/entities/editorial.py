class Editorial:
    """Entidad pura: Editorial."""

    def __init__(self, nombre: str, id_editorial: int = None):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la editorial es obligatorio.")
            
        self._id_editorial: int = id_editorial
        self._nombre: str = nombre.strip()

    @property
    def id_editorial(self) -> int:
        return self._id_editorial

    @id_editorial.setter
    def id_editorial(self, valor: int):
        self._id_editorial = valor

    @property
    def nombre(self) -> str:
        return self._nombre