from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

from views.frm_empleado_form_ui import Ui_EmpleadoFormDialog
from controllers.empleado_controller import EmpleadoController
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException

class EmpleadoFormDialog(QDialog, Ui_EmpleadoFormDialog):
    """Formulario modal unificado para Crear y Editar colaboradores (Principio DRY)."""

    def __init__(self, parent=None, id_usuario_editar=None):
        super().__init__(parent)
        self.setupUi(self)

        self._controlador_emp = EmpleadoController()
        self._controlador_rol = RolController()
        self._id_usuario_actual = id_usuario_editar

        # 1. Configuración de UX: Validadores en tiempo de diseño
        self._configurar_validadores_interfaz()

        # 2. Carga dinámica del catálogo de roles desde MySQL
        self._cargar_combo_roles()

        # 3. Polimorfismo de estado: Adaptar la interfaz según el modo
        if self._id_usuario_actual is not None:
            self.setWindowTitle("Gestión de Personal - Modificar Colaborador")
            self.btn_guardar.setText("Actualizar Datos")
            self._poblar_datos_para_edicion()
        else:
            self.setWindowTitle("Gestión de Personal - Registrar Nuevo Colaborador")
            self.btn_guardar.setText("Registrar Empleado")

        # 4. Vinculación de Señales y Ranuras (Signals & Slots)
        self.btn_guardar.clicked.connect(self._al_guardar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _configurar_validadores_interfaz(self):
        """Aplica restricciones y máscaras sobre los campos de captura de texto."""
        # Restricción estricta de DNI: Exclusivamente números enteros hasta 8 dígitos
        regex_dni = QRegularExpression(r"^[0-9]{8}$")
        self.txt_numero_documento.setValidator(QRegularExpressionValidator(regex_dni, self))
        self.txt_numero_documento.setMaxLength(8)

        # Límites máximos acordes a las columnas de base de datos
        self.txt_codigo_empleado.setMaxLength(20)
        self.txt_nombres.setMaxLength(80)
        self.txt_apellidos.setMaxLength(80)
        self.txt_username.setMaxLength(100)

    def _cargar_combo_roles(self):
        """Puebla el selector visual almacenando id_rol como metadato en userData."""
        try:
            roles = self._controlador_rol.obtener_roles()
            self.cbo_rol.clear()
            self.cbo_rol.addItem("-- Seleccione un Rol --", None)
            for r in roles:
                self.cbo_rol.addItem(r.nombre_rol, r.id_rol)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Datos", f"No se pudo cargar el catálogo de roles: {error}")
            self.btn_guardar.setEnabled(False)

    def _poblar_datos_para_edicion(self):
        """Modo Edición: Recupera el registro y puebla los controles visuales."""
        try:
            datos = self._controlador_emp.obtener_empleado_por_id(self._id_usuario_actual)

            self.txt_numero_documento.setText(datos['numero_documento'])
            self.txt_nombres.setText(datos['nombres'])
            self.txt_apellidos.setText(datos['apellidos'])
            self.txt_username.setText(datos['username'])
            self.txt_codigo_empleado.setText(datos['codigo_empleado'])
            self.txt_cargo.setText(datos['cargo'])
            self.cbo_turno.setCurrentText(datos['turno'])

            # Mapeo inverso de la clave foránea en el QComboBox
            indice_rol = self.cbo_rol.findData(datos['rol_id'])
            if indice_rol >= 0:
                self.cbo_rol.setCurrentIndex(indice_rol)

            # Inmutabilidad de identidad: Bloqueo de claves naturales en edición
            self.txt_numero_documento.setReadOnly(True)
            self.txt_codigo_empleado.setReadOnly(True)

            # Mensaje orientativo de UX para contraseñas
            self.txt_password.setPlaceholderText("Deje en blanco para conservar la clave actual")

        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Persistencia", str(error))
            self.btn_guardar.setEnabled(False)

    def _al_guardar(self):
        """Captura datos, extrae metadatos y procesa la transacción."""
        doc = self.txt_numero_documento.text()
        nom = self.txt_nombres.text()
        ape = self.txt_apellidos.text()
        user = self.txt_username.text()
        pwd = self.txt_password.text()
        cod = self.txt_codigo_empleado.text()
        cargo = self.txt_cargo.text()
        turno = self.cbo_turno.currentText()
        rol_id = self.cbo_rol.currentData()

        # Validación inmediata del componente selector
        if rol_id is None:
            QMessageBox.warning(self, "Validación Requerida", "Debe asignar un rol válido al colaborador.")
            self.cbo_rol.setFocus()
            return

        try:
            if self._id_usuario_actual is None:
                # Flujo: INSERCIÓN
                id_nuevo = self._controlador_emp.registrar_empleado(
                    doc, nom, ape, user, pwd, rol_id, cod, cargo, turno
                )
                QMessageBox.information(
                    self,
                    "Registro Confirmado",
                    f"Colaborador registrado exitosamente con ID de Usuario: {id_nuevo}"
                )
            else:
                # Flujo: ACTUALIZACIÓN
                self._controlador_emp.actualizar_empleado(
                    self._id_usuario_actual, doc, nom, ape, user, pwd, rol_id, cod, cargo, turno
                )
                QMessageBox.information(
                    self,
                    "Actualización Exitosa",
                    "Los datos del colaborador fueron modificados en el sistema."
                )

            self.accept()

        except ValidacionDatosError as advertencia:
            # Respuesta interactiva ante errores de entrada del usuario
            QMessageBox.warning(self, "Validación de Formulario", str(advertencia))

        except BibliotecaException as error_bd:
            # Respuesta crítica ante fallas en base de datos o transacciones
            QMessageBox.critical(self, "Falla Transaccional", str(error_bd))
