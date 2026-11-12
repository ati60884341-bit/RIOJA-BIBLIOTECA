from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QFormLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout

class Ui_RolFormDialog(object):
    def setupUi(self, RolFormDialog):
        if not RolFormDialog.objectName():
            RolFormDialog.setObjectName(u"RolFormDialog")
        RolFormDialog.resize(460, 300)
        self.verticalLayout = QVBoxLayout(RolFormDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.grp_rol = QGroupBox(RolFormDialog)
        self.grp_rol.setObjectName(u"grp_rol")
        self.form_rol = QFormLayout(self.grp_rol)
        self.form_rol.setObjectName(u"form_rol")
        self.form_rol.setVerticalSpacing(8)
        self.lbl_nombre_rol = QLabel(self.grp_rol)
        self.lbl_nombre_rol.setObjectName(u"lbl_nombre_rol")

        self.form_rol.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_nombre_rol)

        self.txt_nombre_rol = QLineEdit(self.grp_rol)
        self.txt_nombre_rol.setObjectName(u"txt_nombre_rol")

        self.form_rol.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_nombre_rol)

        self.lbl_descripcion = QLabel(self.grp_rol)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")

        self.form_rol.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_descripcion)

        self.txt_descripcion = QPlainTextEdit(self.grp_rol)
        self.txt_descripcion.setObjectName(u"txt_descripcion")

        self.form_rol.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_descripcion)


        self.verticalLayout.addWidget(self.grp_rol)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.layout_botones = QHBoxLayout()
        self.layout_botones.setObjectName(u"layout_botones")
        self.btn_guardar = QPushButton(RolFormDialog)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.layout_botones.addWidget(self.btn_guardar)

        self.btn_cancelar = QPushButton(RolFormDialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.layout_botones.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.layout_botones)


        self.retranslateUi(RolFormDialog)

        QMetaObject.connectSlotsByName(RolFormDialog)

    def retranslateUi(self, RolFormDialog):
        RolFormDialog.setWindowTitle(QCoreApplication.translate("RolFormDialog", u"Gesti\u00f3n de Roles - Registro Oficial", None))
        self.grp_rol.setTitle(QCoreApplication.translate("RolFormDialog", u"Datos del Rol en el Sistema", None))
        self.lbl_nombre_rol.setText(QCoreApplication.translate("RolFormDialog", u"Nombre del Rol:", None))
        self.txt_nombre_rol.setPlaceholderText(QCoreApplication.translate("RolFormDialog", u"Ej. Bibliotecario, Catalogador", None))
        self.lbl_descripcion.setText(QCoreApplication.translate("RolFormDialog", u"Descripci\u00f3n:", None))
        self.txt_descripcion.setPlaceholderText(QCoreApplication.translate("RolFormDialog", u"Funciones y permisos del rol (m\u00e1x. 150 caracteres)", None))
        self.btn_guardar.setText(QCoreApplication.translate("RolFormDialog", u"Guardar Rol", None))
        self.btn_cancelar.setText(QCoreApplication.translate("RolFormDialog", u"Cancelar", None))

