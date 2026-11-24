from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView
# ===== S26 (inicio): imports para Debounce (QTimer) y semáforo visual (QColor, QBrush) =====
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QBrush
# ===== S26 (fin) =====

# 1. Importamos la interfaz precompilada desde Qt Designer
from views.frm_empleado_reporte_ui import Ui_Form

# 2. Importamos los controladores de negocio (Arquitectura MVC + DAO)
from controllers.empleado_controller import EmpleadoController
from controllers.rol_controller import RolController
from exceptions.biblioteca_exceptions import BibliotecaException


class EmpleadoReporteView(QWidget, Ui_Form):
    """
    Vista optimizada de Consultas y Reportes de Personal.
    Implementa patrón Debounce, sincronización tabla-consulta y UX visual.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Instanciamos los controladores
        self._controlador_emp = EmpleadoController()
        self._controlador_rol = RolController()

        # Configuramos comportamiento inicial de la grilla y caja de búsqueda
        self._configurar_cabeceras()
        self.txt_buscar.setClearButtonEnabled(True)

        # ===== S26 (inicio): Debounce, botón Limpiar y conexión tabla -> consulta =====
        # --- OPTIMIZACIÓN 1: Temporizador Debounce (450 ms) ---
        self._timer_busqueda = QTimer(self)
        self._timer_busqueda.setSingleShot(True)
        self._timer_busqueda.timeout.connect(self._aplicar_filtros)

        # --- SINCRONIZACIÓN DINÁMICA INICIAL ---
        self._cargar_combo_roles()

        # --- CONEXIÓN DE EVENTOS DE FILTRADO ---
        self.cbo_rol.currentIndexChanged.connect(self._aplicar_filtros)
        self.cbo_turno.currentIndexChanged.connect(self._aplicar_filtros)
        self.chk_activos.stateChanged.connect(self._aplicar_filtros)
        self.txt_buscar.textChanged.connect(self._al_escribir_busqueda)
        self.btn_limpiar.clicked.connect(self._limpiar_todos_los_filtros)

        # --- CONEXIÓN DE LA TABLA A CONSULTAS DINÁMICAS ---
        self.tbl_reporte.itemSelectionChanged.connect(self._al_seleccionar_fila)
        # ===== S26 (fin) =====

        # Carga inicial de datos
        self._aplicar_filtros()

    def _configurar_cabeceras(self):
        """Ajusta el ancho responsivo de las 7 columnas de la tabla."""
        cabecera = self.tbl_reporte.horizontalHeader()
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Código
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # DNI
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)           # Apellidos y Nombres
        cabecera.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Cargo
        cabecera.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Turno
        cabecera.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Rol
        cabecera.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)  # Estado

    def _cargar_combo_roles(self):
        """Sincroniza dinámicamente el desplegable de roles desde MySQL."""
        try:
            roles = self._controlador_rol.obtener_roles()
            self.cbo_rol.clear()
            self.cbo_rol.addItem("-- Todos los Roles --", 0)
            for r in roles:
                self.cbo_rol.addItem(r.nombre_rol, r.id_rol)
        except BibliotecaException as error:
            QMessageBox.critical(self, "Error de Sincronización", f"No se pudo cargar roles: {error}")

    # ===== S26 (inicio): Debounce y limpieza de filtros con blockSignals =====
    def _al_escribir_busqueda(self):
        """Patrón Debounce: reinicia el reloj en cada pulsación de tecla."""
        self._timer_busqueda.start(450)

    def _limpiar_todos_los_filtros(self):
        """Restablece todos los controles de filtro sin disparar consultas redundantes."""
        self._timer_busqueda.stop()

        # Bloqueamos señales temporalmente para evitar 4 llamadas seguidas a MySQL
        for control in (self.cbo_rol, self.cbo_turno, self.chk_activos, self.txt_buscar):
            control.blockSignals(True)

        self.cbo_rol.setCurrentIndex(0)
        self.cbo_turno.setCurrentIndex(0)
        self.chk_activos.setChecked(False)
        self.txt_buscar.clear()

        for control in (self.cbo_rol, self.cbo_turno, self.chk_activos, self.txt_buscar):
            control.blockSignals(False)

        # Ejecutamos una única consulta limpia
        self._aplicar_filtros()
    # ===== S26 (fin) =====

    def _aplicar_filtros(self):
        """Ejecuta la consulta multinivel contra MySQL y actualiza la grilla."""
        try:
            rol_id = self.cbo_rol.currentData()
            if rol_id is None:
                rol_id = 0

            turno = self.cbo_turno.currentText()
            solo_activos = self.chk_activos.isChecked()
            criterio = self.txt_buscar.text()

            lista_filtrada = self._controlador_emp.filtrar_reporte(
                rol_id, turno, solo_activos, criterio
            )

            self._renderizar_tabla(lista_filtrada)
            # ===== S26 (inicio): contador de resultados =====
            self._actualizar_feedback_ux(len(lista_filtrada))
        except BibliotecaException as ex:
            self.lbl_contador.setText(f"Error al consultar datos: {ex}")
            # ===== S26 (fin) =====

    # ===== S26 (inicio): ordenamiento seguro, ID oculto, semáforo visual, contador y ficha rápida =====
    def _renderizar_tabla(self, lista):
        """Puebla la grilla aplicando ordenamiento seguro y semáforo visual UX."""
        # IMPORTANTE: Desactivar ordenamiento antes de insertar filas para evitar desalineación
        self.tbl_reporte.setSortingEnabled(False)
        self.tbl_reporte.setRowCount(0)

        for fila_idx, emp in enumerate(lista):
            self.tbl_reporte.insertRow(fila_idx)

            # Guardamos el ID oculto en la celda 0 para consultas dinámicas al seleccionar
            item_cod = QTableWidgetItem(emp['codigo_empleado'])
            item_cod.setData(99, emp['id_usuario'])
            item_cod.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_dni = QTableWidgetItem(emp['numero_documento'])
            item_dni.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_nom = QTableWidgetItem(emp['nombre_completo'])
            item_cargo = QTableWidgetItem(emp['cargo'])

            item_turno = QTableWidgetItem(emp['turno'])
            item_turno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_rol = QTableWidgetItem(emp['rol'])
            item_rol.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            item_estado = QTableWidgetItem(emp['estado'])
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            es_inactivo = (emp['estado'] == 'Inactivo')
            celdas = (item_cod, item_dni, item_nom, item_cargo, item_turno, item_rol, item_estado)

            for col_idx, item in enumerate(celdas):
                # UX Defensiva: celdas de solo lectura
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                # Semáforo Visual UX
                if es_inactivo:
                    item.setForeground(QBrush(QColor(140, 140, 140)))
                    fuente = item.font()
                    fuente.setItalic(True)
                    item.setFont(fuente)
                elif col_idx == 6:
                    item.setForeground(QBrush(QColor(0, 128, 0)))

                self.tbl_reporte.setItem(fila_idx, col_idx, item)

        # Reactivamos el ordenamiento interactivo por clic en cabeceras
        self.tbl_reporte.setSortingEnabled(True)

    def _actualizar_feedback_ux(self, total: int):
        """Informa al usuario el resultado de su consulta de manera clara."""
        if total == 0:
            self.lbl_contador.setText("No se encontraron colaboradores con los filtros aplicados.")
            self.lbl_detalle_empleado.setText("Sin selección activa.")
        elif total == 1:
            self.lbl_contador.setText("Mostrando 1 colaborador encontrado.")
        else:
            self.lbl_contador.setText(f"Mostrando {total} colaboradores encontrados.")

    def _al_seleccionar_fila(self):
        """
        Conexión dinámica tabla -> base de datos:
        Al seleccionar una fila, consulta los datos completos del colaborador por su ID.
        """
        fila = self.tbl_reporte.currentRow()
        if fila < 0:
            return

        item_codigo = self.tbl_reporte.item(fila, 0)
        if not item_codigo:
            return

        id_usuario = item_codigo.data(99)
        try:
            datos = self._controlador_emp.obtener_empleado_por_id(id_usuario)
            self.lbl_detalle_empleado.setText(
                f"Colaborador: {datos['apellidos']}, {datos['nombres']}   |   "
                f"Usuario de Acceso: {datos['username']}   |   "
                f"Cargo: {datos['cargo']} ({datos['turno']})"
            )
        except BibliotecaException as error:
            self.lbl_detalle_empleado.setText(f"No se pudo cargar el detalle: {error}")
    # ===== S26 (fin) =====
