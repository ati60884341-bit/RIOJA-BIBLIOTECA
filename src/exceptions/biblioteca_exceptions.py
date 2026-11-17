class BibliotecaException(Exception):
    """Excepción base del sistema (errores técnicos: BD, criptografía, etc.)."""
    pass


class ValidacionDatosError(BibliotecaException):
    """Error de reglas de negocio o de datos ingresados por el operador."""
    pass


class IntegridadReferencialError(BibliotecaException):
    """El registro no se puede borrar físicamente: tiene registros hijos vinculados (MySQL 1451)."""
    pass
