
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_takeinput(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_body_2 = QtWidgets.QFrame(self.centralwidget)
        self.main_body_2.setGeometry(QtCore.QRect(0, 0, 781, 321))
        self.main_body_2.setStyleSheet("background-color: rgb(30, 31, 48);")
        self.main_body_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_2.setObjectName("main_body_2")
        self.input_body = QtWidgets.QWidget(self.main_body_2)
        self.input_body.setGeometry(QtCore.QRect(10, 140, 751, 171))
        self.input_body.setStyleSheet("QWidget{    \n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(98, 114, 164);\n"
"    border-radius: 20px;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid rgb(30, 31, 48);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(30, 31, 48);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(206, 206, 206);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(254, 121, 199);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
" QPushButton:hover {\n"
"    border: 2px solid rgb(254, 121, 199);\n"
"    background-color: rgb(255, 162, 255);\n"
"}\n"
" QPushButton:pressed {\n"
"    background-color: rgb(229, 109, 181);\n"
" }\n"
"QLabel{\n"
"    border:3px solid  rgb(30, 31, 48);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(50, 50, 80);\n"
"}\n"
"QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(0, 93, 159);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    background:rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"")
        self.input_body.setObjectName("input_body")
        self.input = QtWidgets.QLineEdit(self.input_body)
        self.input.setGeometry(QtCore.QRect(50, 20, 651, 52))
        self.input.setMinimumSize(QtCore.QSize(170, 50))
        self.input.setMaximumSize(QtCore.QSize(999, 16777215))
        self.input.setStyleSheet("QLineEdit {background-color: rgb(83, 97, 140);}\n"
"QLineEdit:hover {background-color: rgb(98, 114, 164);}\n"
"")
        self.input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setObjectName("input")
        self.enter_btn = QtWidgets.QPushButton(self.input_body)
        self.enter_btn.setEnabled(True)
        self.enter_btn.setGeometry(QtCore.QRect(280, 100, 200, 50))
        self.enter_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.enter_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.enter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_btn.setStyleSheet(" QPushButton#login_btn_2 {\n"
"     background-color: rgb(0, 2, 42 );\n"
" }\n"
" QPushButton#login_btn_2:pressed {\n"
"     background-color: rgb(224, 0, 0);     \n"
" }\n"
" QPushButton#login_btn_2:hover {\n"
"     background-color: rgb(93, 109, 126 );\n"
" }")
        self.enter_btn.setObjectName("enter_btn")
        self.title_body = QtWidgets.QWidget(self.main_body_2)
        self.title_body.setGeometry(QtCore.QRect(10, 10, 751, 121))
        self.title_body.setStyleSheet("QWidget{    \n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(98, 114, 164);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(254, 121, 199);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
" QPushButton:hover {\n"
"    border: 2px solid rgb(254, 121, 199);\n"
"    background-color: rgb(255, 162, 255);\n"
"}\n"
" QPushButton:pressed {\n"
"    background-color: rgb(229, 109, 181);\n"
" }\n"
"\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.title_body.setObjectName("title_body")
        self.label_title = QtWidgets.QLabel(self.title_body)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 731, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input.setText(_translate("MainWindow", "Enter Text"))
        self.input.setPlaceholderText(_translate("MainWindow", "Enter Text"))
        self.enter_btn.setText(_translate("MainWindow", "Enter"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Take Input</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_takeinput()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

