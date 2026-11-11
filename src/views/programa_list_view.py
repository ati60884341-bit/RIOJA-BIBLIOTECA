import os
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView
from PySide6.QtCore import Qt

# 1. Importamos la clase visual generada por pyside6-uic
from views.frm_programa_list_ui import Ui_Form

from controllers.programa_controller import ProgramaController
from exceptions.biblioteca_exceptions import BibliotecaException

class ProgramaListView(QWidget, Ui_Form):
    """Controlador visual del catálogo de Programas de Estudio."""

    def __init__(self, padre=None):
        super().__init__(padre)

        # 2. Inicializamos todos los controles arrastrados en Qt Designer
        self.setupUi(self)

        # 3. Instanciamos nuestro Controlador de Negocio (Cerebro del MVC)
        self._controlador = ProgramaController()

        # 4. Configuración avanzada de la tabla (Ajuste dinámico de columnas)
        self._configurar_cabeceras_tabla()

        # 5. Icono de limpieza nativo 'X' en la caja de búsqueda
        self.txt_buscar.setClearButtonEnabled(True)

        # 6. Conexión de Eventos (Signals & Slots)
        # Búsqueda y filtrado (Sesión 20)
        self.btn_buscar.clicked.connect(self._ejecutar_busqueda)
        self.txt_buscar.returnPressed.connect(self._ejecutar_busqueda)
        self.txt_buscar.textChanged.connect(self._al_cambiar_texto_busqueda)

        # Control de botones CRUD según selección de la grilla
        self.tbl_programas.itemSelectionChanged.connect(self._al_cambiar_seleccion_tabla)

        # Eventos CRUD (Preparación para Sesión 21/22)
        self.btn_nuevo.clicked.connect(self._al_hacer_clic_nuevo)
        self.btn_editar.clicked.connect(self._al_hacer_clic_editar)
        self.btn_eliminar.clicked.connect(self._al_hacer_clic_eliminar)

        # 7. Estado inicial: Deshabilitar botones que requieren tener una fila seleccionada
        self.btn_editar.setEnabled(False)
        self.btn_eliminar.setEnabled(False)

        # 8. Carga inicial de datos desde MySQL al abrir la ventana
        self._cargar_grilla()

    def _configurar_cabeceras_tabla(self):
        """Aplica comportamiento elástico a las columnas para un diseño corporativo."""
        cabecera = self.tbl_programas.horizontalHeader()
        
        # Columna 0 (Código): Se ajusta al tamaño mínimo del texto
        cabecera.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        # Columna 1 (Estado): Se ajusta al tamaño mínimo del texto
        cabecera.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # Columna 2 (Nombre): Se estira elásticamente para ocupar todo el espacio vacío
        cabecera.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        # Columna 3 (Creación): Se ajusta a la fecha
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
        """Si la caja se vacía (por borrar todo o presionar la 'X'), restaura el listado."""
        if not nuevo_texto.strip():
            self._cargar_grilla()

    def _renderizar_datos(self, coleccion_programas):
        """Puebla las celdas de la tabla y oculta el ID original en memoria."""
        # Limpiar filas previas
        self.tbl_programas.setRowCount(0)

        for fila_idx, programa in enumerate(coleccion_programas):
            # Insertar una fila nueva en blanco
            self.tbl_programas.insertRow(fila_idx)

            # COLUMNA 0: Código (Inyectando el ID oculto con setData)
            item_codigo = QTableWidgetItem(programa.codigo_programa)
            item_codigo.setData(99, programa.id_programa)  # Truco de Arquitectura
            item_codigo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # COLUMNA 1: Estado
            item_estado = QTableWidgetItem(programa.estado)
            item_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # COLUMNA 2: Nombre
            item_nombre = QTableWidgetItem(programa.nombre_programa)

            # COLUMNA 3: Creación (Auditoría)
            fecha_str = str(programa.creado_en) if programa.creado_en else "N/A"
            item_creacion = QTableWidgetItem(fecha_str)
            item_creacion.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # Blindaje corporativo: Marcar celdas como SOLO LECTURA
            for item in (item_codigo, item_estado, item_nombre, item_creacion):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

            # Inyectar celdas en el QTableWidget
            self.tbl_programas.setItem(fila_idx, 0, item_codigo)
            self.tbl_programas.setItem(fila_idx, 1, item_estado)
            self.tbl_programas.setItem(fila_idx, 2, item_nombre)
            self.tbl_programas.setItem(fila_idx, 3, item_creacion)

        # Actualizar la etiqueta inferior con el conteo real
        if hasattr(self, 'label_2'):
            self.label_2.setText(f"Se muestran los últimos ({len(coleccion_programas)}) registros")

    def _al_cambiar_seleccion_tabla(self):
        """Habilita o deshabilita botones según si hay una fila seleccionada."""
        hay_seleccion = len(self.tbl_programas.selectedItems()) > 0
        self.btn_editar.setEnabled(hay_seleccion)
        self.btn_eliminar.setEnabled(hay_seleccion)

    def _al_hacer_clic_nuevo(self):
        """(Sesión 21) Abrirá el modal vacío para crear un registro."""
        QMessageBox.information(self, "Desarrollo", "Formulario de Registro (Próxima Sesión)")

    def _al_hacer_clic_editar(self):
        """(Sesión 22) Recupera el ID oculto y abre el modal para editar."""
        fila_actual = self.tbl_programas.currentRow()
        if fila_actual >= 0:
            # Rescatamos el ID que escondimos en la columna 0 (Código)
            id_oculto = self.tbl_programas.item(fila_actual, 0).data(99)
            QMessageBox.information(self, "Desarrollo", f"Se editará el registro con ID BD: {id_oculto}")

    def _al_hacer_clic_eliminar(self):
        """(Sesión 22) Recupera el ID y ejecuta la transacción de borrado."""
        pass