from PySide6.QtWidgets import QMainWindow

from views.ui.frm_main_ui import Ui_MainWindow
from views.programa_list_view import ProgramaListView
from views.empleado_list_view import EmpleadoListView


class MainWindow(QMainWindow, Ui_MainWindow):
    """Controlador visual de la Ventana Principal del sistema corporativo."""

    def __init__(self):
        super().__init__()

        # 1. Cargar diseño con barra de menú
        self.setupUi(self)

        # 2. Variable para mantener viva la referencia de la subventana en memoria RAM
        self._ventana_programas = None
        self._ventana_empleados = None

        # 3. Vincular acción del menú (QAction dispara la señal triggered)
        self.action_programas.triggered.connect(self._abrir_modulo_programas)
        self.action_empleados.triggered.connect(self._abrir_modulo_empleados)

    def _abrir_modulo_programas(self):
        """Instancia y muestra la ventana del catálogo de Programas de Estudio."""
        if self._ventana_programas is None or not self._ventana_programas.isVisible():
            self._ventana_programas = ProgramaListView()
            self._ventana_programas.show()
        else:
            self._ventana_programas.activateWindow()
            self._ventana_programas.raise_()

    def _abrir_modulo_empleados(self):
        """Instancia y muestra la ventana del catálogo de Colaboradores."""
        if self._ventana_empleados is None or not self._ventana_empleados.isVisible():
            self._ventana_empleados = EmpleadoListView()
            self._ventana_empleados.show()
        else:
            self._ventana_empleados.activateWindow()
            self._ventana_empleados.raise_()
