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

        # Validaciones defensivas en la interfaz (QRegularExpressionValidator)
        self._configurar_validadores_interfaz()

        # El combo de roles se llena ANTES de poblar datos, para que findData() encuentre el rol
        self._cargar_combo_roles()

        # Inicializamos el modo Creación (porque el ID es None)
        if self._id_usuario_actual is None:
            self.setWindowTitle("Nuevo Colaborador")
            self.btn_guardar.setText("Guardar Empleado")
        else:
            self.setWindowTitle("Modificar Colaborador")
            self.btn_guardar.setText("Actualizar Datos")
            self._poblar_datos() # Llama a la función de abajo

        self.btn_guardar.clicked.connect(self._al_guardar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _configurar_validadores_interfaz(self):
        """Aplica restricciones y máscaras sobre los campos de captura de texto."""
        # DNI: exclusivamente 8 dígitos numéricos
        regex_dni = QRegularExpression(r"^[0-9]{8}$")
        self.txt_numero_documento.setValidator(QRegularExpressionValidator(regex_dni, self))
        self.txt_numero_documento.setMaxLength(8)

        # Límites máximos acordes a las columnas de base de datos
        self.txt_codigo_empleado.setMaxLength(20)
        self.txt_nombres.setMaxLength(80)
        self.txt_apellidos.setMaxLength(80)
        self.txt_username.setMaxLength(100)

    # ---------------------------------------------------------------
    # Paso 2.1: Llenar el desplegable de roles (ID oculto en userData)
    # ---------------------------------------------------------------
    def _cargar_combo_roles(self):
        try:
            roles = self._controlador_rol.obtener_roles()
            self.cbo_rol.clear()
            self.cbo_rol.addItem("-- Seleccione un Rol --", None)

            for r in roles:
                # addItem("Texto Visible", Dato_Oculto)
                self.cbo_rol.addItem(r.nombre_rol, r.id_rol)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error", str(error))
            self.btn_guardar.setEnabled(False)

    # ---------------------------------------------------------------
    # Paso 4.3: Cargar los datos del registro en modo Edición
    # ---------------------------------------------------------------
    def _poblar_datos(self):
        try:
            datos = self._controlador_emp.obtener_empleado_por_id(self._id_usuario_actual)
            self.txt_numero_documento.setText(datos['numero_documento'])
            self.txt_nombres.setText(datos['nombres'])
            self.txt_apellidos.setText(datos['apellidos'])
            self.txt_username.setText(datos['username'])
            self.txt_codigo_empleado.setText(datos['codigo_empleado'])
            self.txt_cargo.setText(datos['cargo'])
            self.cbo_turno.setCurrentText(datos['turno'])

            # Buscar el rol numérico y seleccionarlo en el combo
            indice_rol = self.cbo_rol.findData(datos['rol_id'])
            if indice_rol >= 0:
                self.cbo_rol.setCurrentIndex(indice_rol)

            self.txt_numero_documento.setReadOnly(True)
            self.txt_codigo_empleado.setReadOnly(True)
        except BibliotecaException as e:
            QMessageBox.critical(self, "Error", str(e))

    # ---------------------------------------------------------------
    # Paso 3.3 / 4.3: Guardar (Inserción o Actualización)
    # ---------------------------------------------------------------
    def _al_guardar(self):
        doc = self.txt_numero_documento.text()
        nom = self.txt_nombres.text()
        ape = self.txt_apellidos.text()
        user = self.txt_username.text()
        pwd = self.txt_password.text()
        cod = self.txt_codigo_empleado.text()
        cargo = self.txt_cargo.text()
        turno = self.cbo_turno.currentText()
        rol_id = self.cbo_rol.currentData() # Extrae el ID oculto numérico

        if rol_id is None:
            QMessageBox.warning(self, "Atención", "Debe seleccionar un Rol.")
            return

        try:
            if self._id_usuario_actual is None:
                id_nuevo = self._controlador_emp.registrar_empleado(
                    doc, nom, ape, user, pwd, rol_id, cod, cargo, turno
                )
                QMessageBox.information(self, "Éxito", f"Empleado registrado con ID: {id_nuevo}")
                self.accept()
            else:
                self._controlador_emp.actualizar_empleado(
                    self._id_usuario_actual, doc, nom, ape, user, pwd, rol_id, cod, cargo, turno
                )
                QMessageBox.information(self, "Éxito", "Colaborador actualizado.")
                self.accept()

        except ValidacionDatosError as advertencia:
            QMessageBox.warning(self, "Datos Inválidos", str(advertencia))
        except BibliotecaException as error_bd:
            QMessageBox.critical(self, "Error BD", str(error_bd))
