from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit

from views.frm_login_ui import Ui_Form
from controllers.auth_controller import AuthController
from exceptions.biblioteca_exceptions import ValidacionDatosError, BibliotecaException


class LoginDialog(QDialog, Ui_Form):
    """Vista modal encargada de capturar credenciales y mostrar respuestas al operador."""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Cargar el diseño de interfaz gráfica
        self.setupUi(self)

        # 2. Instanciar el controlador de seguridad
        self._controlador_autenticacion = AuthController()

        # 3. Máscara de seguridad para no mostrar la contraseña en pantalla
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        # 4. Vincular el botón a la ranura (slot) con nombre en español
        self.btn_ingresar.clicked.connect(self._al_hacer_clic_ingresar)

    def _al_hacer_clic_ingresar(self):
        """Maneja el evento de solicitud de inicio de sesión."""
        usuario_tipeado = self.txt_usuario.text()
        clave_tipeada = self.txt_password.text()

        try:
            # Delegación total de la lógica de negocio al controlador
            self._controlador_autenticacion.iniciar_sesion(usuario_tipeado, clave_tipeada)

            # Cierre con estado de éxito (QDialog.DialogCode.Accepted)
            self.accept()

        except ValidacionDatosError as advertencia:
            QMessageBox.warning(self, "Acceso Denegado", str(advertencia))
            self.txt_password.clear()
            self.txt_password.setFocus()

        except BibliotecaException as error_sistema:
            QMessageBox.critical(self, "Error de Sistema", str(error_sistema))
