from models.entities.usuario import Usuario


class Empleado(Usuario):
    """Clase HIJA de Usuario: refleja la tabla `empleados`.

    Tabla `empleados`:
        usuario_id       INT          (PK y FK -> usuarios.id_usuario)
        codigo_empleado  VARCHAR(20)
        cargo            VARCHAR(80)
        turno            VARCHAR(30)

    `usuario_id` NO se declara aquí: es el mismo `id_usuario` heredado de Usuario.
    Los datos de identidad y acceso (DNI, nombres, username, clave_hash, rol...) también
    se heredan, así que solo se añaden los 3 atributos propios del empleado.
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
        codigo_empleado: str = "",
        cargo: str = "",
        turno: str = "Mañana",
        rol: str = "",
        estado: str = "Activo"
    ):
        # 1. Inicializa la parte heredada (tabla usuarios)
        super().__init__(
            id_usuario=id_usuario,
            numero_documento=numero_documento,
            nombres=nombres,
            apellidos=apellidos,
            nombre_usuario=nombre_usuario,
            clave_hash=clave_hash,
            rol_id=rol_id,
            rol=rol,
            estado=estado
        )
        # 2. Atributos propios (tabla empleados)
        self.codigo_empleado = codigo_empleado
        self.cargo = cargo
        self.turno = turno

    @property
    def usuario_id(self) -> int:
        """Alias con el nombre de la columna de `empleados` (es el mismo id_usuario)."""
        return self.id_usuario

    def __repr__(self) -> str:
        return (f"<Empleado id={self.id_usuario} codigo='{self.codigo_empleado}' "
                f"usuario='{self.nombre_usuario}' cargo='{self.cargo}'>")
