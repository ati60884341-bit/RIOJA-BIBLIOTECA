# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_empleado_reporte.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 520)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(Form)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_titulo.setFont(font)

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.grp_filtros = QGroupBox(Form)
        self.grp_filtros.setObjectName(u"grp_filtros")
        self.horizontalLayout = QHBoxLayout(self.grp_filtros)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_rol = QLabel(self.grp_filtros)
        self.lbl_rol.setObjectName(u"lbl_rol")

        self.horizontalLayout.addWidget(self.lbl_rol)

        self.cbo_rol = QComboBox(self.grp_filtros)
        self.cbo_rol.setObjectName(u"cbo_rol")
        self.cbo_rol.setMinimumSize(QSize(170, 0))

        self.horizontalLayout.addWidget(self.cbo_rol)

        self.lbl_turno = QLabel(self.grp_filtros)
        self.lbl_turno.setObjectName(u"lbl_turno")

        self.horizontalLayout.addWidget(self.lbl_turno)

        self.cbo_turno = QComboBox(self.grp_filtros)
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.setObjectName(u"cbo_turno")

        self.horizontalLayout.addWidget(self.cbo_turno)

        self.chk_activos = QCheckBox(self.grp_filtros)
        self.chk_activos.setObjectName(u"chk_activos")

        self.horizontalLayout.addWidget(self.chk_activos)

        self.txt_buscar = QLineEdit(self.grp_filtros)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.horizontalLayout.addWidget(self.txt_buscar)

        self.btn_limpiar = QPushButton(self.grp_filtros)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout.addWidget(self.btn_limpiar)


        self.verticalLayout.addWidget(self.grp_filtros)

        self.tbl_reporte = QTableWidget(Form)
        if (self.tbl_reporte.columnCount() < 7):
            self.tbl_reporte.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_reporte.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tbl_reporte.setObjectName(u"tbl_reporte")
        self.tbl_reporte.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_reporte.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayout.addWidget(self.tbl_reporte)

        self.lbl_contador = QLabel(Form)
        self.lbl_contador.setObjectName(u"lbl_contador")

        self.verticalLayout.addWidget(self.lbl_contador)

        self.grp_detalle = QGroupBox(Form)
        self.grp_detalle.setObjectName(u"grp_detalle")
        self.layout_detalle = QVBoxLayout(self.grp_detalle)
        self.layout_detalle.setObjectName(u"layout_detalle")
        self.lbl_detalle_empleado = QLabel(self.grp_detalle)
        self.lbl_detalle_empleado.setObjectName(u"lbl_detalle_empleado")
        self.lbl_detalle_empleado.setWordWrap(True)

        self.layout_detalle.addWidget(self.lbl_detalle_empleado)


        self.verticalLayout.addWidget(self.grp_detalle)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Consulta de Personal", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"Consulta y Reporte de Personal", None))
        self.grp_filtros.setTitle(QCoreApplication.translate("Form", u"Filtros", None))
        self.lbl_rol.setText(QCoreApplication.translate("Form", u"Rol:", None))
        self.lbl_turno.setText(QCoreApplication.translate("Form", u"Turno:", None))
        self.cbo_turno.setItemText(0, QCoreApplication.translate("Form", u"TODOS", None))
        self.cbo_turno.setItemText(1, QCoreApplication.translate("Form", u"Ma\u00f1ana", None))
        self.cbo_turno.setItemText(2, QCoreApplication.translate("Form", u"Tarde", None))
        self.cbo_turno.setItemText(3, QCoreApplication.translate("Form", u"Noche", None))

        self.chk_activos.setText(QCoreApplication.translate("Form", u"Mostrar solo personal activo", None))
        self.txt_buscar.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar por DNI o Apellidos...", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Form", u"Limpiar Filtros", None))
        ___qtablewidgetitem = self.tbl_reporte.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        ___qtablewidgetitem1 = self.tbl_reporte.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"DNI", None))
        ___qtablewidgetitem2 = self.tbl_reporte.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Apellidos y Nombres", None))
        ___qtablewidgetitem3 = self.tbl_reporte.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Cargo", None))
        ___qtablewidgetitem4 = self.tbl_reporte.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Turno", None))
        ___qtablewidgetitem5 = self.tbl_reporte.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Rol", None))
        ___qtablewidgetitem6 = self.tbl_reporte.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Estado", None))
        self.lbl_contador.setText(QCoreApplication.translate("Form", u"Mostrando 0 registros", None))
        self.grp_detalle.setTitle(QCoreApplication.translate("Form", u"Ficha R\u00e1pida del Colaborador Seleccionado", None))
        self.lbl_detalle_empleado.setText(QCoreApplication.translate("Form", u"Seleccione un registro de la tabla para ver su cuenta de acceso y detalles...", None))
    # retranslateUi

