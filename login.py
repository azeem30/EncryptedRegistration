import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet

class Ui_login(object):
    def setupUi(self, login):
        self.conn = sqlite3.connect("mydatabase.sqlite")
        self.cursor = self.conn.cursor()
        login.setObjectName("login")
        login.resize(353, 315)
        self.log_pass = QtWidgets.QLineEdit(login)
        self.log_pass.setGeometry(QtCore.QRect(135, 85, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.log_pass.setFont(font)
        self.log_pass.setStyleSheet("color: rgb(0, 0, 0);\n border-radius: 5px;")
        self.log_pass.setText("")
        self.log_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_pass.setObjectName("log_pass")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(50, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.log_user = QtWidgets.QLineEdit(login)
        self.log_user.setGeometry(QtCore.QRect(135, 55, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.log_user.setFont(font)
        self.log_user.setStyleSheet("color: rgb(0, 0, 0);\n border-radius: 5px;")
        self.log_user.setObjectName("log_user")
        self.message = QtWidgets.QLabel(login)
        self.message.setGeometry(QtCore.QRect(50, 140, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setStyleSheet("color: rgb(255, 0, 0);")
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.login_button = QtWidgets.QPushButton(login, clicked=self.check_user)
        self.login_button.setGeometry(QtCore.QRect(250, 280, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.login_button.setObjectName("login_button")
        self.login_Signup = QtWidgets.QPushButton(login, clicked=self.open_sign)
        self.login_Signup.setGeometry(QtCore.QRect(10, 280, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_Signup.setFont(font)
        self.login_Signup.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.login_Signup.setObjectName("login_Signup")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.label_2.setText(_translate("login", "Password"))
        self.label.setText(_translate("login", "Username"))
        self.login_button.setText(_translate("login", "LOGIN"))
        self.login_Signup.setText(_translate("login", "SIGNUP"))

    def open_sign(self):
        import signup
        self.sign_win = QtWidgets.QWidget()
        self.sign_ui = signup.Ui_SignUp()
        self.sign_ui.setupUi(self.sign_win)
        self.sign_win.show()

    def check_user(self):
        try:
            with open('key_text.key', 'rb') as file:
                self.key = file.read()
                self.fernet_key = Fernet(self.key)
            self.entered_user = self.log_user.text()
            self.entered_pass = self.log_pass.text()
            query = f'''SELECT PASSWORD FROM USERS WHERE USERNAME = '{self.entered_user}';'''
            result = self.cursor.execute(query)
            self.fetched_password = result.fetchone()[0]
            self.decoded_password = self.fernet_key.decrypt(self.fetched_password).decode()
            if self.decoded_password == self.entered_pass:
                self.message.setStyleSheet("color: rgb(0, 255, 0);")
                self.message.setText("Login Successful!")
            else:
                self.message.setText("Incorrect Password!")
        except Exception as e:
            self.message.setText(str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
