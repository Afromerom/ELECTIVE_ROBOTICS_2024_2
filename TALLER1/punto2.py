import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import serial
import threading




class Ui_MainWindow(QtWidgets.QMainWindow):
    update_plot_signal = QtCore.pyqtSignal(list, list, list, list, list, list , list, list, list, list)
    
        

    def __init__(self):
        super().__init__()
        self.setupUi()
        
        # Serial connection
        self.serial_connection = None
        self.running = False
        self.acel_x_dato = []
        self.acel_y_dato = []
        self.acel_z_dato = []

        self.giros_x_dato = []
        self.giros_y_dato = []
        self.giros_z_dato = []

        self.mag_x_dato = []
        self.mag_y_dato = []
        self.mag_z_dato = []

        self.indices = []  # Lista para los índices del eje X
        self.index = 0     # Inicializar el contador de índice
        
        # Conectar la señal para actualizar las gráficas
        self.update_plot_signal.connect(self.actualizar_plots)
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1074, 874)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        # Graficas
        self.graph_acel_x = pg.PlotWidget(self.centralwidget)
        self.graph_acel_x.setGeometry(QtCore.QRect(20, 280, 301, 111))
        self.graph_acel_x.setObjectName("graph_acel_x")
        
        self.graph_acel_y = pg.PlotWidget(self.centralwidget)
        self.graph_acel_y.setGeometry(QtCore.QRect(20, 470, 301, 111))
        self.graph_acel_y.setObjectName("graph_acel_y")
        
        self.graph_acel_z = pg.PlotWidget(self.centralwidget)
        self.graph_acel_z.setGeometry(QtCore.QRect(20, 660, 301, 111))
        self.graph_acel_z.setObjectName("graph_acel_z")

        self.graph_giros_x = pg.PlotWidget(self.centralwidget)
        self.graph_giros_x.setGeometry(QtCore.QRect(360, 280, 301, 111))
        self.graph_giros_x.setObjectName("graph_giros_x")

        self.graph_giros_y = pg.PlotWidget(self.centralwidget)
        self.graph_giros_y.setGeometry(QtCore.QRect(360, 470, 301, 111))
        self.graph_giros_y.setObjectName("graph_giros_y")

        self.graph_giros_z = pg.PlotWidget(self.centralwidget)
        self.graph_giros_z.setGeometry(QtCore.QRect(360, 660, 301, 111))
        self.graph_giros_z.setObjectName("graph_giros_z")

        # Gráficas del magnetómetro
        self.graph_mag_x = pg.PlotWidget(self.centralwidget)
        self.graph_mag_x.setGeometry(QtCore.QRect(450, 0, 631, 271))  # Tamaño ajustado
        self.graph_mag_x.setObjectName("graph_mag_x")

        self.graph_mag_y = pg.PlotWidget(self.centralwidget)
        self.graph_mag_y.setGeometry(QtCore.QRect(410, 280, 671, 191))  # Tamaño ajustado
        self.graph_mag_y.setObjectName("graph_mag_y")

        self.graph_mag_z = pg.PlotWidget(self.centralwidget)
        self.graph_mag_z.setGeometry(QtCore.QRect(430, 480, 651, 241))  # Tamaño ajustado
        self.graph_mag_z.setObjectName("graph_mag_z")
        
        # Combo box
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 210, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("COM3")
        self.comboBox.addItem("COM4")
        
        # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 430, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 620, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 250, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 440, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 630, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(700, 250, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 440, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 630, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
        # Botón para iniciar
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(220, 160, 121, 41))
        self.startButton.setObjectName("startButton")
        self.startButton.setText("Iniciar")
        self.startButton.clicked.connect(self.inicio_adquisicion)

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(750, 20, 221, 121))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../../Escritorio/logo_ecci.png"))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 511, 101))
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_12")


       # Botón para parar
        self.startButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.startButton2.setGeometry(QtCore.QRect(220, 210, 121, 41))
        self.startButton2.setObjectName("startButton2")
        self.startButton2.setText("STOP")
        self.startButton2.clicked.connect(self.detener_adquisicion)
       
                
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "COM4"))
        self.label.setText(_translate("MainWindow", "PUERTO"))
        self.label_2.setText(_translate("MainWindow", "ACELEROMETRO EN X"))
        self.label_3.setText(_translate("MainWindow", "ACELEROMETRO EN Y"))
        self.label_4.setText(_translate("MainWindow", "ACELEROMETRO EN Z"))

        self.label_6.setText(_translate("MainWindow", "GIROSCOPIO EN X"))
        self.label_7.setText(_translate("MainWindow", "GIROSCOPIO EN Y"))
        self.label_8.setText(_translate("MainWindow", "GIROSCOPIO EN Z"))
        self.label_9.setText(_translate("MainWindow", "MAGNETOMETRO EN X"))
        self.label_10.setText(_translate("MainWindow", "MAGNETOMETRO EN Y"))
        self.label_11.setText(_translate("MainWindow", "MAGNETOMETRO EN Z"))
        self.label_13.setText(_translate("MainWindow", "Andres Acevedo, Cod 55305 "))

    def inicio_adquisicion(self):
        port = self.comboBox.currentText()
        if port:
            try:
                self.serial_connection = serial.Serial(port, baudrate=9600, timeout=1)
                self.serial_connection.write(b'H')  # Envía el carácter 'H' para iniciar el envío de datos desde la STM32
                self.running = True
                self.start_thread()
            except serial.SerialException as e:
                print(f"Error abriendo el puerto serial: {e}")

    
    def detener_adquisicion(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.write(b'A')  # Envía el carácter 'A' para detener el envío de datos
            self.running = False
            self.serial_connection.close()
            print("Adquisición detenida y puerto cerrado.")


    
    def start_thread(self):
        thread = threading.Thread(target=self.actualizar_datos)
        thread.start()

    def actualizar_datos(self):

        
        SENSITIVITY_ACCEL  =   (2.0 / 32768.0)
        SENSITIVITY_GYRO  =    (250.0 / 32768.0)
        SENSITIVITY_MAGN =      (4800.0 / 32768.0)

        while self.running:
            if self.serial_connection.in_waiting > 0:
                try:
                    line = self.serial_connection.readline().decode('utf-8').strip()
                    data = line.split()
                    if len(data) == 10:
                        acel_x = float(data[1])*SENSITIVITY_ACCEL
                        acel_y = float(data[2])*SENSITIVITY_ACCEL
                        acel_z = float(data[3])*SENSITIVITY_ACCEL

                        giros_x = float(data[4])*SENSITIVITY_GYRO
                        giros_y = float(data[5])*SENSITIVITY_GYRO
                        giros_z = float(data[6])*SENSITIVITY_GYRO

                        mag_x = float(data[7])*SENSITIVITY_MAGN
                        mag_y = float(data[8])*SENSITIVITY_MAGN
                        mag_z = float(data[9])*SENSITIVITY_MAGN
                        
                        # Añadir los nuevos datos
                        self.acel_x_dato.append(acel_x)
                        self.acel_y_dato.append(acel_y)
                        self.acel_z_dato.append(acel_z)

                        self.giros_x_dato.append(giros_x)
                        self.giros_y_dato.append(giros_y)
                        self.giros_z_dato.append(giros_z)

                        self.mag_x_dato.append(mag_x)
                        self.mag_y_dato.append(mag_y)
                        self.mag_z_dato.append(mag_z)

                        # Añadir el índice correspondiente
                        self.indices.append(self.index)
                        self.index += 1

                        # Emitir señal para actualizar las gráficas
                        self.update_plot_signal.emit(self.indices, self.acel_x_dato, self.acel_y_dato, self.acel_z_dato, self.giros_x_dato, self.giros_y_dato, self.giros_z_dato, self.mag_x_dato, self.mag_y_dato, self.mag_z_dato)
                
                      
                
                        
                        
                except Exception as e:
                    print(f"Error procesando datos: {e}")

    def actualizar_plots(self, indices, acel_x, acel_y, acel_z, giros_x, giros_y, giros_z, mag_x, mag_y, mag_z):
    # Limpiar las gráficas anteriores
        self.graph_acel_x.clear()
        self.graph_acel_y.clear()
        self.graph_acel_z.clear()

        self.graph_giros_x.clear()
        self.graph_giros_y.clear()
        self.graph_giros_z.clear()

        self.graph_mag_x.clear()
        self.graph_mag_y.clear()
        self.graph_mag_z.clear()
        
        # Graficar acelerómetro
        self.graph_acel_x.plot(acel_x, pen='r')
        self.graph_acel_y.plot(acel_y, pen='g')
        self.graph_acel_z.plot(acel_z, pen='b')

        # Graficar giroscopio
        self.graph_giros_x.plot(giros_x, pen='r')
        self.graph_giros_y.plot(giros_y, pen='g')
        self.graph_giros_z.plot(giros_z, pen='b')

        # Graficar magnetómetro
    # Primera gráfica: X -> mag_x, Y -> mag_z
        self.graph_mag_x.plot(mag_y, mag_z, pen=None, symbol='o', symbolBrush='r')
        
        # Segunda gráfica: X -> mag_x, Y -> mag_z
        self.graph_mag_y.plot(mag_x, mag_z, pen=None, symbol='o', symbolBrush='g')
        
        # Tercera gráfica: X -> mag_x, Y -> mag_z
        self.graph_mag_z.plot(mag_x, mag_y, pen=None, symbol='o', symbolBrush='b')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
