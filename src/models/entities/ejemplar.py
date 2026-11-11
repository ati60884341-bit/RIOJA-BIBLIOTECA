class Ejemplar:
    """Entidad pura: Ejemplar físico patrimonial de un libro."""

    def __init__(self, codigo_patrimonial: str, id_libro: int = None, estado_conservacion: str = "Bueno", esta_disponible: bool = True, id_ejemplar: int = None):
        if not codigo_patrimonial or not codigo_patrimonial.strip():
            raise ValueError("El código patrimonial del ejemplar es obligatorio.")

        self._id_ejemplar: int = id_ejemplar
        self._id_libro: int = id_libro
        self._codigo_patrimonial: str = codigo_patrimonial.strip()
        self._estado_conservacion: str = estado_conservacion
        self._esta_disponible: bool = esta_disponible

    @property
    def id_ejemplar(self) -> int:
        return self._id_ejemplar

    @property
    def id_libro(self) -> int:
        return self._id_libro

    @property
    def codigo_patrimonial(self) -> str:
        return self._codigo_patrimonial

    @property
    def estado_conservacion(self) -> str:
        return self._estado_conservacion

    @property
    def esta_disponible(self) -> bool:
        return self._esta_disponible