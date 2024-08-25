import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import serial
import threading


class Ui_MainWindow(QtWidgets.QMainWindow):
    update_plot_signal = QtCore.pyqtSignal(list, list, list, list, list, list, list, list, list, list)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Variables para almacenar datos durante el temporizador
        self.timer_acel_x = []
        self.timer_acel_y = []
        self.timer_acel_z = []

        self.timer_giros_x = []
        self.timer_giros_y = []
        self.timer_giros_z = []

        self.timer_mag_x = []
        self.timer_mag_y = []
        self.timer_mag_z = []

        self.indices = []
        self.index = 0
        
        # Conectar la señal para actualizar las gráficas
        self.update_plot_signal.connect(self.actualizar_plots)
        
        # Inicializar temporizador
        self.timer_count = 30
        self.qtimer = QtCore.QTimer(self)  

        
        # Botones
        self.pushButton.clicked.connect(self.inicio_adquisicion)
        self.pushButton_2.clicked.connect(self.detener_adquisicion)
        self.REED.clicked.connect(lambda: self.mostrar_graficas("acelerometro"))
        self.REED_2.clicked.connect(lambda: self.mostrar_graficas("giroscopio"))
        self.REED_3.clicked.connect(lambda: self.mostrar_graficas("magnetometro"))
        self.pushButton_3.clicked.connect(lambda: print("Button clicked!"))


        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 490, 421, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 190, 91, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 190, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 490, 421, 311))
        self.graphicsView.setObjectName("graphicsView")
        
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(630, 160, 431, 301))
        self.graphicsView_2.setObjectName("graphicsView_2")
        
        
        self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(190, 160, 421, 301))
        self.graphicsView_3.setObjectName("graphicsView_3")
        
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 140, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 140, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 470, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 260, 61, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.REED = QtWidgets.QPushButton(self.centralwidget)
        self.REED.setGeometry(QtCore.QRect(30, 340, 131, 21))
        self.REED.setObjectName("REED")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(500, 50, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(500, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 20, 181, 101))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("TALLER1\IMAGENES\ecci.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(260, 90, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(260, 50, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(390, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(410, 30, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(610, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.graphicsView_4 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(630, 490, 431, 311))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 310, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.REED_2 = QtWidgets.QPushButton(self.centralwidget)
        self.REED_2.setGeometry(QtCore.QRect(30, 370, 131, 21))
        self.REED_2.setObjectName("REED_2")
        self.REED_3 = QtWidgets.QPushButton(self.centralwidget)
        self.REED_3.setGeometry(QtCore.QRect(30, 400, 131, 21))
        self.REED_3.setObjectName("REED_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 470, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 530, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(115, 530, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 500, 141, 21))
        self.pushButton_3.setObjectName("pushButton_3")

        # Objeto STATE
        self.STATE = QtWidgets.QLabel(self.centralwidget)
        self.STATE.setGeometry(QtCore.QRect(40, 550, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.STATE.setFont(font)
        self.STATE.setText("")
        self.STATE.setObjectName("STATE")


        # Objeto timer_label para mostrar la cuenta regresiva
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(90, 530, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timer_label.setFont(font)
        self.timer_label.setText("")
        self.timer_label.setObjectName("timer_label")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3.clicked.connect(self.start_timer)
        self.time_remaining = 30
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Taller1.2"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "COM4"))
        self.label.setText(_translate("MainWindow", "PORT"))
        self.label_2.setText(_translate("MainWindow", "X  GRAPH"))
        self.label_3.setText(_translate("MainWindow", "Y  GRAPH"))
        self.label_4.setText(_translate("MainWindow", "Z  GRAPH"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.REED.setText(_translate("MainWindow", "ACCELEROMETER"))
        self.label_21.setText(_translate("MainWindow", "Adriana Patricia Bolivar Bolivar"))
        self.label_22.setText(_translate("MainWindow", "Alex Andrés Acevedo Mora"))
        self.label_20.setText(_translate("MainWindow", "Valentina Elizabeth Rubiano Avendaño"))
        self.label_12.setText(_translate("MainWindow", "Andrés Felipe Romero Medina"))
        self.label_13.setText(_translate("MainWindow", "Nicolas Mejia Muñoz"))
        self.label_14.setText(_translate("MainWindow", "Algoritmos de Robótica  II"))
        self.label_15.setText(_translate("MainWindow", "Ingeniería Mecatrónica"))
        self.label_16.setText(_translate("MainWindow", "2024 - 2"))
        self.label_5.setText(_translate("MainWindow", "SENSOR"))
        self.REED_2.setText(_translate("MainWindow", "GYROSCOPE"))
        self.REED_3.setText(_translate("MainWindow", "MAGNETOMETER"))
        self.label_6.setText(_translate("MainWindow", "CALIBRATION"))
        self.label_7.setText(_translate("MainWindow", "TIMER"))
        self.label_9.setText(_translate("MainWindow", "s"))
        self.pushButton_3.setText(_translate("MainWindow", "START"))

    def start_timer(self):
        print("Timer started")
        self.STATE.setText("LOADING")
        self.STATE.setStyleSheet("color: orange;")
        self.timer_count = 30

        # Limpiar listas de datos previos
        self.timer_acel_x.clear()
        self.timer_acel_y.clear()
        self.timer_acel_z.clear()
        self.timer_giros_x.clear()
        self.timer_giros_y.clear()
        self.timer_giros_z.clear()
        self.timer_mag_x.clear()
        self.timer_mag_y.clear()
        self.timer_mag_z.clear()
        self.indices.clear()

        # Iniciar la adquisición de datos
        self.running = True
        self.start_thread()

        self.qtimer.timeout.connect(self.update_timer)
        self.qtimer.start(1000)  # Actualizar cada 1 segundo

    def update_timer(self):
        if self.timer_count > 0:
            self.timer_label.setText(str(self.timer_count))
            self.timer_count -= 1
        else:
            self.qtimer.stop()
            self.STATE.setText("DONE")
            self.STATE.setStyleSheet("color: green;")
            self.timer_label.setText("0")
            self.running = False  # Detener la adquisición de datos
            print("Timer finished")

    def inicio_adquisicion(self):
        port = self.comboBox.currentText()
        if port:
            try:
                self.serial_connection = serial.Serial(port, baudrate=9600, timeout=1)
                self.serial_connection.write(b'H')
                self.running = True
                self.start_thread()
            except serial.SerialException as e:
                print(f"Error abriendo el puerto serial: {e}")

    def detener_adquisicion(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.write(b'A')
            self.running = False
            self.serial_connection.close()
            print("Adquisición detenida y puerto cerrado.")

    def start_thread(self):
        thread = threading.Thread(target=self.actualizar_datos)
        thread.start()

    def actualizar_datos(self):
        SENSITIVITY_ACCEL = (2.0 / 32768.0)
        SENSITIVITY_GYRO = (250.0 / 32768.0)
        SENSITIVITY_MAGN = (4800.0 / 32768.0)

        while self.running:
            if self.serial_connection.in_waiting > 0:
                try:
                    line = self.serial_connection.readline().decode('utf-8').strip()
                    data = line.split()
                    if len(data) == 10:
                        acel_x = float(data[1]) * SENSITIVITY_ACCEL
                        acel_y = float(data[2]) * SENSITIVITY_ACCEL
                        acel_z = float(data[3]) * SENSITIVITY_ACCEL

                        giros_x = float(data[4]) * SENSITIVITY_GYRO
                        giros_y = float(data[5]) * SENSITIVITY_GYRO
                        giros_z = float(data[6]) * SENSITIVITY_GYRO

                        mag_x = float(data[7]) * SENSITIVITY_MAGN
                        mag_y = float(data[8]) * SENSITIVITY_MAGN
                        mag_z = float(data[9]) * SENSITIVITY_MAGN

                        self.acel_x_dato.append(acel_x)
                        self.acel_y_dato.append(acel_y)
                        self.acel_z_dato.append(acel_z)

                        self.giros_x_dato.append(giros_x)
                        self.giros_y_dato.append(giros_y)
                        self.giros_z_dato.append(giros_z)

                        self.mag_x_dato.append(mag_x)
                        self.mag_y_dato.append(mag_y)
                        self.mag_z_dato.append(mag_z)

                        self.indices.append(self.index)
                        self.index += 1

                        # Emitir señal para actualizar las gráficas
                        self.update_plot_signal.emit(self.indices, self.acel_x_dato, self.acel_y_dato, self.acel_z_dato)
                except Exception as e:
                    print(f"Error procesando datos: {e}")

    def mostrar_graficas(self, sensor):
        if sensor == "acelerometro":
            self.update_plot_signal.emit(self.indices, self.acel_x_dato, self.acel_y_dato, self.acel_z_dato)
        elif sensor == "giroscopio":
            self.update_plot_signal.emit(self.indices, self.giros_x_dato, self.giros_y_dato, self.giros_z_dato)
        elif sensor == "magnetometro":
            self.update_plot_signal.emit(self.indices, self.mag_x_dato, self.mag_y_dato, self.mag_z_dato)

    def actualizar_plots(self, indices, x_dato, y_dato, z_dato):
        self.graphicsView_3.clear()  # Gráfica de X
        self.graphicsView_2.clear()  # Gráfica de Y
        self.graphicsView.clear()    # Gráfica de Z
        self.graphicsView_4.clear()  # Gráfica de Z

        self.graphicsView_3.plot(indices, x_dato, pen='r')  # Gráfica en graphicsView_3 (X)
        self.graphicsView_2.plot(indices, y_dato, pen='g')  # Gráfica en graphicsView_2 (Y)
        self.graphicsView.plot(indices, z_dato, pen='b')    # Gráfica en graphicsView (Z)
        self.graphicsView_4.plot(indices, z_dato, pen='b')  # Gráfica en graphicsView_4 (Z)
    
    def simple_test(self):
        print("Button connection works!")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
