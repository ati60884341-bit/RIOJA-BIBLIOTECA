from PySide6.QtWidgets import QDialog, QMessageBox

from views.frm_programa_form_ui import Ui_ProgramaFormDialog
from controllers.programa_controller import ProgramaController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class ProgramaFormDialog(QDialog, Ui_ProgramaFormDialog):
    """Formulario modal unificado para Crear y Editar Programas de Estudio."""

    def __init__(self, parent=None, id_programa_editar=None):
        super().__init__(parent)
        self.setupUi(self)

        self._controlador = ProgramaController()
        self._id_programa_actual = id_programa_editar

        self.txt_codigo_programa.setMaxLength(10)
        self.txt_nombre_programa.setMaxLength(120)

        if self._id_programa_actual is not None:
            self.setWindowTitle("Programas de Estudio - Modificar Programa")
            self.btn_guardar.setText("Actualizar Programa")
            self._poblar_datos_para_edicion()
        else:
            self.setWindowTitle("Programas de Estudio - Registrar Nuevo Programa")
            self.btn_guardar.setText("Registrar Programa")
            # Un programa nuevo siempre nace Activo
            self.chk_estado.setEnabled(False)

        self.btn_guardar.clicked.connect(self._al_guardar)
        self.btn_cancelar.clicked.connect(self.reject)

    def _poblar_datos_para_edicion(self):
        try:
            programa = self._controlador.obtener_programa_por_id(self._id_programa_actual)
            if programa is None:
                QMessageBox.warning(self, "Registro No Encontrado",
                                    "El programa seleccionado ya no existe en la base de datos.")
                self.btn_guardar.setEnabled(False)
                return
            self.txt_codigo_programa.setText(programa.codigo_programa)
            self.txt_nombre_programa.setText(programa.nombre_programa)
            self.chk_estado.setChecked(programa.es_activo)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Persistencia", str(error))
            self.btn_guardar.setEnabled(False)

    def _al_guardar(self):
        codigo = self.txt_codigo_programa.text()
        nombre = self.txt_nombre_programa.text()
        estado = "Activo" if self.chk_estado.isChecked() else "Inactivo"
        try:
            if self._id_programa_actual is None:
                self._controlador.registrar_programa(codigo, nombre)
                QMessageBox.information(self, "Registro Confirmado",
                                        "Programa de estudio registrado exitosamente.")
            else:
                self._controlador.actualizar_programa(self._id_programa_actual, codigo, nombre, estado)
                QMessageBox.information(self, "Actualización Exitosa",
                                        "Los datos del programa fueron modificados en el sistema.")
            self.accept()
        except ValidacionDatosError as advertencia:
            QMessageBox.warning(self, "Validación de Formulario", str(advertencia))
            self.txt_codigo_programa.setFocus()
        except BibliotecaException as error_bd:
            QMessageBox.critical(self, "Falla Transaccional", str(error_bd))
