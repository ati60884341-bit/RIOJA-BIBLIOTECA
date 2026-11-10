# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_empleado_list.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(860, 480)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.layout_busqueda = QHBoxLayout()
        self.layout_busqueda.setObjectName(u"layout_busqueda")
        self.txt_buscar = QLineEdit(Form)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.layout_busqueda.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(Form)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.layout_busqueda.addWidget(self.btn_buscar)


        self.verticalLayout.addLayout(self.layout_busqueda)

        self.tbl_empleados = QTableWidget(Form)
        if (self.tbl_empleados.columnCount() < 6):
            self.tbl_empleados.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_empleados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tbl_empleados.setObjectName(u"tbl_empleados")
        self.tbl_empleados.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_empleados.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_empleados.setAlternatingRowColors(True)
        self.tbl_empleados.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tbl_empleados)

        self.layout_inferior = QHBoxLayout()
        self.layout_inferior.setObjectName(u"layout_inferior")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.layout_inferior.addWidget(self.label_2)

        self.espaciador = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_inferior.addItem(self.espaciador)

        self.btn_nuevo = QPushButton(Form)
        self.btn_nuevo.setObjectName(u"btn_nuevo")

        self.layout_inferior.addWidget(self.btn_nuevo)

        self.btn_editar = QPushButton(Form)
        self.btn_editar.setObjectName(u"btn_editar")

        self.layout_inferior.addWidget(self.btn_editar)

        self.btn_eliminar = QPushButton(Form)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.layout_inferior.addWidget(self.btn_eliminar)


        self.verticalLayout.addLayout(self.layout_inferior)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Catálogo de Colaboradores", None))
        self.label.setText(QCoreApplication.translate("Form", u"COLABORADORES", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar por DNI, nombre o usuario...", None))
        self.btn_buscar.setText(QCoreApplication.translate("Form", u"Buscar", None))
        ___qtablewidgetitem = self.tbl_empleados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Código", None))
        ___qtablewidgetitem1 = self.tbl_empleados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"DNI", None))
        ___qtablewidgetitem2 = self.tbl_empleados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nombres y Apellidos", None))
        ___qtablewidgetitem3 = self.tbl_empleados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Usuario", None))
        ___qtablewidgetitem4 = self.tbl_empleados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Cargo", None))
        ___qtablewidgetitem5 = self.tbl_empleados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Turno", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Se muestran los últimos (0) registros", None))
        self.btn_nuevo.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        self.btn_editar.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form", u"Eliminar", None))
    # retranslateUi

