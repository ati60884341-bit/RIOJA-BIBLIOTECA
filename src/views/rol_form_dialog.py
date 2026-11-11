from PySide6.QtWidgets import QDialog, QMessageBox

from views.frm_rol_form_ui import Ui_RolFormDialog
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class RolFormDialog(QDialog, Ui_RolFormDialog):
    """Formulario modal unificado para Crear y Editar roles."""

    LIMITE_DESCRIPCION = 150

    def __init__(self, parent=None, id_rol_editar=None):
        super().__init__(parent)
        self.setupUi(self)

        self._controlador = RolController()
        self._id_rol_actual = id_rol_editar

        self.txt_nombre_rol.setMaxLength(50)
        self.txt_descripcion.textChanged.connect(self._limitar_descripcion)

        if self._id_rol_actual is not None:
            self.setWindowTitle("Gestión de Roles - Modificar Rol")
            self.btn_guardar.setText("Actualizar Rol")
            self._poblar_datos_para_edicion()
        else:
            self.setWindowTitle("Gestión de Roles - Registrar Nuevo Rol")
            self.btn_guardar.setText("Registrar Rol")

        self.btn_guardar.clicked.connect(self._al_guardar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _limitar_descripcion(self):
        """QPlainTextEdit no tiene maxLength: se recorta manualmente."""
        texto = self.txt_descripcion.toPlainText()
        if len(texto) > self.LIMITE_DESCRIPCION:
            self.txt_descripcion.blockSignals(True)
            self.txt_descripcion.setPlainText(texto[:self.LIMITE_DESCRIPCION])
            cursor = self.txt_descripcion.textCursor()
            cursor.movePosition(cursor.MoveOperation.End)
            self.txt_descripcion.setTextCursor(cursor)
            self.txt_descripcion.blockSignals(False)

    def _poblar_datos_para_edicion(self):
        try:
            rol = self._controlador.obtener_rol_por_id(self._id_rol_actual)
            self.txt_nombre_rol.setText(rol.nombre_rol)
            self.txt_descripcion.setPlainText(rol.descripcion)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Persistencia", str(error))
            self.btn_guardar.setEnabled(False)

    def _al_guardar(self):
        nombre = self.txt_nombre_rol.text()
        descripcion = self.txt_descripcion.toPlainText()
        try:
            if self._id_rol_actual is None:
                id_nuevo = self._controlador.registrar_rol(nombre, descripcion)
                QMessageBox.information(self, "Registro Confirmado",
                                        f"Rol registrado exitosamente con ID: {id_nuevo}")
            else:
                self._controlador.actualizar_rol(self._id_rol_actual, nombre, descripcion)
                QMessageBox.information(self, "Actualización Exitosa",
                                        "Los datos del rol fueron modificados en el sistema.")
            self.accept()
        except ValidacionDatosError as advertencia:
            QMessageBox.warning(self, "Validación de Formulario", str(advertencia))
            self.txt_nombre_rol.setFocus()
        except BibliotecaException as error_bd:
            QMessageBox.critical(self, "Falla Transaccional", str(error_bd))
