from models.entities.editorial import Editorial
from models.entities.autor import Autor
from models.entities.ejemplar import Ejemplar

class Libro:
    """Entidad pura: Obra Intelectual. Agrupa Editorial, lista de Autores y Ejemplares."""

    def __init__(self, isbn: str, titulo: str, editorial: Editorial, anio_publicacion: int, numero_paginas: int, ubicacion_estante: str, subtitulo: str = None, lugar_publicacion: str = "Perú", id_libro: int = None):
        self._id_libro: int = id_libro
        self._isbn: str = isbn
        self._titulo: str = titulo
        self._subtitulo: str = subtitulo
        self._editorial: Editorial = editorial
        self._anio_publicacion: int = anio_publicacion
        self._lugar_publicacion: str = lugar_publicacion
        self._numero_paginas: int = numero_paginas
        self._ubicacion_estante: str = ubicacion_estante
        self._autores: list[Autor] = []
        self._ejemplares: list[Ejemplar] = []

    @property
    def id_libro(self) -> int:
        return self._id_libro

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def subtitulo(self) -> str:
        return self._subtitulo

    @property
    def editorial(self) -> Editorial:
        return self._editorial

    @property
    def anio_publicacion(self) -> int:
        return self._anio_publicacion

    @property
    def lugar_publicacion(self) -> str:
        return self._lugar_publicacion

    @property
    def numero_paginas(self) -> int:
        return self._numero_paginas

    @property
    def ubicacion_estante(self) -> str:
        return self._ubicacion_estante

    @property
    def autores(self) -> list[Autor]:
        return self._autores

    @property
    def ejemplares(self) -> list[Ejemplar]:
        return self._ejemplares

    def agregar_autor(self, autor: Autor):
        self._autores.append(autor)

    def agregar_ejemplar(self, ejemplar: Ejemplar):
        self._ejemplares.append(ejemplar)