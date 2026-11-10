from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView
from PySide6.QtCore import Qt

from views.ui.frm_programa_list_ui import Ui_Form
from controllers.programa_controller import ProgramaController
from exceptions.biblioteca_exceptions import BibliotecaException


class ProgramaListView(QWidget, Ui_Form):
    """Vista del catálogo de Programas de Estudio (Capa Vista del MVC)."""

    def __init__(self, padre=None):
        super().__init__(padre)
        self.setupUi(self)

        self._controlador = ProgramaController()

        self._configurar_cabeceras_tabla()
        self.txt_buscar.setClearButtonEnabled(True)

        self.btn_buscar.clicked.connect(self._ejecutar_busqueda)
        self.txt_buscar.returnPressed.connect(self._ejecutar_busqueda)
        self.txt_buscar.textChanged.connect(self._al_cambiar_texto_busqueda)

        self.tbl_programas.itemSelectionChanged.connect(self._al_cambiar_seleccion_tabla)

        self.btn_nuevo.clicked.connect(self._al_hacer_clic_nuevo)
        self.btn_editar.clicked.connect(self._al_hacer_clic_editar)
        self.btn_eliminar.clicked.connect(self._al_hacer_clic_eliminar)

        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)

        self._cargar_grilla()

    def _configurar_cabeceras_tabla(self):
        """Aplica el modo de ajuste elastico a las columnas de la grilla."""
        cabecera = self.tbl_programas.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

    def _cargar_grilla(self):
        """Solicita el listado completo al controlador y renderiza la tabla."""
        try:
            lista_programas = self._controlador.obtener_todos()
            self._renderizar_datos(lista_programas)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Conexión", str(error))

    def _ejecutar_busqueda(self):
        """Dispara la búsqueda parametrizada enviando el texto al controlador."""
        criterio = self.txt_buscar.text()
        try:
            lista_filtrada = self._controlador.buscar_programas(criterio)
            self._renderizar_datos(lista_filtrada)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Búsqueda", str(error))

    def _al_cambiar_texto_busqueda(self, nuevo_texto: str):
        """Si la caja se vacía, restaura el listado completo."""
        if not nuevo_texto.strip():
            self._cargar_grilla()

    def _renderizar_datos(self, coleccion_programas):
        """Puebla las celdas de la tabla y oculta el ID original en memoria."""
        self.tbl_programas.setRowCount(0)

        for fila_idx, programa in enumerate(coleccion_programas):
            self.tbl_programas.insertRow(fila_idx)

            item_codigo = QTableWidgetItem(programa.codigo_programa)
            item_codigo.setData(99, programa.id_programa)
            item_codigo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_estado = QTableWidgetItem(programa.estado)
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nombre = QTableWidgetItem(programa.nombre_programa)

            fecha_str = str(programa.creado_en) if programa.creado_en else "N/A"
            item_creacion = QTableWidgetItem(fecha_str)
            item_creacion.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            for item in (item_codigo, item_estado, item_nombre, item_creacion):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

            self.tbl_programas.setItem(fila_idx, 0, item_codigo)
            self.tbl_programas.setItem(fila_idx, 1, item_estado)
            self.tbl_programas.setItem(fila_idx, 2, item_nombre)
            self.tbl_programas.setItem(fila_idx, 3, item_creacion)

        self.label_2.setText(f"Se muestran los últimos ({len(coleccion_programas)}) registros")

    def _al_cambiar_seleccion_tabla(self):
        """Habilita o deshabilita los botones según si hay una fila seleccionada."""
        hay_seleccion = len(self.tbl_programas.selectedItems()) > 0
        self.btn_editar.setEnabled(hay_seleccion)
        self.btn_eliminar.setEnabled(hay_seleccion)

    def _al_hacer_clic_nuevo(self):
        QMessageBox.information(self, "Desarrollo", "Formulario de Registro (próxima sesión)")

    def _al_hacer_clic_editar(self):
        fila_actual = self.tbl_programas.currentRow()
        if fila_actual >= 0:
            id_oculto = self.tbl_programas.item(fila_actual, 0).data(99)
            QMessageBox.information(self, "Desarrollo", f"Se editará el registro con ID BD: {id_oculto}")

    def _al_hacer_clic_eliminar(self):
        pass
