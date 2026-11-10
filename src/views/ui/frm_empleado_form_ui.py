# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_empleado_form.ui'
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
from PySide6.QtWidgets import (QComboBox, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_EmpleadoFormDialog(object):
    def setupUi(self, EmpleadoFormDialog):
        if not EmpleadoFormDialog.objectName():
            EmpleadoFormDialog.setObjectName(u"EmpleadoFormDialog")
        EmpleadoFormDialog.resize(420, 420)
        self.verticalLayout = QVBoxLayout(EmpleadoFormDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_numero_documento = QLabel(EmpleadoFormDialog)
        self.lbl_numero_documento.setObjectName(u"lbl_numero_documento")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_numero_documento)

        self.txt_numero_documento = QLineEdit(EmpleadoFormDialog)
        self.txt_numero_documento.setObjectName(u"txt_numero_documento")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_numero_documento)

        self.lbl_nombres = QLabel(EmpleadoFormDialog)
        self.lbl_nombres.setObjectName(u"lbl_nombres")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_nombres)

        self.txt_nombres = QLineEdit(EmpleadoFormDialog)
        self.txt_nombres.setObjectName(u"txt_nombres")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_nombres)

        self.lbl_apellidos = QLabel(EmpleadoFormDialog)
        self.lbl_apellidos.setObjectName(u"lbl_apellidos")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_apellidos)

        self.txt_apellidos = QLineEdit(EmpleadoFormDialog)
        self.txt_apellidos.setObjectName(u"txt_apellidos")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txt_apellidos)

        self.lbl_username = QLabel(EmpleadoFormDialog)
        self.lbl_username.setObjectName(u"lbl_username")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_username)

        self.txt_username = QLineEdit(EmpleadoFormDialog)
        self.txt_username.setObjectName(u"txt_username")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txt_username)

        self.lbl_password = QLabel(EmpleadoFormDialog)
        self.lbl_password.setObjectName(u"lbl_password")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_password)

        self.txt_password = QLineEdit(EmpleadoFormDialog)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txt_password)

        self.lbl_codigo_empleado = QLabel(EmpleadoFormDialog)
        self.lbl_codigo_empleado.setObjectName(u"lbl_codigo_empleado")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_codigo_empleado)

        self.txt_codigo_empleado = QLineEdit(EmpleadoFormDialog)
        self.txt_codigo_empleado.setObjectName(u"txt_codigo_empleado")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txt_codigo_empleado)

        self.lbl_cargo = QLabel(EmpleadoFormDialog)
        self.lbl_cargo.setObjectName(u"lbl_cargo")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lbl_cargo)

        self.txt_cargo = QLineEdit(EmpleadoFormDialog)
        self.txt_cargo.setObjectName(u"txt_cargo")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.txt_cargo)

        self.lbl_turno = QLabel(EmpleadoFormDialog)
        self.lbl_turno.setObjectName(u"lbl_turno")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lbl_turno)

        self.cbo_turno = QComboBox(EmpleadoFormDialog)
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.setObjectName(u"cbo_turno")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cbo_turno)

        self.lbl_rol = QLabel(EmpleadoFormDialog)
        self.lbl_rol.setObjectName(u"lbl_rol")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lbl_rol)

        self.cbo_rol = QComboBox(EmpleadoFormDialog)
        self.cbo_rol.setObjectName(u"cbo_rol")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.cbo_rol)


        self.verticalLayout.addLayout(self.formLayout)

        self.layout_botones = QHBoxLayout()
        self.layout_botones.setObjectName(u"layout_botones")
        self.espaciador = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_botones.addItem(self.espaciador)

        self.btn_cancelar = QPushButton(EmpleadoFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.layout_botones.addWidget(self.btn_cancelar)

        self.btn_guardar = QPushButton(EmpleadoFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.layout_botones.addWidget(self.btn_guardar)


        self.verticalLayout.addLayout(self.layout_botones)


        self.retranslateUi(EmpleadoFormDialog)

        QMetaObject.connectSlotsByName(EmpleadoFormDialog)
    # setupUi

    def retranslateUi(self, EmpleadoFormDialog):
        EmpleadoFormDialog.setWindowTitle(QCoreApplication.translate("EmpleadoFormDialog", u"Gestión de Personal", None))
        self.lbl_numero_documento.setText(QCoreApplication.translate("EmpleadoFormDialog", u"DNI:", None))
        self.lbl_nombres.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Nombres:", None))
        self.lbl_apellidos.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Apellidos:", None))
        self.lbl_username.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Usuario:", None))
        self.lbl_password.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Contraseña:", None))
        self.lbl_codigo_empleado.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Código:", None))
        self.lbl_cargo.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Cargo:", None))
        self.lbl_turno.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Turno:", None))
        self.cbo_turno.setItemText(0, QCoreApplication.translate("EmpleadoFormDialog", u"Mañana", None))
        self.cbo_turno.setItemText(1, QCoreApplication.translate("EmpleadoFormDialog", u"Tarde", None))
        self.cbo_turno.setItemText(2, QCoreApplication.translate("EmpleadoFormDialog", u"Noche", None))

        self.lbl_rol.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Rol:", None))
        self.btn_cancelar.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Cancelar", None))
        self.btn_guardar.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Registrar Empleado", None))
    # retranslateUi

