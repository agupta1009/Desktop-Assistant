from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 500)
        MainWindow.setMinimumSize(QtCore.QSize(439, 500))
        MainWindow.setMaximumSize(QtCore.QSize(439, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_body_2 = QtWidgets.QFrame(self.centralwidget)
        self.main_body_2.setGeometry(QtCore.QRect(0, 0, 441, 501))
        self.main_body_2.setStyleSheet("background-color: rgb(30, 31, 48);")
        self.main_body_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_2.setObjectName("main_body_2")
        self.widget = QtWidgets.QWidget(self.main_body_2)
        self.widget.setGeometry(QtCore.QRect(10, 10, 421, 121))
        self.widget.setStyleSheet("QWidget{    \n"
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
        self.widget.setObjectName("widget")
        self.login_response_msg_2 = QtWidgets.QLabel(self.widget)
        self.login_response_msg_2.setGeometry(QtCore.QRect(20, 10, 374, 51))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Lt")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.login_response_msg_2.setFont(font)
        self.login_response_msg_2.setStyleSheet("font: 25 8pt \"Proxima Nova Lt\";")
        self.login_response_msg_2.setAlignment(QtCore.Qt.AlignCenter)
        self.login_response_msg_2.setObjectName("login_response_msg_2")
        self.login_res_ok_btn_2 = QtWidgets.QPushButton(self.widget)
        self.login_res_ok_btn_2.setGeometry(QtCore.QRect(170, 60, 80, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_res_ok_btn_2.sizePolicy().hasHeightForWidth())
        self.login_res_ok_btn_2.setSizePolicy(sizePolicy)
        self.login_res_ok_btn_2.setMinimumSize(QtCore.QSize(80, 50))
        self.login_res_ok_btn_2.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_res_ok_btn_2.setFont(font)
        self.login_res_ok_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_res_ok_btn_2.setStyleSheet(" QPushButton#login_res_ok_btn {\n"
"     background-color: rgb(28, 89, 130);\n"
" }\n"
" QPushButton#login_res_ok_btn:pressed {\n"
"     background-color: RGB(255, 0, 0);     \n"
" }\n"
" QPushButton#login_res_ok_btn:hover {\n"
"     background-color: rgb(127, 179, 213);\n"
" }\n"
"\n"
"")
        self.login_res_ok_btn_2.setObjectName("login_res_ok_btn_2")
        self.widget_3 = QtWidgets.QWidget(self.main_body_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 421, 121))
        self.widget_3.setStyleSheet("QWidget{    \n"
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
        self.widget_3.setObjectName("widget_3")
        self.label_title = QtWidgets.QLabel(self.widget_3)
        self.label_title.setGeometry(QtCore.QRect(30, 10, 371, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.widget_2 = QtWidgets.QWidget(self.main_body_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 140, 421, 351))
        self.widget_2.setStyleSheet("QWidget{    \n"
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
        self.widget_2.setObjectName("widget_2")
        self.profile_icon_frame_3 = QtWidgets.QFrame(self.widget_2)
        self.profile_icon_frame_3.setGeometry(QtCore.QRect(190, 20, 50, 50))
        self.profile_icon_frame_3.setMinimumSize(QtCore.QSize(50, 50))
        self.profile_icon_frame_3.setMaximumSize(QtCore.QSize(50, 50))
        self.profile_icon_frame_3.setStyleSheet("image: url(D://ankush//projects//virtual_assistant//desktop assitant ui//icons//cil-user-follow.png);\n"
"border-radius: 25px;\n"
"background-color: rgb(30, 31, 48);\n"
"border: 2px solid rgb(98, 114, 164);")
        self.profile_icon_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_icon_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_icon_frame_3.setObjectName("profile_icon_frame_3")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(20, 151, 100, 52))
        self.label_7.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_email = QtWidgets.QLabel(self.widget_2)
        self.label_email.setGeometry(QtCore.QRect(20, 151, 100, 52))
        self.label_email.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet("")
        self.label_email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_email.setObjectName("label_email")


        self.username_3 = QtWidgets.QLineEdit(self.widget_2)
        self.username_3.setGeometry(QtCore.QRect(127, 92, 268, 52))
        self.username_3.setMinimumSize(QtCore.QSize(170, 50))
        self.username_3.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.username_3.setStyleSheet("QLineEdit {background-color: rgb(83, 97, 140);}\n"
"QLineEdit:hover {background-color: rgb(98, 114, 164);}\n"
"")
        self.username_3.setAlignment(QtCore.Qt.AlignCenter)
        self.username_3.setObjectName("username_3")
        self.password_3 = QtWidgets.QLineEdit(self.widget_2)
        self.password_3.setGeometry(QtCore.QRect(127, 151, 268, 52))
        self.password_3.setMinimumSize(QtCore.QSize(170, 50))
        self.password_3.setMaximumSize(QtCore.QSize(999, 16777215))
        self.password_3.setStyleSheet("QLineEdit {background-color: rgb(83, 97, 140);}\n"
"QLineEdit:hover {background-color: rgb(98, 114, 164);}\n"
"")
        self.password_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_3.setAlignment(QtCore.Qt.AlignCenter)
        self.password_3.setObjectName("password_3")
        self.enter_email = QtWidgets.QLineEdit(self.widget_2)
        self.enter_email.setGeometry(QtCore.QRect(127, 151, 268, 52))
        self.enter_email.setMinimumSize(QtCore.QSize(170, 50))
        self.enter_email.setMaximumSize(QtCore.QSize(999, 16777215))
        self.enter_email.setStyleSheet("QLineEdit {background-color: rgb(83, 97, 140);}\n"
"QLineEdit:hover {background-color: rgb(98, 114, 164);}\n"
"")
        # self.enter_email.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_email.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_email.setObjectName("enter_email")
        


        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 92, 100, 52))
        self.label_4.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.login_btn_3 = QtWidgets.QPushButton(self.widget_2)
        self.login_btn_3.setEnabled(True)
        self.login_btn_3.setGeometry(QtCore.QRect(120, 250, 200, 50))
        self.login_btn_3.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.login_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn_3.setStyleSheet(" QPushButton#login_btn_2 {\n"
"     background-color: rgb(0, 2, 42 );\n"
" }\n"
" QPushButton#login_btn_2:pressed {\n"
"     background-color: rgb(224, 0, 0);     \n"
" }\n"
" QPushButton#login_btn_2:hover {\n"
"     background-color: rgb(93, 109, 126 );\n"
" }")
        self.login_btn_3.setObjectName("login_btn_3")
        self.login_btn = QtWidgets.QPushButton(self.widget_2)
        self.login_btn.setEnabled(True)
        self.login_btn.setGeometry(QtCore.QRect(120, 250, 200, 50))
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet(" QPushButton#login_btn_2 {\n"
"     background-color: rgb(0, 2, 42 );\n"
" }\n"
" QPushButton#login_btn_2:pressed {\n"
"     background-color: rgb(224, 0, 0);     \n"
" }\n"
" QPushButton#login_btn_2:hover {\n"
"     background-color: rgb(93, 109, 126 );\n"
" }")
        self.login_btn.setObjectName("login_btn")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_response_msg_2.setText(_translate("MainWindow", "Login Response Message"))
        self.login_res_ok_btn_2.setText(_translate("MainWindow", "Ok"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Authentication</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "OTP"))
        self.username_3.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password_3.setPlaceholderText(_translate("MainWindow", "OTP"))
        self.enter_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.label_email.setText(_translate("MainWindow", "Email"))


        self.label_4.setText(_translate("MainWindow", "Username"))
        self.login_btn_3.setText(_translate("MainWindow", "Login"))
        self.login_btn.setText(_translate("MainWindow", "Press Here"))

# import initial_screen_rc


# if __name__ == "__main__":
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         MainWindow = QtWidgets.QMainWindow()
#         ui = Ui_LoginWindow()
#         ui.setupUi(MainWindow)
#         MainWindow.show()
#         sys.exit(app.exec_())
