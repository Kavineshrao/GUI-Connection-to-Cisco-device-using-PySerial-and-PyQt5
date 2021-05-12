import serial
import serial.tools.list_ports
from time import sleep
from PyQt5 import QtCore, QtWidgets

class connection(object):

    def interface(self, Form):

        Form.setObjectName("Form")
        Form.resize(220, 251)

        self.serial_port_label = QtWidgets.QLabel(Form)
        self.serial_port_label.setGeometry(QtCore.QRect(20, 50, 111, 31))
        self.serial_port_label.setObjectName("serial_port_label")

        self.serial_port = QtWidgets.QComboBox(Form)
        self.serial_port.setGeometry(QtCore.QRect(90, 50, 100, 31))
        self.serial_port.setObjectName("serial_port")

        self.baudrate_label = QtWidgets.QLabel(Form)
        self.baudrate_label.setGeometry(QtCore.QRect(20, 100, 111, 31))
        self.baudrate_label.setObjectName("baudrate_label")

        self.baudrate = QtWidgets.QLineEdit(Form)
        self.baudrate.setGeometry(QtCore.QRect(90, 100, 100, 31 ))
        self.baudrate.setObjectName("baudrate")

        self.connect = QtWidgets.QPushButton(Form)
        self.connect.setGeometry(QtCore.QRect(55, 180, 120, 30))
        self.connect.setObjectName("connect")
        self.connect.clicked.connect(self.connect_to_Cisco)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.serial_port_label.setText(_translate("Form", "Serial Port : "))
        self.baudrate_label.setText(_translate("Form", "BaudRate : "))
        self.connect.setText(_translate("Form", "CONNECT"))
        self.comm()

    def comm(self):

        self.serial_port.addItem("")
        ports = serial.tools.list_ports.comports()
        for p in ports:

            a = str(p) #Changes bytes to string to display serial ports in option
            #print(a)
            b = a.split()[0]
            self.serial_port.addItem(b) #This is where it creates item for the dropdown menu

    def connect_to_Cisco(self):

        comm     = self.serial_port.currentText() #Get com number from the user input from the GUI
        baudrate = self.baudrate.text() #get the baudrate from the user

        ser  = serial.Serial(port = comm, baudrate=baudrate)

        enable         = b'enable' + b'\n'
        ser.write(enable)
        sleep(0.5)

        show_clock = b'show clock' + b'\n'
        ser.write(show_clock)
        sleep(0.5)

        print(ser.read(ser.inWaiting()).decode('utf-8'))

        ser.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = connection()
    ui.interface(Form)
    Form.show()
    sys.exit(app.exec_())
