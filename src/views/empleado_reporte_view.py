from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView
from PySide6.QtCore import Qt

#1. Importamos la vista compilada que acabamos de crear en Qt Designer
from views.frm_empleado_reporte_ui import Ui_Form

#2. Importamos los controladores necesarios
from controllers.empleado_controller import EmpleadoController
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import BibliotecaException


class EmpleadoReporteView(QWidget, Ui_Form):
    """Ventana dedicada exclusivamente a consultas y reportes de personal."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Instanciamos los controladores
        self._controlador_emp = EmpleadoController()
        self._controlador_rol = RolController()

        # Ajustamos el ancho de las columnas de la tabla
        self._configurar_cabeceras()

        # PASO 1: Sincronización Dinámica (Llenar ComboBox desde Base de Datos)
        self._cargar_combo_roles()

        # PASO 2: Reactividad. Conectamos CUALQUIER cambio en los filtros al mismo método.
        self.cbo_rol.currentIndexChanged.connect(self._aplicar_filtros)
        self.cbo_turno.currentIndexChanged.connect(self._aplicar_filtros)
        self.chk_activos.stateChanged.connect(self._aplicar_filtros)
        self.txt_buscar.textChanged.connect(self._aplicar_filtros)

        # Carga inicial de datos al abrir la ventana
        self._aplicar_filtros()

    def _configurar_cabeceras(self):
        cabecera = self.tbl_reporte.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents) # Código
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents) # DNI
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)          # Nombres
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents) # Cargo
        cabecera.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents) # Turno
        cabecera.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents) # Rol
        cabecera.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents) # Estado

    def _cargar_combo_roles(self):
        """Consulta la BD y puebla el ComboBox dinámicamente."""
        try:
            roles = self._controlador_rol.obtener_roles()
            self.cbo_rol.clear()

            # Opción por defecto (ID = 0 para que MySQL traiga todos)
            self.cbo_rol.addItem("-- Todos los Roles --", 0)

            for r in roles:
                self.cbo_rol.addItem(r.nombre_rol, r.id_rol)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los roles: {error}")

    def _aplicar_filtros(self):
        """Se dispara instantáneamente cada vez que el usuario toca un combo, check o escribe."""
        try:
            # Rescatar el valor actual de los 4 filtros
            rol_id = self.cbo_rol.currentData()
            if rol_id is None:
                rol_id = 0

            turno = self.cbo_turno.currentText()
            solo_activos = self.chk_activos.isChecked()
            criterio = self.txt_buscar.text()

            # Enviar los 4 datos al controlador y recibir la lista filtrada
            lista_filtrada = self._controlador_emp.filtrar_reporte(rol_id, turno, solo_activos, criterio)

            # Dibujar la tabla
            self._renderizar_tabla(lista_filtrada)
        except BibliotecaException as ex:
            # Comentamos el QMessageBox para que no sea molesto si el usuario tipea rápido,
            # pero lo dejamos impreso en consola para el desarrollador.
            print(f"Error de filtro: {ex}")

    def _renderizar_tabla(self, lista):
        """Dibuja los registros y aplica UX defensiva (solo lectura)."""
        self.tbl_reporte.setRowCount(0)
        for fila_idx, emp in enumerate(lista):
            self.tbl_reporte.insertRow(fila_idx)

            item_cod = QTableWidgetItem(emp['codigo_empleado'])
            item_cod.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_dni = QTableWidgetItem(emp['numero_documento'])
            item_dni.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nom = QTableWidgetItem(emp['nombre_completo'])
            item_cargo = QTableWidgetItem(emp['cargo'])
            item_turno = QTableWidgetItem(emp['turno'])
            item_rol = QTableWidgetItem(emp['rol'])

            item_estado = QTableWidgetItem(emp['estado'])
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Blindaje UX: Hacer que no se puedan editar dando doble clic
            for item in (item_cod, item_dni, item_nom, item_cargo, item_turno, item_rol, item_estado):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

            self.tbl_reporte.setItem(fila_idx, 0, item_cod)
            self.tbl_reporte.setItem(fila_idx, 1, item_dni)
            self.tbl_reporte.setItem(fila_idx, 2, item_nom)
            self.tbl_reporte.setItem(fila_idx, 3, item_cargo)
            self.tbl_reporte.setItem(fila_idx, 4, item_turno)
            self.tbl_reporte.setItem(fila_idx, 5, item_rol)
            self.tbl_reporte.setItem(fila_idx, 6, item_estado)
