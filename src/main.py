import sys
from PyQt6.QtWidgets import QApplication, QDialog
from src.views.login_dialog import LoginDialog
from src.views.main_window import MainWindow

def principal():
    aplicacion = QApplication(sys.argv)

    # 1. Despliegue modal del Login[cite: 9]
    cuadro_login = LoginDialog()

    # exec() detiene la ejecución hasta que el diálogo sea aceptado o cerrado[cite: 9]
    if cuadro_login.exec() == QDialog.DialogCode.Accepted:
        # 2. Credenciales válidas: despliegue de la ventana principal corporativa[cite: 9]
        ventana_principal = MainWindow()
        ventana_principal.show()
        sys.exit(aplicacion.exec())
    else:
        # Cierre limpio del proceso si se cancela la autenticación[cite: 9]
        sys.exit(0)

if __name__ == '__main__':
    principal()