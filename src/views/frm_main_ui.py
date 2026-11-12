from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import QLabel, QMenu, QMenuBar, QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_salir = QAction(MainWindow)
        self.action_salir.setObjectName(u"action_salir")
        self.action_programas = QAction(MainWindow)
        self.action_programas.setObjectName(u"action_programas")
        self.action_empleados = QAction(MainWindow)
        self.action_empleados.setObjectName(u"action_empleados")
        self.action_roles = QAction(MainWindow)
        self.action_roles.setObjectName(u"action_roles")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spacer_superior = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer_superior)

        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.lbl_subtitulo = QLabel(self.centralwidget)
        self.lbl_subtitulo.setObjectName(u"lbl_subtitulo")
        font1 = QFont()
        font1.setPointSize(11)
        self.lbl_subtitulo.setFont(font1)
        self.lbl_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_subtitulo)

        self.spacer_inferior = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer_inferior)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuMantenimiento = QMenu(self.menubar)
        self.menuMantenimiento.setObjectName(u"menuMantenimiento")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuMantenimiento.menuAction())
        self.menuArchivo.addAction(self.action_salir)
        self.menuMantenimiento.addAction(self.action_programas)
        self.menuMantenimiento.addAction(self.action_empleados)
        self.menuMantenimiento.addAction(self.action_roles)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema Integrado de Gesti\u00f3n Bibliotecaria", None))
        self.action_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.action_programas.setText(QCoreApplication.translate("MainWindow", u"Programas de Estudio", None))
        self.action_empleados.setText(QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.action_roles.setText(QCoreApplication.translate("MainWindow", u"Roles del Sistema", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE GESTI\u00d3N INSTITUCIONAL", None))
        self.lbl_subtitulo.setText(QCoreApplication.translate("MainWindow", u"Seleccione una opci\u00f3n del men\u00fa superior para comenzar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"&Archivo", None))
        self.menuMantenimiento.setTitle(QCoreApplication.translate("MainWindow", u"&Mantenimiento", None))

