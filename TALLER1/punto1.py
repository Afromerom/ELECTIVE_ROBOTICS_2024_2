from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1550, 900)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(620, 20, 181, 101))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER1\IMAGENES\ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(530, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(330, 30, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.valor1 = QtWidgets.QLabel(Dialog)
        self.valor1.setGeometry(QtCore.QRect(250, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1.setFont(font)
        self.valor1.setText("")
        self.valor1.setObjectName("valor1")
        self.valor1_2 = QtWidgets.QLabel(Dialog)
        self.valor1_2.setGeometry(QtCore.QRect(250, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_2.setFont(font)
        self.valor1_2.setText("")
        self.valor1_2.setObjectName("valor1_2")
        self.valor1_3 = QtWidgets.QLabel(Dialog)
        self.valor1_3.setGeometry(QtCore.QRect(250, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_3.setFont(font)
        self.valor1_3.setText("")
        self.valor1_3.setObjectName("valor1_3")
        
        self.BUTTON_CONNECT = QtWidgets.QPushButton(Dialog)
        self.BUTTON_CONNECT.setGeometry(QtCore.QRect(340, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BUTTON_CONNECT.setFont(font)
        self.BUTTON_CONNECT.setObjectName("BUTTON_CONNECT")
        self.BUTTON_CONNECT.setText("CONNECT")
        self.BUTTON_CONNECT.clicked.connect(self.check_com_connection)
        
        
        
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(500, 180, 22, 690))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line.setFont(font)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 160, 1500, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(180, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(10, 860, 1500, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.GRAF_ACEL = QtWidgets.QWidget(Dialog)
        self.GRAF_ACEL.setGeometry(QtCore.QRect(30, 220, 261, 211))
        self.GRAF_ACEL.setObjectName("GRAF_ACEL")
        
        
        
        self.COMMAND = QtWidgets.QTextEdit(Dialog)
        self.COMMAND.setGeometry(QtCore.QRect(590, 130, 111, 31))
        self.COMMAND.setObjectName("COMMAND")
        self.COMMAND.textChanged.connect(self.check_command_input)
        
        
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(180, 90, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(420, 50, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(420, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(130, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(700, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.GRAF_GIRO = QtWidgets.QWidget(Dialog)
        self.GRAF_GIRO.setGeometry(QtCore.QRect(320, 220, 400, 211))
        self.GRAF_GIRO.setObjectName("GRAF_GIRO")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(1000, 180, 22, 690))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_5.setFont(font)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(450, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(1150, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.GRAF_MAG = QtWidgets.QWidget(Dialog)
        self.GRAF_MAG.setGeometry(QtCore.QRect(610, 220, 261, 211))
        self.GRAF_MAG.setObjectName("GRAF_MAG")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(1500, 180, 22, 690))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_6.setFont(font)
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(0, 180, 22, 690))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_7.setFont(font)
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        # Atributo para almacenar la conexión serial
        self.serial_connection = None
        # Temporizador para leer datos de la conexión serial
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_serial_data)
        
        # Widget para las gráficas
        self.GRAF_ACEL = QtWidgets.QWidget(Dialog)
        self.GRAF_ACEL.setGeometry(QtCore.QRect(30, 220, 470, 400))
        self.GRAF_ACEL.setObjectName("GRAF_ACEL")

        # Creación del canvas de matplotlib dentro de GRAF_ACEL
        self.sc = MplCanvas(self.GRAF_ACEL, width=5, height=4, dpi=100)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Entrega1"))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        # (Resto del código omitido por brevedad)
        
    def check_com_connection(self):
        ports = list(serial.tools.list_ports.comports())
        if ports:
            port_name = ports[0].device  # Toma el primer puerto COM encontrado
            self.BUTTON_CONNECT.setText(f"{port_name}")
            # Abre la conexión serial
            try:
                self.serial_connection = serial.Serial(port_name, baudrate=9600, timeout=1)
                self.timer.start(100)  # Lee datos cada 100 ms
            except serial.SerialException as e:
                print(f"Error al abrir el puerto {port_name}: {e}")
        else:
            self.BUTTON_CONNECT.setText("No COM Connected")
            
    def check_command_input(self):
        text = self.COMMAND.toPlainText().strip()
        if text.lower() == 'h' and self.serial_connection and self.serial_connection.is_open:
            self.activate_protocol()
            self.COMMAND.clear()  # Borra el texto después de la activación
            
    def plot_acceleration(self, t, accelX, accelY, accelZ):
        self.sc.axes.clear()  # Limpiar el gráfico
        self.sc.axes.plot(t, accelX, 'b', label='ax')
        self.sc.axes.plot(t, accelY, 'r', label='ay')
        self.sc.axes.plot(t, accelZ, 'g', label='az')
        self.sc.axes.set_title('Acelerômetros da MPU6050 sem calibração')
        self.sc.axes.set_xlabel('Tempo (segundos)')
        self.sc.axes.set_ylabel('aceleração (g)')
        self.sc.axes.legend(loc='upper right')
        self.sc.draw()  # Redibujar la gráfica

    def activate_protocol(self):
        # Simulación de datos para `accelX`, `accelY`, `accelZ` y `t`
        t = np.linspace(0, 10, 100)  # Simulando 100 puntos en 10 segundos
        accelX = np.sin(t)
        accelY = np.cos(t)
        accelZ = np.sin(t + np.pi / 4)

        # Llamar a la función de graficado
        self.plot_acceleration(t, accelX, accelY, accelZ)
        
    def activate_protocol(self):
        if self.serial_connection:
            try:
                self.serial_connection.write(b'H')  # Envía el carácter 'H' por el puerto COM
                print("Protocolo de comunicación activado")
            except serial.SerialException as e:
                print(f"Error al enviar datos: {e}")
                
    def read_serial_data(self):
        if self.serial_connection and self.serial_connection.is_open:
            try:
                if self.serial_connection.in_waiting > 0:
                    data = self.serial_connection.readline().decode('utf-8').strip()
                    print(data)  # Imprime los datos recibidos en la consola
            except serial.SerialException as e:
                print(f"Error al leer datos: {e}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Entrega1"))
        self.label_3.setText(_translate("Dialog", "Andrés Felipe Romero Medina"))
        self.label_4.setText(_translate("Dialog", "2024 - 2"))
        self.label_2.setText(_translate("Dialog", "Nicolas Mejia Muñoz"))
        self.label.setText(_translate("Dialog", "Algoritmos de Robótica  II"))
        self.label_7.setText(_translate("Dialog", "Ingeniería Mecatrónica"))
        self.BUTTON_CONNECT.setText(_translate("Dialog", "CONNECT"))
        self.label_17.setText(_translate("Dialog", "LECTURA COM: "))
        self.label_20.setText(_translate("Dialog", "Valentina Elizabeth Rubiano Avendaño"))
        self.label_21.setText(_translate("Dialog", "Adriana Patricia Bolivar Bolivar"))
        self.label_22.setText(_translate("Dialog", "Alex Andrés Acevedo Mora"))
        self.label_18.setText(_translate("Dialog", "ACELEROMETRO"))
        self.label_19.setText(_translate("Dialog", "GIROSCOPIO"))
        self.label_23.setText(_translate("Dialog", "ACTIVACIÓN: "))
        self.label_24.setText(_translate("Dialog", "MAGNETOMETRO"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
