from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 160, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(240, 160, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.STATE = QtWidgets.QLabel(Dialog)
        self.STATE.setGeometry(QtCore.QRect(110, 190, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.STATE.setFont(font)
        self.STATE.setText("")
        self.STATE.setObjectName("STATE")
        self.timer = QtWidgets.QLabel(Dialog)
        self.timer.setGeometry(QtCore.QRect(180, 160, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timer.setFont(font)
        self.timer.setText("")
        self.timer.setObjectName("timer")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 110, 191, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Conectar el botón a la función start_timer
        self.pushButton_3.clicked.connect(self.start_timer)

        # Configurar un temporizador para la cuenta regresiva
        self.countdown_timer = QtCore.QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)

        # Variable para almacenar el tiempo restante
        self.time_remaining = 30

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "TIMER"))
        self.label_9.setText(_translate("Dialog", "s"))
        self.pushButton_3.setText(_translate("Dialog", "START"))

    def start_timer(self):
        # Cambiar el texto y color del estado a "LOADING" en azul
        self.STATE.setText("LOADING")
        self.STATE.setStyleSheet("color: blue;")
        
        # Inicializar la cuenta regresiva a 30 segundos
        self.time_remaining = 30
        self.timer.setText(str(self.time_remaining))
        
        # Iniciar el temporizador (1 segundo)
        self.countdown_timer.start(1000)

    def update_timer(self):
        self.time_remaining -= 1
        self.timer.setText(str(self.time_remaining))
        
        if self.time_remaining == 0:
            self.countdown_timer.stop()
            # Cambiar el texto y color del estado a "DONE" en verde
            self.STATE.setText("DONE")
            self.STATE.setStyleSheet("color: green;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
