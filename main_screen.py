from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 511)
        MainWindow.setMinimumSize(QtCore.QSize(800, 511))
        MainWindow.setMaximumSize(QtCore.QSize(800, 511))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setGeometry(QtCore.QRect(0, 0, 801, 461))
        self.main_body.setAutoFillBackground(False)
        self.main_body.setStyleSheet("background-color: rgb(30, 31, 48);")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.header = QtWidgets.QFrame(self.main_body)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.header.setStyleSheet("background-color: rgb(56, 58, 89);")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.pushButton_4 = QtWidgets.QPushButton(self.header)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 10, 91, 51))
        self.pushButton_4.setStyleSheet("QPushButton{    \n"
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
" }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.header)
        self.label_6.setGeometry(QtCore.QRect(150, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Lt")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 63 16pt \"Proxima Nova Lt\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(56, 58, 89);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.header)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 91, 51))
        self.pushButton_6.setStyleSheet("QPushButton{    \n"
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
" }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 801, 371))
        self.stackedWidget.setStyleSheet("background-color: rgb(30, 31, 48)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("")
        self.home_page.setObjectName("home_page")
        self.label_title = QtWidgets.QLabel(self.home_page)
        self.label_title.setGeometry(QtCore.QRect(0, 10, 791, 351))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.stackedWidget.addWidget(self.home_page)
        self.accounts_page = QtWidgets.QWidget()
        self.accounts_page.setStyleSheet("")
        self.accounts_page.setObjectName("accounts_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.accounts_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.login_form_frame = QtWidgets.QFrame(self.accounts_page)
        self.login_form_frame.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_form_frame.sizePolicy().hasHeightForWidth())
        self.login_form_frame.setSizePolicy(sizePolicy)
        self.login_form_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.login_form_frame.setMaximumSize(QtCore.QSize(340, 200))
        self.login_form_frame.setStyleSheet("border-radius: 20px;\n"
"")
        self.login_form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_form_frame.setObjectName("login_form_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.login_form_frame)
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.input_fileds_frame = QtWidgets.QFrame(self.login_form_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_fileds_frame.sizePolicy().hasHeightForWidth())
        self.input_fileds_frame.setSizePolicy(sizePolicy)
        self.input_fileds_frame.setStyleSheet("QWidget{    \n"
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
        self.input_fileds_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_fileds_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_fileds_frame.setObjectName("input_fileds_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.input_fileds_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.input_fileds_frame)
        self.label_2.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLabel(self.input_fileds_frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setStyleSheet("border:3px solid  rgb(43, 31, 91);\n"
"border-radius: 10px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.input_fileds_frame)
        self.label_5.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLabel(self.input_fileds_frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 50))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_2.setStyleSheet("border:3px solid  rgb(43, 31, 91);\n"
"border-radius: 10px;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.profile_icon_frame = QtWidgets.QFrame(self.input_fileds_frame)
        self.profile_icon_frame.setMinimumSize(QtCore.QSize(50, 50))
        self.profile_icon_frame.setMaximumSize(QtCore.QSize(50, 50))
        self.profile_icon_frame.setStyleSheet("image: url(D://ankush//projects//virtual_assistant//desktop assitant ui//icons//cil-user-follow.png);\n"
"border-radius: 25px;\n"
"background-color: rgb(30, 31, 48);\n"
"border: 2px solid rgb(98, 114, 164);")
        self.profile_icon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_icon_frame.setObjectName("profile_icon_frame")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.profile_icon_frame)
        self.verticalLayout_8.addWidget(self.input_fileds_frame)
        self.verticalLayout_6.addWidget(self.login_form_frame, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.accounts_page)
        self.speak_page = QtWidgets.QWidget()
        self.speak_page.setStyleSheet("")
        self.speak_page.setObjectName("speak_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.speak_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gif = QtWidgets.QLabel(self.speak_page)
        self.gif.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("D:/ankush/projects/virtual_assistant/desktop assitant ui/gifloader.gif"))
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        self.verticalLayout_5.addWidget(self.gif)
        self.stackedWidget.addWidget(self.speak_page)
        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(0, 440, 801, 71))
        self.footer.setStyleSheet("background-color: rgb(56, 58, 89);")
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.pushButton_3 = QtWidgets.QPushButton(self.footer)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 10, 91, 51))
        self.pushButton_3.setStyleSheet("QPushButton{    \n"
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
" }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.footer)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 91, 51))
        self.pushButton_5.setStyleSheet("QPushButton{    \n"
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
" }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.footer_label = QtWidgets.QLabel(self.footer)
        self.footer_label.setGeometry(QtCore.QRect(170, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Lt")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.footer_label.setFont(font)
        self.footer_label.setStyleSheet("font: 63 16pt \"Proxima Nova Lt\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(56, 58, 89);")
        self.footer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.footer_label.setObjectName("footer_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.label_6.setText(_translate("MainWindow", "Virtual Assistant "))
        self.pushButton_6.setText(_translate("MainWindow", "Account"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p>Virtual Assistant</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "email"))
        self.pushButton_3.setText(_translate("MainWindow", "Speak"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.footer_label.setText(_translate("MainWindow", "Listening... & Computing..."))
# import vu_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
