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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_EmpleadoFormDialog(object):
    def setupUi(self, EmpleadoFormDialog):
        if not EmpleadoFormDialog.objectName():
            EmpleadoFormDialog.setObjectName(u"EmpleadoFormDialog")
        EmpleadoFormDialog.resize(520, 560)
        self.verticalLayout = QVBoxLayout(EmpleadoFormDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.grp_usuario = QGroupBox(EmpleadoFormDialog)
        self.grp_usuario.setObjectName(u"grp_usuario")
        self.form_usuario = QFormLayout(self.grp_usuario)
        self.form_usuario.setObjectName(u"form_usuario")
        self.form_usuario.setVerticalSpacing(8)
        self.lbl_dni = QLabel(self.grp_usuario)
        self.lbl_dni.setObjectName(u"lbl_dni")

        self.form_usuario.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_dni)

        self.txt_numero_documento = QLineEdit(self.grp_usuario)
        self.txt_numero_documento.setObjectName(u"txt_numero_documento")

        self.form_usuario.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_numero_documento)

        self.lbl_nombres = QLabel(self.grp_usuario)
        self.lbl_nombres.setObjectName(u"lbl_nombres")

        self.form_usuario.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_nombres)

        self.txt_nombres = QLineEdit(self.grp_usuario)
        self.txt_nombres.setObjectName(u"txt_nombres")

        self.form_usuario.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_nombres)

        self.lbl_apellidos = QLabel(self.grp_usuario)
        self.lbl_apellidos.setObjectName(u"lbl_apellidos")

        self.form_usuario.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_apellidos)

        self.txt_apellidos = QLineEdit(self.grp_usuario)
        self.txt_apellidos.setObjectName(u"txt_apellidos")

        self.form_usuario.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txt_apellidos)

        self.lbl_user = QLabel(self.grp_usuario)
        self.lbl_user.setObjectName(u"lbl_user")

        self.form_usuario.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_user)

        self.txt_username = QLineEdit(self.grp_usuario)
        self.txt_username.setObjectName(u"txt_username")

        self.form_usuario.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txt_username)

        self.lbl_pwd = QLabel(self.grp_usuario)
        self.lbl_pwd.setObjectName(u"lbl_pwd")

        self.form_usuario.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_pwd)

        self.txt_password = QLineEdit(self.grp_usuario)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.form_usuario.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txt_password)

        self.lbl_rol = QLabel(self.grp_usuario)
        self.lbl_rol.setObjectName(u"lbl_rol")

        self.form_usuario.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_rol)

        self.cbo_rol = QComboBox(self.grp_usuario)
        self.cbo_rol.setObjectName(u"cbo_rol")

        self.form_usuario.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cbo_rol)


        self.verticalLayout.addWidget(self.grp_usuario)

        self.grp_empleado = QGroupBox(EmpleadoFormDialog)
        self.grp_empleado.setObjectName(u"grp_empleado")
        self.form_empleado = QFormLayout(self.grp_empleado)
        self.form_empleado.setObjectName(u"form_empleado")
        self.form_empleado.setVerticalSpacing(8)
        self.lbl_cod_emp = QLabel(self.grp_empleado)
        self.lbl_cod_emp.setObjectName(u"lbl_cod_emp")

        self.form_empleado.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_cod_emp)

        self.txt_codigo_empleado = QLineEdit(self.grp_empleado)
        self.txt_codigo_empleado.setObjectName(u"txt_codigo_empleado")

        self.form_empleado.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_codigo_empleado)

        self.lbl_cargo = QLabel(self.grp_empleado)
        self.lbl_cargo.setObjectName(u"lbl_cargo")

        self.form_empleado.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_cargo)

        self.txt_cargo = QLineEdit(self.grp_empleado)
        self.txt_cargo.setObjectName(u"txt_cargo")

        self.form_empleado.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_cargo)

        self.lbl_turno = QLabel(self.grp_empleado)
        self.lbl_turno.setObjectName(u"lbl_turno")

        self.form_empleado.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_turno)

        self.cbo_turno = QComboBox(self.grp_empleado)
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.addItem("")
        self.cbo_turno.setObjectName(u"cbo_turno")

        self.form_empleado.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cbo_turno)


        self.verticalLayout.addWidget(self.grp_empleado)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.layout_botones = QHBoxLayout()
        self.layout_botones.setObjectName(u"layout_botones")
        self.btn_guardar = QPushButton(EmpleadoFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.layout_botones.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(EmpleadoFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.layout_botones.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.layout_botones)


        self.retranslateUi(EmpleadoFormDialog)

        QMetaObject.connectSlotsByName(EmpleadoFormDialog)
    # setupUi

    def retranslateUi(self, EmpleadoFormDialog):
        EmpleadoFormDialog.setWindowTitle(QCoreApplication.translate("EmpleadoFormDialog", u"Gesti\u00f3n de Personal - Registro Oficial", None))
        self.grp_usuario.setTitle(QCoreApplication.translate("EmpleadoFormDialog", u"Datos de Identidad y Acceso (Usuario)", None))
        self.lbl_dni.setText(QCoreApplication.translate("EmpleadoFormDialog", u"N\u00b0 Documento (DNI):", None))
        self.txt_numero_documento.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"8 d\u00edgitos num\u00e9ricos", None))
        self.lbl_nombres.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Nombres:", None))
        self.txt_nombres.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"Nombres del colaborador", None))
        self.lbl_apellidos.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Apellidos:", None))
        self.txt_apellidos.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"Apellidos paterno y materno", None))
        self.lbl_user.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Usuario / Correo:", None))
        self.txt_username.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"usuario@sistema.com", None))
        self.lbl_pwd.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Contrase\u00f1a:", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"M\u00ednimo 6 caracteres", None))
        self.lbl_rol.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Rol en Sistema:", None))
        self.grp_empleado.setTitle(QCoreApplication.translate("EmpleadoFormDialog", u"Datos Laborales e Institucionales (Empleado)", None))
        self.lbl_cod_emp.setText(QCoreApplication.translate("EmpleadoFormDialog", u"C\u00f3digo Empleado:", None))
        self.txt_codigo_empleado.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"Ej. EMP-001", None))
        self.lbl_cargo.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Cargo Institucional:", None))
        self.txt_cargo.setPlaceholderText(QCoreApplication.translate("EmpleadoFormDialog", u"Ej. Auxiliar de Biblioteca, Catalogador", None))
        self.lbl_turno.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Turno Laboral:", None))
        self.cbo_turno.setItemText(0, QCoreApplication.translate("EmpleadoFormDialog", u"Ma\u00f1ana", None))
        self.cbo_turno.setItemText(1, QCoreApplication.translate("EmpleadoFormDialog", u"Tarde", None))
        self.cbo_turno.setItemText(2, QCoreApplication.translate("EmpleadoFormDialog", u"Noche", None))
        self.cbo_turno.setItemText(3, QCoreApplication.translate("EmpleadoFormDialog", u"Completo", None))

        self.btn_guardar.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Guardar Empleado", None))
        self.btn_cancelar.setText(QCoreApplication.translate("EmpleadoFormDialog", u"Cancelar", None))
    # retranslateUi

