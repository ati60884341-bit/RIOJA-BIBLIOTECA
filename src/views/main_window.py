from PySide6.QtWidgets import QMainWindow
from views.frm_main_ui import Ui_MainWindow
from views.programa_list_view import ProgramaListView
from views.empleado_list_view import EmpleadoListView
from views.rol_list_view import RolListView

class MainWindow(QMainWindow, Ui_MainWindow):
    """Contenedor principal de navegación corporativa del sistema."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Referencias en memoria RAM para evitar que el Garbage Collector cierre las ventanas
        self._ventana_programas = None
        self._ventana_empleados = None
        self._ventana_roles = None

        # Menú Archivo: cierra la aplicación
        self.action_salir.triggered.connect(self.close)

        # Conexión de acciones del menú Mantenimiento (QAction.triggered)
        self.action_programas.triggered.connect(self._abrir_modulo_programas)
        self.action_empleados.triggered.connect(self._abrir_modulo_empleados)
        self.action_roles.triggered.connect(self._abrir_modulo_roles)

    def _abrir_modulo_programas(self):
        """Despliega o trae al frente el catálogo de Programas de Estudio."""
        if self._ventana_programas is None or not self._ventana_programas.isVisible():
            self._ventana_programas = ProgramaListView()
            self._ventana_programas.show()
        else:
            self._ventana_programas.activateWindow()
            self._ventana_programas.raise_()

    def _abrir_modulo_empleados(self):
        """Despliega o trae al frente el catálogo de Empleados."""
        if self._ventana_empleados is None or not self._ventana_empleados.isVisible():
            self._ventana_empleados = EmpleadoListView()
            self._ventana_empleados.show()
        else:
            self._ventana_empleados.activateWindow()
            self._ventana_empleados.raise_()

    def _abrir_modulo_roles(self):
        """Despliega o trae al frente el catálogo de Roles."""
        if self._ventana_roles is None or not self._ventana_roles.isVisible():
            self._ventana_roles = RolListView()
            self._ventana_roles.show()
        else:
            self._ventana_roles.activateWindow()
            self._ventana_roles.raise_()
