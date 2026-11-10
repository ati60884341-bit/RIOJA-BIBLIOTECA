from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView, QDialog
from PySide6.QtCore import Qt

from views.ui.frm_empleado_list_ui import Ui_Form
from views.empleado_form_dialog import EmpleadoFormDialog
from controllers.empleado_controller import EmpleadoController
from exceptions.biblioteca_exceptions import BibliotecaException


class EmpleadoListView(QWidget, Ui_Form):
    """Vista del catálogo de Colaboradores (Capa Vista del MVC)."""

    def __init__(self, padre=None):
        super().__init__(padre)
        self.setupUi(self)

        self._controlador = EmpleadoController()

        self._configurar_cabeceras_tabla()
        self.txt_buscar.setClearButtonEnabled(True)

        self.btn_buscar.clicked.connect(self._ejecutar_busqueda)
        self.txt_buscar.returnPressed.connect(self._ejecutar_busqueda)
        self.txt_buscar.textChanged.connect(self._al_cambiar_texto_busqueda)

        self.tbl_empleados.itemSelectionChanged.connect(self._al_cambiar_seleccion_tabla)

        self.btn_nuevo.clicked.connect(self._al_hacer_clic_nuevo)
        self.btn_editar.clicked.connect(self._al_hacer_clic_editar)
        self.btn_eliminar.clicked.connect(self._al_hacer_clic_eliminar)

        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)

        self._cargar_grilla()

    def _configurar_cabeceras_tabla(self):
        cabecera = self.tbl_empleados.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

    def _cargar_grilla(self):
        try:
            lista_empleados = self._controlador.listar_empleados()
            self._renderizar_datos(lista_empleados)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Conexión", str(error))

    def _ejecutar_busqueda(self):
        criterio = self.txt_buscar.text()
        try:
            lista_filtrada = self._controlador.listar_empleados(criterio)
            self._renderizar_datos(lista_filtrada)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Búsqueda", str(error))

    def _al_cambiar_texto_busqueda(self, nuevo_texto: str):
        if not nuevo_texto.strip():
            self._cargar_grilla()

    def _renderizar_datos(self, coleccion_empleados):
        self.tbl_empleados.setRowCount(0)

        for fila_idx, empleado in enumerate(coleccion_empleados):
            self.tbl_empleados.insertRow(fila_idx)

            nombre_completo = f"{empleado.get('nombres', '')} {empleado.get('apellidos', '')}".strip()

            item_codigo = QTableWidgetItem(empleado.get('codigo_empleado', ''))
            item_codigo.setData(99, empleado.get('id_usuario'))
            item_codigo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_dni = QTableWidgetItem(empleado.get('numero_documento', ''))
            item_dni.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nombre = QTableWidgetItem(nombre_completo)

            item_usuario = QTableWidgetItem(empleado.get('username', ''))

            item_cargo = QTableWidgetItem(empleado.get('cargo', ''))

            item_turno = QTableWidgetItem(empleado.get('turno', ''))
            item_turno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            for item in (item_codigo, item_dni, item_nombre, item_usuario, item_cargo, item_turno):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

            self.tbl_empleados.setItem(fila_idx, 0, item_codigo)
            self.tbl_empleados.setItem(fila_idx, 1, item_dni)
            self.tbl_empleados.setItem(fila_idx, 2, item_nombre)
            self.tbl_empleados.setItem(fila_idx, 3, item_usuario)
            self.tbl_empleados.setItem(fila_idx, 4, item_cargo)
            self.tbl_empleados.setItem(fila_idx, 5, item_turno)

        if hasattr(self, 'label_2'):
            self.label_2.setText(f"Se muestran los últimos ({len(coleccion_empleados)}) registros")

    def _al_cambiar_seleccion_tabla(self):
        hay_seleccion = len(self.tbl_empleados.selectedItems()) > 0
        self.btn_editar.setEnabled(hay_seleccion)
        self.btn_eliminar.setEnabled(hay_seleccion)

    def _al_hacer_clic_nuevo(self):
        """Abre el modal vacío para registrar un nuevo colaborador."""
        modal_registro = EmpleadoFormDialog(parent=self)
        if modal_registro.exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()

    def _al_hacer_clic_editar(self):
        """Recupera el ID de la fila seleccionada y abre el modal en modo Edición."""
        fila_actual = self.tbl_empleados.currentRow()
        if fila_actual < 0:
            QMessageBox.warning(self, "Selección Requerida", "Seleccione un empleado de la lista para editar.")
            return

        # Rescate del identificador primario almacenado en la memoria de la celda
        celda_codigo = self.tbl_empleados.item(fila_actual, 0)
        if celda_codigo is None:
            QMessageBox.warning(self, "Selección Inválida", "No se encontró el empleado seleccionado.")
            return

        id_usuario = celda_codigo.data(99)

        # Apertura modal inyectando el identificador
        modal_edicion = EmpleadoFormDialog(parent=self, id_usuario_editar=id_usuario)
        if modal_edicion.exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()  # Recarga reactiva de los datos actualizados

    def _al_hacer_clic_eliminar(self):
        pass
