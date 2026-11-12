from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(560, 250)
        self.lbl_titulo = QLabel(Form)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(20, 20, 520, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_usuario = QLabel(Form)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(60, 85, 130, 30))
        self.txt_usuario = QLineEdit(Form)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(200, 85, 300, 30))
        self.lbl_password = QLabel(Form)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setGeometry(QRect(60, 130, 130, 30))
        self.txt_password = QLineEdit(Form)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(200, 130, 300, 30))
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.btn_ingresar = QPushButton(Form)
        self.btn_ingresar.setObjectName(u"btn_ingresar")
        self.btn_ingresar.setGeometry(QRect(200, 185, 300, 36))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Inicio de Sesi\u00f3n - Sistema de Biblioteca", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"SISTEMA DE GESTI\u00d3N DE BIBLIOTECA", None))
        self.lbl_usuario.setText(QCoreApplication.translate("Form", u"Usuario / Correo:", None))
        self.lbl_password.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a:", None))
        self.btn_ingresar.setText(QCoreApplication.translate("Form", u"Ingresar al Sistema", None))

