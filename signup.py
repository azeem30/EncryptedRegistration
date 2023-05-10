from cryptography.fernet import Fernet
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        self.conn = sqlite3.connect("mydatabase.sqlite")
        self.cursor = self.conn.cursor()
        SignUp.setObjectName("SignUp")
        SignUp.resize(319, 286)
        self.label = QtWidgets.QLabel(SignUp)
        self.label.setGeometry(QtCore.QRect(35, 35, 91, 20))
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
        self.label_2 = QtWidgets.QLabel(SignUp)
        self.label_2.setGeometry(QtCore.QRect(35, 65, 91, 20))
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
        self.label_3 = QtWidgets.QLabel(SignUp)
        self.label_3.setGeometry(QtCore.QRect(35, 90, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(SignUp)
        self.username.setGeometry(QtCore.QRect(120, 30, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("color: rgb(0, 0, 0);\n border-radius: 5px;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(SignUp)
        self.password.setGeometry(QtCore.QRect(120, 60, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(0, 0, 0);\n border-radius: 5px;")
        self.password.setText("")
        self.password.setObjectName("password")
        self.confirm = QtWidgets.QLineEdit(SignUp)
        self.confirm.setGeometry(QtCore.QRect(120, 105, 160, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("color: rgb(0, 0, 0);\n border-radius: 5px;")
        self.confirm.setObjectName("confirm")
        self.signup_button = QtWidgets.QPushButton(SignUp, clicked=self.get_data)
        self.signup_button.setGeometry(QtCore.QRect(220, 250, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.signup_button.setObjectName("signup_button")
        self.message = QtWidgets.QLabel(SignUp)
        self.message.setGeometry(QtCore.QRect(40, 160, 241, 41))
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
        self.signup_login = QtWidgets.QPushButton(SignUp, clicked=self.open_login)
        self.signup_login.setGeometry(QtCore.QRect(10, 250, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup_login.setFont(font)
        self.signup_login.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.signup_login.setObjectName("signup_login")

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Signup"))
        self.label.setText(_translate("SignUp", "Username"))
        self.label_2.setText(_translate("SignUp", "Password"))
        self.label_3.setText(_translate("SignUp", "Confirm\n"
"Password"))
        self.signup_button.setText(_translate("SignUp", "SIGNUP"))
        self.signup_login.setText(_translate("SignUp", "LOGIN"))

    def get_data(self):
        self.str_username = self.username.text()
        self.str_password = self.password.text()
        self.str_confirm = self.confirm.text()
        if self.str_password == "" or self.str_username == "" or self.str_confirm == "":
            self.message.setText("No field can be empty!")
        elif self.str_password != self.str_confirm:
            self.message.setText("Passwords do not match!")
        else:
            self.create_table()
            self.enc_password = self.encrypted()
            self.insert_data()
            self.message.setStyleSheet("color: rgb(0, 255, 0);")
            self.message.setText("Registered Successfully!")

    def create_table(self):
        try:
            query = '''CREATE TABLE IF NOT EXISTS USERS(
                    USERNAME VARCHAR(100) PRIMARY KEY,
                    PASSWORD BLOB);'''
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            self.message.setText(str(e))

    def insert_data(self):
        try:
            query = f'''INSERT INTO USERS(USERNAME, PASSWORD) VALUES ('{self.str_username}','{self.enc_password.decode()}');'''
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            self.message.setText(str(e))

    def encrypted(self):
        try:
            self.key = Fernet.generate_key()
            self.fernet_key = Fernet(self.key)
            self.enc_string = self.fernet_key.encrypt(self.str_password.encode())
            with open('key_text.key', 'wb') as file:
                file.write(self.key)
        except Exception as e:
            self.message.setText(str(e))
        finally:
            return self.enc_string

    def open_login(self):
        import login
        self.log_win = QtWidgets.QWidget()
        self.log_ui = login.Ui_login()
        self.log_ui.setupUi(self.log_win)
        self.log_win.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QWidget()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())
