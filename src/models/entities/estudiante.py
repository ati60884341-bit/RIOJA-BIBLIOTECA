from models.entities.usuario import Usuario

class Estudiante(Usuario):
    """Entidad pura: Representa al alumnado de la institución."""

    def __init__(self, id_usuario: int, numero_documento: str, nombres: str, 
                 apellidos: str, correo: str, es_activo: bool, carnet: str, 
                 id_programa: int, nombre_programa: str, tiene_sancion: bool = False, 
                 id_rol: int = 4, nombre_rol: str = 'Estudiante', semestre: str = 'I'):
        super().__init__(id_usuario, numero_documento, nombres, apellidos, correo, id_rol, nombre_rol, es_activo)
        self._carnet: str = carnet
        self._id_programa: int = id_programa
        self._nombre_programa: str = nombre_programa
        self._semestre: str = semestre
        self._tiene_sancion: bool = tiene_sancion

    @property
    def carnet(self) -> str: return self._carnet
    @property
    def id_programa(self) -> int: return self._id_programa
    @property
    def nombre_programa(self) -> str: return self._nombre_programa
    @property
    def semestre(self) -> str: return self._semestre
    @property
    def tiene_sancion(self) -> bool: return self._tiene_sancion