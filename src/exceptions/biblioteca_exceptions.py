class BibliotecaException(Exception):
    """Excepción base del sistema (errores técnicos: BD, criptografía, etc.)."""
    pass


class ValidacionDatosError(BibliotecaException):
    """Error de reglas de negocio o de datos ingresados por el operador."""
    pass
