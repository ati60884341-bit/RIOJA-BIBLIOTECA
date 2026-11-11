from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView, QDialog
from PySide6.QtCore import Qt

from views.frm_rol_list_ui import Ui_FormRolList
from views.rol_form_dialog import RolFormDialog
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import BibliotecaException


class RolListView(QWidget, Ui_FormRolList):
    """Vista del catálogo de Roles (Capa Vista del MVC)."""

    ROL_ID = Qt.ItemDataRole.UserRole

    def __init__(self, padre=None):
        super().__init__(padre)
        self.setupUi(self)

        self._controlador = RolController()

        self._configurar_tabla()
        self.txt_buscar.setClearButtonEnabled(True)

        self.btn_buscar.clicked.connect(self._cargar_grilla)
        self.txt_buscar.returnPressed.connect(self._cargar_grilla)
        self.txt_buscar.textChanged.connect(self._al_cambiar_texto_busqueda)

        self.tbl_roles.itemSelectionChanged.connect(self._al_cambiar_seleccion_tabla)
        self.tbl_roles.cellDoubleClicked.connect(lambda *_: self._al_hacer_clic_editar())

        self.btn_nuevo.clicked.connect(self._al_hacer_clic_nuevo)
        self.btn_editar.clicked.connect(self._al_hacer_clic_editar)
        self.btn_eliminar.clicked.connect(self._al_hacer_clic_eliminar)

        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)

        self._cargar_grilla()

    def _configurar_tabla(self):
        self.tbl_roles.verticalHeader().setVisible(False)
        self.tbl_roles.setAlternatingRowColors(True)
        cabecera = self.tbl_roles.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

    def _cargar_grilla(self):
        try:
            roles = self._controlador.buscar_roles(self.txt_buscar.text())
            self._renderizar_datos(roles)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Conexión", str(error))

    def _al_cambiar_texto_busqueda(self, nuevo_texto: str):
        if not nuevo_texto.strip():
            self._cargar_grilla()

    def _renderizar_datos(self, roles):
        self.tbl_roles.setRowCount(0)
        for fila, rol in enumerate(roles):
            self.tbl_roles.insertRow(fila)

            item_id = QTableWidgetItem(str(rol.id_rol))
            item_id.setData(self.ROL_ID, rol.id_rol)
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nombre = QTableWidgetItem(rol.nombre_rol)
            item_desc = QTableWidgetItem(rol.descripcion)

            item_total = QTableWidgetItem(str(rol.total_usuarios))
            item_total.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            for col, item in enumerate((item_id, item_nombre, item_desc, item_total)):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tbl_roles.setItem(fila, col, item)

        self.label_conteo.setText(f"Se muestran ({len(roles)}) roles registrados")
        self._al_cambiar_seleccion_tabla()

    def _id_rol_seleccionado(self):
        fila = self.tbl_roles.currentRow()
        if fila < 0 or not self.tbl_roles.selectedItems():
            return None
        celda = self.tbl_roles.item(fila, 0)
        return celda.data(self.ROL_ID) if celda else None

    def _al_cambiar_seleccion_tabla(self):
        hay_seleccion = len(self.tbl_roles.selectedItems()) > 0
        self.btn_editar.setEnabled(hay_seleccion)
        self.btn_eliminar.setEnabled(hay_seleccion)

    def _al_hacer_clic_nuevo(self):
        if RolFormDialog(parent=self).exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()

    def _al_hacer_clic_editar(self):
        id_rol = self._id_rol_seleccionado()
        if id_rol is None:
            QMessageBox.warning(self, "Selección Requerida", "Seleccione un rol de la lista para editar.")
            return
        if RolFormDialog(parent=self, id_rol_editar=id_rol).exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()

    def _al_hacer_clic_eliminar(self):
        id_rol = self._id_rol_seleccionado()
        if id_rol is None:
            QMessageBox.warning(self, "Selección Requerida", "Seleccione un rol de la lista para eliminar.")
            return

        nombre = self.tbl_roles.item(self.tbl_roles.currentRow(), 1).text()
        respuesta = QMessageBox.question(
            self, "Confirmar Eliminación",
            f"¿Está seguro de eliminar el rol '{nombre}'?\nEsta acción no se puede deshacer.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return

        try:
            self._controlador.eliminar_rol(id_rol)
            QMessageBox.information(self, "Eliminación Exitosa", f"El rol '{nombre}' fue eliminado.")
            self._cargar_grilla()
        except BibliotecaException as error:
            QMessageBox.warning(self, "No se pudo eliminar", str(error))
