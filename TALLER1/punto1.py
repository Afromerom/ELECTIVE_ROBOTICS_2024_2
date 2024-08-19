from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Ui_Entrega1(object):
    def setupUi(self, Entrega1):
        Entrega1.setObjectName("Entrega1")
        Entrega1.resize(818, 784)
        self.label_3 = QtWidgets.QLabel(Entrega1)
        self.label_3.setGeometry(QtCore.QRect(120, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(Entrega1)
        self.label_8.setGeometry(QtCore.QRect(560, 20, 181, 101))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("TALLER1\IMAGENES\ecci.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(Entrega1)
        self.label_4.setGeometry(QtCore.QRect(470, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Entrega1)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Entrega1)
        self.label.setGeometry(QtCore.QRect(250, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Entrega1)
        self.label_7.setGeometry(QtCore.QRect(270, 30, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.valor1 = QtWidgets.QLabel(Entrega1)
        self.valor1.setGeometry(QtCore.QRect(250, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1.setFont(font)
        self.valor1.setText("")
        self.valor1.setObjectName("valor1")
        self.valor1_2 = QtWidgets.QLabel(Entrega1)
        self.valor1_2.setGeometry(QtCore.QRect(250, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.valor1_2.setFont(font)
        self.valor1_2.setText("")
        self.valor1_2.setObjectName("valor1_2")
        self.BUTTON_CONNECT = QtWidgets.QPushButton(Entrega1)
        self.BUTTON_CONNECT.setGeometry(QtCore.QRect(240, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BUTTON_CONNECT.setFont(font)
        self.BUTTON_CONNECT.setObjectName("BUTTON_CONNECT")
        self.BUTTON_CONNECT.setText("CONNECT")
        self.BUTTON_CONNECT.clicked.connect(self.check_com_connection)
        
        
        
        self.line = QtWidgets.QFrame(Entrega1)
        self.line.setGeometry(QtCore.QRect(270, 180, 22, 581))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line.setFont(font)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Entrega1)
        self.line_2.setGeometry(QtCore.QRect(10, 160, 791, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_17 = QtWidgets.QLabel(Entrega1)
        self.label_17.setGeometry(QtCore.QRect(80, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.line_4 = QtWidgets.QFrame(Entrega1)
        self.line_4.setGeometry(QtCore.QRect(10, 750, 791, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.GRAF_ACEL_X = QtWidgets.QWidget(Entrega1)
        self.GRAF_ACEL_X.setGeometry(QtCore.QRect(40, 220, 221, 171))
        self.GRAF_ACEL_X.setObjectName("GRAF_ACEL_X")
        self.COMMAND = QtWidgets.QTextEdit(Entrega1)
        self.COMMAND.setGeometry(QtCore.QRect(490, 130, 111, 31))
        self.COMMAND.setObjectName("COMMAND")
        self.COMMAND.textChanged.connect(self.check_command_input)
        
        
        self.label_20 = QtWidgets.QLabel(Entrega1)
        self.label_20.setGeometry(QtCore.QRect(120, 90, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Entrega1)
        self.label_21.setGeometry(QtCore.QRect(360, 50, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Entrega1)
        self.label_22.setGeometry(QtCore.QRect(360, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_18 = QtWidgets.QLabel(Entrega1)
        self.label_18.setGeometry(QtCore.QRect(40, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Entrega1)
        self.label_19.setGeometry(QtCore.QRect(340, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.line_5 = QtWidgets.QFrame(Entrega1)
        self.line_5.setGeometry(QtCore.QRect(530, 180, 22, 581))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_5.setFont(font)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_23 = QtWidgets.QLabel(Entrega1)
        self.label_23.setGeometry(QtCore.QRect(350, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Entrega1)
        self.label_24.setGeometry(QtCore.QRect(560, 180, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.line_7 = QtWidgets.QFrame(Entrega1)
        self.line_7.setGeometry(QtCore.QRect(0, 180, 22, 581))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_7.setFont(font)
        self.line_7.setLineWidth(1)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.GRAF_ACEL_Y = QtWidgets.QWidget(Entrega1)
        self.GRAF_ACEL_Y.setGeometry(QtCore.QRect(40, 400, 221, 171))
        self.GRAF_ACEL_Y.setObjectName("GRAF_ACEL_Y")
        self.GRAF_ACEL_Z = QtWidgets.QWidget(Entrega1)
        self.GRAF_ACEL_Z.setGeometry(QtCore.QRect(40, 580, 221, 171))
        self.GRAF_ACEL_Z.setObjectName("GRAF_ACEL_Z")
        self.GRAF_GIRO_X = QtWidgets.QWidget(Entrega1)
        self.GRAF_GIRO_X.setGeometry(QtCore.QRect(300, 220, 221, 171))
        self.GRAF_GIRO_X.setObjectName("GRAF_GIRO_X")
        self.GRAF_GIRO_Y = QtWidgets.QWidget(Entrega1)
        self.GRAF_GIRO_Y.setGeometry(QtCore.QRect(300, 400, 221, 171))
        self.GRAF_GIRO_Y.setObjectName("GRAF_GIRO_Y")
        self.GRAF_GIRO_Z = QtWidgets.QWidget(Entrega1)
        self.GRAF_GIRO_Z.setGeometry(QtCore.QRect(300, 580, 221, 171))
        self.GRAF_GIRO_Z.setObjectName("GRAF_GIRO_Z")
        self.GRAF_MAG_X = QtWidgets.QWidget(Entrega1)
        self.GRAF_MAG_X.setGeometry(QtCore.QRect(560, 220, 221, 171))
        self.GRAF_MAG_X.setObjectName("GRAF_MAG_X")
        self.GRAF_MAG_Y = QtWidgets.QWidget(Entrega1)
        self.GRAF_MAG_Y.setGeometry(QtCore.QRect(560, 400, 221, 171))
        self.GRAF_MAG_Y.setObjectName("GRAF_MAG_Y")
        self.GRAF_MAG_Z = QtWidgets.QWidget(Entrega1)
        self.GRAF_MAG_Z.setGeometry(QtCore.QRect(560, 580, 221, 171))
        self.GRAF_MAG_Z.setObjectName("GRAF_MAG_Z")
        self.line_8 = QtWidgets.QFrame(Entrega1)
        self.line_8.setGeometry(QtCore.QRect(790, 180, 22, 581))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.line_8.setFont(font)
        self.line_8.setLineWidth(1)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.DISCONNECT = QtWidgets.QPushButton(Entrega1)
        self.DISCONNECT.setGeometry(QtCore.QRect(620, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DISCONNECT.setFont(font)
        self.DISCONNECT.setObjectName("DISCONNECT")
        self.DISCONNECT.clicked.connect(self.disconnect_serial)

        # Agrega las figuras de Matplotlib
        self.figure_acel_x = Figure()
        self.canvas_acel_x = FigureCanvas(self.figure_acel_x)
        self.ax_acel_x = self.figure_acel_x.add_subplot(111)
        self.layout_acel_x = QtWidgets.QVBoxLayout(self.GRAF_ACEL_X)
        self.layout_acel_x.addWidget(self.canvas_acel_x)

        self.figure_acel_y = Figure()
        self.canvas_acel_y = FigureCanvas(self.figure_acel_y)
        self.ax_acel_y = self.figure_acel_y.add_subplot(111)
        self.layout_acel_y = QtWidgets.QVBoxLayout(self.GRAF_ACEL_Y)
        self.layout_acel_y.addWidget(self.canvas_acel_y)

        self.figure_acel_z = Figure()
        self.canvas_acel_z = FigureCanvas(self.figure_acel_z)
        self.ax_acel_z = self.figure_acel_z.add_subplot(111)
        self.layout_acel_z = QtWidgets.QVBoxLayout(self.GRAF_ACEL_Z)
        self.layout_acel_z.addWidget(self.canvas_acel_z)

        self.figure_gyro_x = Figure()
        self.canvas_gyro_x = FigureCanvas(self.figure_gyro_x)
        self.ax_gyro_x = self.figure_gyro_x.add_subplot(111)
        self.layout_gyro_x = QtWidgets.QVBoxLayout(self.GRAF_GIRO_X)
        self.layout_gyro_x.addWidget(self.canvas_gyro_x)

        self.figure_gyro_y = Figure()
        self.canvas_gyro_y = FigureCanvas(self.figure_gyro_y)
        self.ax_gyro_y = self.figure_gyro_y.add_subplot(111)
        self.layout_gyro_y = QtWidgets.QVBoxLayout(self.GRAF_GIRO_Y)
        self.layout_gyro_y.addWidget(self.canvas_gyro_y)

        self.figure_gyro_z = Figure()
        self.canvas_gyro_z = FigureCanvas(self.figure_gyro_z)
        self.ax_gyro_z = self.figure_gyro_z.add_subplot(111)
        self.layout_gyro_z = QtWidgets.QVBoxLayout(self.GRAF_GIRO_Z)
        self.layout_gyro_z.addWidget(self.canvas_gyro_z)

        self.figure_mag_x = Figure()
        self.canvas_mag_x = FigureCanvas(self.figure_mag_x)
        self.ax_mag_x = self.figure_mag_x.add_subplot(111)
        self.layout_mag_x = QtWidgets.QVBoxLayout(self.GRAF_MAG_X)
        self.layout_mag_x.addWidget(self.canvas_mag_x)

        self.figure_mag_y = Figure()
        self.canvas_mag_y = FigureCanvas(self.figure_mag_y)
        self.ax_mag_y = self.figure_mag_y.add_subplot(111)
        self.layout_mag_y = QtWidgets.QVBoxLayout(self.GRAF_MAG_Y)
        self.layout_mag_y.addWidget(self.canvas_mag_y)

        self.figure_mag_z = Figure()
        self.canvas_mag_z = FigureCanvas(self.figure_mag_z)
        self.ax_mag_z = self.figure_mag_z.add_subplot(111)
        self.layout_mag_z = QtWidgets.QVBoxLayout(self.GRAF_MAG_Z)
        self.layout_mag_z.addWidget(self.canvas_mag_z)

        # Datos para las gráficas
        self.data_accel_x = []
        self.data_accel_y = []
        self.data_accel_z = []

        self.data_gyro_x = []
        self.data_gyro_y = []
        self.data_gyro_z = []

        self.data_mag_x = []
        self.data_mag_y = []
        self.data_mag_z = []

        # Atributo para almacenar la conexión serial
        self.serial_connection = None
        # Temporizador para leer datos de la conexión serial
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_serial_data)
        
        self.retranslateUi(Entrega1)
        QtCore.QMetaObject.connectSlotsByName(Entrega1)
        
         
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

                    try:
                        if "Acelerómetro:" in data and "Giroscopio:" in data and "Magnetómetro:" in data:
                            # Extraer los datos del Acelerómetro
                            accel_data = data.split("Acelerómetro: [")[1].split("]")[0]
                            accel_values = [float(val) for val in accel_data.split(', ')]
                            self.data_accel_x.append(accel_values[0])
                            self.data_accel_y.append(accel_values[1])
                            self.data_accel_z.append(accel_values[2])

                            # Extraer los datos del Giroscopio
                            gyro_data = data.split("Giroscopio: [")[1].split("]")[0]
                            gyro_values = [float(val) for val in gyro_data.split(', ')]
                            self.data_gyro_x.append(gyro_values[0])
                            self.data_gyro_y.append(gyro_values[1])
                            self.data_gyro_z.append(gyro_values[2])

                            # Extraer los datos del Magnetómetro
                            mag_data = data.split("Magnetómetro: [")[1].split("]")[0]
                            mag_values = [float(val) for val in mag_data.split(', ')]
                            self.data_mag_x.append(mag_values[0])
                            self.data_mag_y.append(mag_values[1])
                            self.data_mag_z.append(mag_values[2])

                            self.update_graphs()
                        else:
                            print("Formato de datos inesperado:", data)
                    except (IndexError, ValueError) as e:
                        print(f"Error al procesar los datos: {e}")
        
            except serial.SerialException as e:
                print(f"Error al leer datos: {e}")

                
    def update_graphs(self):
        # Limita la cantidad de puntos en la gráfica
        max_points = 100
        self.data_accel_x = self.data_accel_x[-max_points:]
        self.data_accel_y = self.data_accel_y[-max_points:]
        self.data_accel_z = self.data_accel_z[-max_points:]

        self.data_gyro_x = self.data_gyro_x[-max_points:]
        self.data_gyro_y = self.data_gyro_y[-max_points:]
        self.data_gyro_z = self.data_gyro_z[-max_points:]

        self.data_mag_x = self.data_mag_x[-max_points:]
        self.data_mag_y = self.data_mag_y[-max_points:]
        self.data_mag_z = self.data_mag_z[-max_points:]

        # Actualiza las gráficas del Acelerómetro
        self.ax_acel_x.clear()
        self.ax_acel_x.plot(self.data_accel_x, label='accelX')
        self.ax_acel_x.set_title("Acelerómetro X", fontsize=7)
        self.ax_acel_x.set_xlabel("Tiempo")
        self.ax_acel_x.set_ylabel("G's")
        self.figure_acel_x.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_acel_x.draw()

        self.ax_acel_y.clear()
        self.ax_acel_y.plot(self.data_accel_y, label='accelY')
        self.ax_acel_y.set_title("Acelerómetro Y", fontsize=7)
        self.ax_acel_y.set_xlabel("Tiempo")
        self.ax_acel_y.set_ylabel("G's")
        self.figure_acel_y.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_acel_y.draw()

        self.ax_acel_z.clear()
        self.ax_acel_z.plot(self.data_accel_z, label='accelZ')
        self.ax_acel_z.set_title("Acelerómetro Z", fontsize=7)
        self.ax_acel_z.set_xlabel("Tiempo")
        self.ax_acel_z.set_ylabel("G's")
        self.figure_acel_z.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_acel_z.draw()

        # Actualiza las gráficas del Giroscopio
        self.ax_gyro_x.clear()
        self.ax_gyro_x.plot(self.data_gyro_x, label='gyroX')
        self.ax_gyro_x.set_title("Giroscopio X", fontsize=7)
        self.ax_gyro_x.set_xlabel("Tiempo")
        self.ax_gyro_x.set_ylabel("°/s")
        self.figure_gyro_x.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_gyro_x.draw()

        self.ax_gyro_y.clear()
        self.ax_gyro_y.plot(self.data_gyro_y, label='gyroY')
        self.ax_gyro_y.set_title("Giroscopio Y", fontsize=7)
        self.ax_gyro_y.set_xlabel("Tiempo")
        self.ax_gyro_y.set_ylabel("°/s")
        self.figure_gyro_y.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_gyro_y.draw()

        self.ax_gyro_z.clear()
        self.ax_gyro_z.plot(self.data_gyro_z, label='gyroZ')
        self.ax_gyro_z.set_title("Giroscopio Z", fontsize=7)
        self.ax_gyro_z.set_xlabel("Tiempo")
        self.ax_gyro_z.set_ylabel("°/s")
        self.figure_gyro_z.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_gyro_z.draw()

        # Actualiza las gráficas del Magnetómetro
        self.ax_mag_x.clear()
        self.ax_mag_x.plot(self.data_mag_x, label='magX')
        self.ax_mag_x.set_title("Magnetómetro X", fontsize=7)
        self.ax_mag_x.set_xlabel("Tiempo")
        self.ax_mag_x.set_ylabel("uT")
        self.figure_mag_x.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_mag_x.draw()

        self.ax_mag_y.clear()
        self.ax_mag_y.plot(self.data_mag_y, label='magY')
        self.ax_mag_y.set_title("Magnetómetro Y", fontsize=7)
        self.ax_mag_y.set_xlabel("Tiempo")
        self.ax_mag_y.set_ylabel("uT")
        self.figure_mag_y.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_mag_y.draw()

        self.ax_mag_z.clear()
        self.ax_mag_z.plot(self.data_mag_z, label='magZ')
        self.ax_mag_z.set_title("Magnetómetro Z", fontsize=7)
        self.ax_mag_z.set_xlabel("Tiempo")
        self.ax_mag_z.set_ylabel("uT")
        self.figure_mag_z.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_mag_z.draw()



    def disconnect_serial(self):
        """Detiene la lectura de datos y cierra la conexión serial."""
        if self.timer.isActive():
            self.timer.stop()  # Detiene el temporizador
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()  # Cierra la conexión serial
            print("Conexión serial cerrada")
        self.BUTTON_CONNECT.setText("CONNECT")
        self.COMMAND.clear()  # Borra cualquier comando pendiente

    def retranslateUi(self, Entrega1):
        _translate = QtCore.QCoreApplication.translate
        Entrega1.setWindowTitle(_translate("Entrega1", "Entrega1"))
        self.label_3.setText(_translate("Entrega1", "Andrés Felipe Romero Medina"))
        self.label_4.setText(_translate("Entrega1", "2024 - 2"))
        self.label_2.setText(_translate("Entrega1", "Nicolas Mejia Muñoz"))
        self.label.setText(_translate("Entrega1", "Algoritmos de Robótica  II"))
        self.label_7.setText(_translate("Entrega1", "Ingeniería Mecatrónica"))
        self.BUTTON_CONNECT.setText(_translate("Entrega1", "CONNECT"))
        self.label_17.setText(_translate("Entrega1", "LECTURA COM: "))
        self.label_20.setText(_translate("Entrega1", "Valentina Elizabeth Rubiano Avendaño"))
        self.label_21.setText(_translate("Entrega1", "Adriana Patricia Bolivar Bolivar"))
        self.label_22.setText(_translate("Entrega1", "Alex Andrés Acevedo Mora"))
        self.label_18.setText(_translate("Entrega1", "ACELERÓMETRO"))
        self.label_19.setText(_translate("Entrega1", "GIRÓSCOPIO"))
        self.label_23.setText(_translate("Entrega1", "ACTIVACIÓN: "))
        self.label_24.setText(_translate("Entrega1", "MAGNETÓMETRO"))
        self.DISCONNECT.setText(_translate("Entrega1", "DISCONNECT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Entrega1 = QtWidgets.QDialog()
    ui = Ui_Entrega1()
    ui.setupUi(Entrega1)
    Entrega1.show()
    sys.exit(app.exec_())
