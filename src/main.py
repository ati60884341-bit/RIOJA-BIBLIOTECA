import sys
from PySide6.QtWidgets import QApplication, QDialog

from views.login_dialog import LoginDialog
from views.main_window import MainWindow

def principal():
    aplicacion = QApplication(sys.argv)

    # 1. Despliegue modal del Login
    cuadro_login = LoginDialog()

    # exec() detiene la ejecución hasta que el diálogo sea aceptado o cerrado
    if cuadro_login.exec() == QDialog.DialogCode.Accepted:
        # 2. Credenciales válidas: despliegue de la ventana principal corporativa
        ventana_principal = MainWindow()
        ventana_principal.show()
        sys.exit(aplicacion.exec())
    else:
        # Cierre limpio del proceso si se cancela la autenticación
        sys.exit(0)

if __name__ == '__main__':
    principal()
