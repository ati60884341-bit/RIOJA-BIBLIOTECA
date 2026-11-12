from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QAbstractItemView, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout

class Ui_FormRolList(object):
    def setupUi(self, FormRolList):
        if not FormRolList.objectName():
            FormRolList.setObjectName(u"FormRolList")
        FormRolList.resize(720, 480)
        self.verticalLayout = QVBoxLayout(FormRolList)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.lbl_buscar = QLabel(FormRolList)
        self.lbl_buscar.setObjectName(u"lbl_buscar")
        font = QFont()
        font.setBold(True)
        self.lbl_buscar.setFont(font)

        self.verticalLayout.addWidget(self.lbl_buscar)

        self.layout_busqueda = QHBoxLayout()
        self.layout_busqueda.setObjectName(u"layout_busqueda")
        self.txt_buscar = QLineEdit(FormRolList)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.layout_busqueda.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(FormRolList)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.layout_busqueda.addWidget(self.btn_buscar)


        self.verticalLayout.addLayout(self.layout_busqueda)

        self.layout_acciones = QHBoxLayout()
        self.layout_acciones.setObjectName(u"layout_acciones")
        self.btn_nuevo = QPushButton(FormRolList)
        self.btn_nuevo.setObjectName(u"btn_nuevo")

        self.layout_acciones.addWidget(self.btn_nuevo)

        self.btn_editar = QPushButton(FormRolList)
        self.btn_editar.setObjectName(u"btn_editar")

        self.layout_acciones.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(FormRolList)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.layout_acciones.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.layout_acciones)

        self.tbl_roles = QTableWidget(FormRolList)
        if (self.tbl_roles.columnCount() < 4):
            self.tbl_roles.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_roles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_roles.setObjectName(u"tbl_roles")
        self.tbl_roles.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_roles.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tbl_roles)

        self.label_conteo = QLabel(FormRolList)
        self.label_conteo.setObjectName(u"label_conteo")

        self.verticalLayout.addWidget(self.label_conteo)


        self.retranslateUi(FormRolList)

        QMetaObject.connectSlotsByName(FormRolList)

    def retranslateUi(self, FormRolList):
        FormRolList.setWindowTitle(QCoreApplication.translate("FormRolList", u"Cat\u00e1logo de Roles", None))
        self.lbl_buscar.setText(QCoreApplication.translate("FormRolList", u"Buscar Por Nombre o Descripci\u00f3n del Rol", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("FormRolList", u"Ingrese el nombre o la descripci\u00f3n del rol...", None))
        self.btn_buscar.setText(QCoreApplication.translate("FormRolList", u"Buscar Rol", None))
        self.btn_nuevo.setText(QCoreApplication.translate("FormRolList", u"Nuevo Rol", None))
        self.btn_editar.setText(QCoreApplication.translate("FormRolList", u"Editar Rol", None))
        self.btn_eliminar.setText(QCoreApplication.translate("FormRolList", u"Eliminar Rol", None))
        ___qtablewidgetitem = self.tbl_roles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormRolList", u"ID", None))
        ___qtablewidgetitem1 = self.tbl_roles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormRolList", u"Nombre del Rol", None))
        ___qtablewidgetitem2 = self.tbl_roles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormRolList", u"Descripci\u00f3n", None))
        ___qtablewidgetitem3 = self.tbl_roles.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormRolList", u"Usuarios Asignados", None))
        self.label_conteo.setText(QCoreApplication.translate("FormRolList", u"Se muestran (0) roles registrados", None))

