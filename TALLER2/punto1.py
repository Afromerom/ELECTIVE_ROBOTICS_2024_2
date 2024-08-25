from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Ui_Entrega1(QtWidgets.QDialog):
    update_plot_signal = QtCore.pyqtSignal(list, list, list, list, list, list , list, list, list)
    
    def __init__(self):
        super(Ui_Entrega1, self).__init__()
        self.setupUi(self)
    
    def setupUi(self, Entrega1):
        Entrega1.setObjectName("Entrega1")
        Entrega1.resize(818, 784)

        # Definir los widgets para las gráficas
        self.GRAF_ACEL_X = QtWidgets.QWidget(Entrega1)
        self.GRAF_ACEL_X.setGeometry(QtCore.QRect(40, 220, 221, 171))
        self.GRAF_ACEL_X.setObjectName("GRAF_ACEL_X")

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

        # Configuración de otros elementos de la interfaz (omitido por brevedad)

        self.BUTTON_CONNECT = QtWidgets.QPushButton(Entrega1)
        self.BUTTON_CONNECT.setGeometry(QtCore.QRect(240, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BUTTON_CONNECT.setFont(font)
        self.BUTTON_CONNECT.setObjectName("BUTTON_CONNECT")
        self.BUTTON_CONNECT.setText("CONNECT")
        self.BUTTON_CONNECT.clicked.connect(self.check_com_connection)
        
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
        self.acel_x_dato = []
        self.acel_y_dato = []
        self.acel_z_dato = []

        self.giros_x_dato = []
        self.giros_y_dato = []
        self.giros_z_dato = []

        self.mag_x_dato = []
        self.mag_y_dato = []
        self.mag_z_dato = []

        # Atributo para almacenar la conexión serial
        self.serial_connection = None
        # Temporizador para leer datos de la conexión serial
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_serial_data)
        
        # Conectar la señal para actualizar las gráficas
        self.update_plot_signal.connect(self.update_graphs)
        
        self.retranslateUi(Entrega1)
        QtCore.QMetaObject.connectSlotsByName(Entrega1)

    def check_com_connection(self):
        ports = list(serial.tools.list_ports.comports())
        if ports:
            port_name = ports[0].device
            self.BUTTON_CONNECT.setText(f"{port_name}")
            try:
                self.serial_connection = serial.Serial(port_name, baudrate=9600, timeout=1)
                self.serial_connection.write(b'H')
                self.timer.start(100)
            except serial.SerialException as e:
                print(f"Error al abrir el puerto {port_name}: {e}")
        else:
            self.BUTTON_CONNECT.setText("No COM Connected")

    def read_serial_data(self):
        SENSITIVITY_ACCEL = 2.0 / 32768.0
        SENSITIVITY_GYRO = 250.0 / 32768.0
        SENSITIVITY_MAGN = 4800.0 / 32768.0

        if self.serial_connection and self.serial_connection.is_open:
            try:
                if self.serial_connection.in_waiting > 0:
                    data = self.serial_connection.readline().decode('utf-8').strip()
                    data_parts = data.split()
                    
                    if len(data_parts) == 10:
                        acel_x = float(data_parts[1]) * SENSITIVITY_ACCEL
                        acel_y = float(data_parts[2]) * SENSITIVITY_ACCEL
                        acel_z = float(data_parts[3]) * SENSITIVITY_ACCEL

                        giros_x = float(data_parts[4]) * SENSITIVITY_GYRO
                        giros_y = float(data_parts[5]) * SENSITIVITY_GYRO
                        giros_z = float(data_parts[6]) * SENSITIVITY_GYRO

                        mag_x = float(data_parts[7]) * SENSITIVITY_MAGN
                        mag_y = float(data_parts[8]) * SENSITIVITY_MAGN
                        mag_z = float(data_parts[9]) * SENSITIVITY_MAGN

                        self.acel_x_dato.append(acel_x)
                        self.acel_y_dato.append(acel_y)
                        self.acel_z_dato.append(acel_z)

                        self.giros_x_dato.append(giros_x)
                        self.giros_y_dato.append(giros_y)
                        self.giros_z_dato.append(giros_z)

                        self.mag_x_dato.append(mag_x)
                        self.mag_y_dato.append(mag_y)
                        self.mag_z_dato.append(mag_z)

                        self.update_plot_signal.emit(self.acel_x_dato, self.acel_y_dato, self.acel_z_dato, self.giros_x_dato, self.giros_y_dato, self.giros_z_dato, self.mag_x_dato, self.mag_y_dato, self.mag_z_dato)
            except serial.SerialException as e:
                print(f"Error al leer datos: {e}")

    def update_graphs(self, acel_x_dato, acel_y_dato, acel_z_dato, giros_x_dato, giros_y_dato, giros_z_dato, mag_x_dato, mag_y_dato, mag_z_dato):
        max_points = 100
        self.acel_x_dato = self.acel_x_dato[-max_points:]
        self.acel_y_dato = self.acel_y_dato[-max_points:]
        self.acel_z_dato = self.acel_z_dato[-max_points:]

        self.giros_x_dato = self.giros_x_dato[-max_points:]
        self.giros_y_dato = self.giros_y_dato[-max_points:]
        self.giros_z_dato = self.giros_z_dato[-max_points:]

        self.mag_x_dato = self.mag_x_dato[-max_points:]
        self.mag_y_dato = self.mag_y_dato[-max_points:]
        self.mag_z_dato = self.mag_z_dato[-max_points:]

        # Actualiza las gráficas del Acelerómetro
        self.ax_acel_x.clear()
        self.ax_acel_x.plot(self.acel_x_dato, label='accelX')
        self.ax_acel_x.set_title("Acelerómetro X", fontsize=7)
        self.ax_acel_x.set_xlabel("Tiempo")
        self.ax_acel_x.set_ylabel("G's")
        self.figure_acel_x.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_acel_x.draw()

        self.ax_acel_y.clear()
        self.ax_acel_y.plot(self.acel_y_dato, label='accelY')
        self.ax_acel_y.set_title("Acelerómetro Y", fontsize=7)
        self.ax_acel_y.set_xlabel("Tiempo")
        self.ax_acel_y.set_ylabel("G's")
        self.figure_acel_y.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_acel_y.draw()

        self.ax_acel_z.clear()
        self.ax_acel_z.plot(self.acel_z_dato, label='accelZ')
        self.ax_acel_z.set_title("Acelerómetro Z", fontsize=7)
        self.ax_acel_z.set_xlabel("Tiempo")
        self.ax_acel_z.set_ylabel("G's")
        self.figure_acel_z.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_acel_z.draw()

        # Actualiza las gráficas del Giroscopio
        self.ax_gyro_x.clear()
        self.ax_gyro_x.plot(self.giros_x_dato, label='gyroX')
        self.ax_gyro_x.set_title("Giroscopio X", fontsize=7)
        self.ax_gyro_x.set_xlabel("Tiempo")
        self.ax_gyro_x.set_ylabel("°/s")
        self.figure_gyro_x.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_gyro_x.draw()

        self.ax_gyro_y.clear()
        self.ax_gyro_y.plot(self.giros_y_dato, label='gyroY')
        self.ax_gyro_y.set_title("Giroscopio Y", fontsize=7)
        self.ax_gyro_y.set_xlabel("Tiempo")
        self.ax_gyro_y.set_ylabel("°/s")
        self.figure_gyro_y.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_gyro_y.draw()

        self.ax_gyro_z.clear()
        self.ax_gyro_z.plot(self.giros_z_dato, label='gyroZ')
        self.ax_gyro_z.set_title("Giroscopio Z", fontsize=7)
        self.ax_gyro_z.set_xlabel("Tiempo")
        self.ax_gyro_z.set_ylabel("°/s")
        self.figure_gyro_z.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_gyro_z.draw()

        # Actualiza las gráficas del Magnetómetro
        self.ax_mag_x.clear()
        self.ax_mag_x.plot(self.mag_x_dato, label='magX')
        self.ax_mag_x.set_title("Magnetómetro X", fontsize=7)
        self.ax_mag_x.set_xlabel("Tiempo")
        self.ax_mag_x.set_ylabel("uT")
        self.figure_mag_x.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_mag_x.draw()

        self.ax_mag_y.clear()
        self.ax_mag_y.plot(self.mag_y_dato, label='magY')
        self.ax_mag_y.set_title("Magnetómetro Y", fontsize=7)
        self.ax_mag_y.set_xlabel("Tiempo")
        self.ax_mag_y.set_ylabel("uT")
        self.figure_mag_y.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_mag_y.draw()

        self.ax_mag_z.clear()
        self.ax_mag_z.plot(self.mag_z_dato, label='magZ')
        self.ax_mag_z.set_title("Magnetómetro Z", fontsize=7)
        self.ax_mag_z.set_xlabel("Tiempo")
        self.ax_mag_z.set_ylabel("uT")
        self.figure_mag_z.subplots_adjust(left=0.4, right=0.95, top=0.85, bottom=0.3)
        self.canvas_mag_z.draw()

    def disconnect_serial(self):
        if self.timer.isActive():
            self.timer.stop()
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Conexión serial cerrada")
        self.BUTTON_CONNECT.setText("CONNECT")
        self.COMMAND.clear()

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
