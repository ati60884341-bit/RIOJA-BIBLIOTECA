# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_programa_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ProgramaFormDialog(object):
    def setupUi(self, ProgramaFormDialog):
        if not ProgramaFormDialog.objectName():
            ProgramaFormDialog.setObjectName(u"ProgramaFormDialog")
        ProgramaFormDialog.resize(460, 240)
        self.verticalLayout = QVBoxLayout(ProgramaFormDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.grp_programa = QGroupBox(ProgramaFormDialog)
        self.grp_programa.setObjectName(u"grp_programa")
        self.form_programa = QFormLayout(self.grp_programa)
        self.form_programa.setObjectName(u"form_programa")
        self.form_programa.setVerticalSpacing(8)
        self.lbl_codigo_programa = QLabel(self.grp_programa)
        self.lbl_codigo_programa.setObjectName(u"lbl_codigo_programa")

        self.form_programa.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_codigo_programa)

        self.txt_codigo_programa = QLineEdit(self.grp_programa)
        self.txt_codigo_programa.setObjectName(u"txt_codigo_programa")

        self.form_programa.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_codigo_programa)

        self.lbl_nombre_programa = QLabel(self.grp_programa)
        self.lbl_nombre_programa.setObjectName(u"lbl_nombre_programa")

        self.form_programa.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_nombre_programa)

        self.txt_nombre_programa = QLineEdit(self.grp_programa)
        self.txt_nombre_programa.setObjectName(u"txt_nombre_programa")

        self.form_programa.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_nombre_programa)

        self.chk_estado = QCheckBox(self.grp_programa)
        self.chk_estado.setObjectName(u"chk_estado")
        self.chk_estado.setChecked(True)

        self.form_programa.setWidget(2, QFormLayout.ItemRole.FieldRole, self.chk_estado)


        self.verticalLayout.addWidget(self.grp_programa)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.layout_botones = QHBoxLayout()
        self.layout_botones.setObjectName(u"layout_botones")
        self.btn_guardar = QPushButton(ProgramaFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.layout_botones.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(ProgramaFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.layout_botones.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.layout_botones)


        self.retranslateUi(ProgramaFormDialog)

        QMetaObject.connectSlotsByName(ProgramaFormDialog)
    # setupUi

    def retranslateUi(self, ProgramaFormDialog):
        ProgramaFormDialog.setWindowTitle(QCoreApplication.translate("ProgramaFormDialog", u"Programas de Estudio - Registro Oficial", None))
        self.grp_programa.setTitle(QCoreApplication.translate("ProgramaFormDialog", u"Datos del Programa de Estudio", None))
        self.lbl_codigo_programa.setText(QCoreApplication.translate("ProgramaFormDialog", u"C\u00f3digo (m\u00e1x. 10):", None))
        self.txt_codigo_programa.setPlaceholderText(QCoreApplication.translate("ProgramaFormDialog", u"Ej. DSI, CONT", None))
        self.lbl_nombre_programa.setText(QCoreApplication.translate("ProgramaFormDialog", u"Nombre del Programa:", None))
        self.txt_nombre_programa.setPlaceholderText(QCoreApplication.translate("ProgramaFormDialog", u"Ej. Desarrollo de Sistemas de Informaci\u00f3n", None))
        self.chk_estado.setText(QCoreApplication.translate("ProgramaFormDialog", u"Programa Activo", None))
        self.btn_guardar.setText(QCoreApplication.translate("ProgramaFormDialog", u"Guardar Programa", None))
        self.btn_cancelar.setText(QCoreApplication.translate("ProgramaFormDialog", u"Cancelar", None))
    # retranslateUi

