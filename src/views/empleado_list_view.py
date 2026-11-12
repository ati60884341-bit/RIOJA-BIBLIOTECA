from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView, QDialog
from PySide6.QtCore import Qt

from views.frm_empleado_list_ui import Ui_Form
from views.empleado_form_dialog import EmpleadoFormDialog
from controllers.empleado_controller import EmpleadoController
from exceptions.biblioteca_exceptions import BibliotecaException, ValidacionDatosError


class EmpleadoListView(QWidget, Ui_Form):
    """Vista del catálogo de Colaboradores (Capa Vista del MVC)."""

    def __init__(self, padre=None):
        super().__init__(padre)
        self.setupUi(self)

        self._controlador = EmpleadoController()
        self._configurar_cabeceras_tabla()
        self.txt_buscar.setClearButtonEnabled(True)

        # Conexiones para el buscador reactivo
        self.btn_buscar.clicked.connect(self._cargar_grilla)
        self.txt_buscar.returnPressed.connect(self._cargar_grilla)
        self.txt_buscar.textChanged.connect(self._al_cambiar_texto_busqueda)

        # Botones de mantenimiento (Acciones 2, 4 y 5)
        self.btn_nuevo.clicked.connect(self._al_hacer_clic_nuevo)
        self.btn_editar.clicked.connect(self._al_hacer_clic_editar)
        self.btn_eliminar.clicked.connect(self._al_hacer_clic_eliminar)

        # Cargar los datos nada más al abrir la ventana
        self._cargar_grilla()

    def _configurar_cabeceras_tabla(self):
        cabecera = self.tbl_empleados.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        cabecera.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        cabecera.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)

    # ---------------------------------------------------------------
    # Acción 1: Mostrar la grilla y buscar
    # ---------------------------------------------------------------
    def _cargar_grilla(self):
        try:
            criterio = self.txt_buscar.text()
            lista = self._controlador.listar_empleados(criterio)
            self._renderizar_tabla(lista)
        except BibliotecaException as ex:
            QMessageBox.critical(self, "Error", str(ex))

    def _al_cambiar_texto_busqueda(self, texto: str):
        # Si el usuario borra todo el texto, vuelve a cargar la tabla completa
        if not texto.strip():
            self._cargar_grilla()

    def _renderizar_tabla(self, lista):
        self.tbl_empleados.setRowCount(0)
        for fila_idx, emp in enumerate(lista):
            self.tbl_empleados.insertRow(fila_idx)

            # ¡Magia Arquitectónica!: Ocultamos el ID real en la memoria de la celda
            item_cod = QTableWidgetItem(emp['codigo_empleado'])
            item_cod.setData(99, emp['id_usuario'])
            item_cod.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_dni = QTableWidgetItem(emp['numero_documento'])
            item_nom = QTableWidgetItem(emp['nombre_completo'])
            item_cargo = QTableWidgetItem(emp['cargo'])
            item_turno = QTableWidgetItem(emp['turno'])
            item_rol = QTableWidgetItem(emp['rol'])
            item_estado = QTableWidgetItem(emp['estado'])
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Proteger celdas contra escritura manual
            for item in (item_cod, item_dni, item_nom, item_cargo, item_turno, item_rol, item_estado):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

            self.tbl_empleados.setItem(fila_idx, 0, item_cod)
            self.tbl_empleados.setItem(fila_idx, 1, item_dni)
            self.tbl_empleados.setItem(fila_idx, 2, item_nom)
            self.tbl_empleados.setItem(fila_idx, 3, item_cargo)
            self.tbl_empleados.setItem(fila_idx, 4, item_turno)
            self.tbl_empleados.setItem(fila_idx, 5, item_rol)
            self.tbl_empleados.setItem(fila_idx, 6, item_estado)

        self.label_conteo.setText(f"Se muestran los últimos ({len(lista)}) registros (Top 20)")

    # ---------------------------------------------------------------
    # Acción 2: Nuevo Empleado
    # ---------------------------------------------------------------
    def _al_hacer_clic_nuevo(self):
        modal = EmpleadoFormDialog(parent=self)
        if modal.exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla() # Si se guarda con éxito, recarga la tabla

    # ---------------------------------------------------------------
    # Acción 4: Editar (Principio DRY)
    # ---------------------------------------------------------------
    def _al_hacer_clic_editar(self):
        """Recupera el ID de la fila seleccionada y abre el modal en modo Edición."""
        fila_actual = self.tbl_empleados.currentRow()
        if fila_actual < 0:
            QMessageBox.warning(self, "Selección Requerida", "Seleccione un empleado de la lista para editar.")
            return

        # Rescate del identificador primario almacenado en la memoria de la celda
        celda_codigo = self.tbl_empleados.item(fila_actual, 0)
        id_usuario = celda_codigo.data(99)

        # Apertura modal inyectando el identificador
        modal_edicion = EmpleadoFormDialog(parent=self, id_usuario_editar=id_usuario)
        if modal_edicion.exec() == QDialog.DialogCode.Accepted:
            self._cargar_grilla()  # Recarga reactiva de los datos actualizados

    # ---------------------------------------------------------------
    # Acción 5: Eliminar (UX defensiva)
    # ---------------------------------------------------------------
    def _al_hacer_clic_eliminar(self):
        fila = self.tbl_empleados.currentRow()
        if fila < 0:
            return

        id_oculto = self.tbl_empleados.item(fila, 0).data(99)
        nombre_empleado = self.tbl_empleados.item(fila, 2).text()

        # UX Defensiva: Confirmación explícita con botón por defecto en 'No'
        respuesta = QMessageBox.question(
            self,
            "Confirmar Baja de Personal",
            f"¿Está seguro de dar de baja (borrado lógico) al colaborador:\n\n{nombre_empleado}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            try:
                # Aplicamos el estándar corporativo: Borrado Lógico (logico=True)
                self._controlador.eliminar_empleado(id_oculto, logico=True)
                QMessageBox.information(self, "Baja Confirmada", "El colaborador ha sido desactivado del sistema.")
                self._cargar_grilla()
            except ValidacionDatosError as adv:
                QMessageBox.warning(self, "Operación No Permitida", str(adv))
            except BibliotecaException as err:
                QMessageBox.critical(self, "Error de Integridad", str(err))
