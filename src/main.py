import sys
from PySide6.QtWidgets import QApplication, QDialog
from views.login_dialog import LoginDialog
from views.main_window import MainWindow

def principal():
    aplicacion = QApplication(sys.argv)

    # 1. Despliegue modal del control de acceso
    cuadro_login = LoginDialog()
    if cuadro_login.exec() == QDialog.DialogCode.Accepted:
        # 2. Credenciales válidas: apertura del centro de mando principal
        ventana_principal = MainWindow()
        ventana_principal.show()
        sys.exit(aplicacion.exec())
    else:
        # Cierre limpio si el operador cancela el inicio de sesión
        sys.exit(0)

if __name__ == "__main__":
    principal()
