from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QVBoxLayout
from w2 import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(292, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("AC"))
        self.cButton.setGeometry(QtCore.QRect(10, 70, 61, 61))
        self.cButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.cButton.setObjectName("cButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(80, 70, 30, 61))
        self.plusminusButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.plusminusButton.setObjectName("plusminusButton")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(150, 70, 61, 61))
        self.percentButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.percentButton.setObjectName("percentButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(220, 70, 61, 61))
        self.divideButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.divideButton.setObjectName("divideButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(80, 140, 61, 61))
        self.eightButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.eightButton.setObjectName("eightButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(220, 140, 61, 61))
        self.multiplyButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.multiplyButton.setObjectName("multiplyButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 140, 61, 61))
        self.sevenButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(150, 140, 61, 61))
        self.nineButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(80, 210, 61, 61))
        self.fiveButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.fiveButton.setObjectName("fiveButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(220, 210, 61, 61))
        self.minusButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.minusButton.setObjectName("minusButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 210, 61, 61))
        self.fourButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(150, 210, 61, 61))
        self.sixButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.sixButton.setObjectName("sixButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(80, 280, 61, 61))
        self.twoButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(220, 280, 61, 61))
        self.addButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.addButton.setObjectName("addButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 280, 61, 61))
        self.oneButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(150, 280, 61, 61))
        self.threeButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(220, 350, 61, 61))
        self.equalButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(10, 350, 131, 61))
        self.zeroButton.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(150, 350, 61, 61))
        self.decimalButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.decimalButton.setObjectName("decimalButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(110, 70, 30, 61))
        self.arrowButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")



        self.arrowButton.setObjectName("arrowButton")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 9, 271, 51))
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))
        self.menubar.setObjectName("menubar")
        self.file_menu = self.menubar.addMenu("Калькулятор комуналки")
        self.open_window_action = QAction("Відкрити нове вікно", MainWindow)
        self.open_window_action.triggered.connect(self.open_n_window)
        self.file_menu.addAction(self.open_window_action)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_n_window(self):
        Form.show()
        MainWindow.hide()


    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def math_it(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:self.outputLabel.setText(f'-{screen}')


    def dot_it(self):
        screen = self.outputLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')
    def press_it(self, pressed):
        if pressed == "AC":
            self.outputLabel.setText("0")
        else:
            #Check to see if starts with 0 and delete 0
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.cButton.setText(_translate("MainWindow", "AC"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.divideButton.setText(_translate("MainWindow", "÷"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.eightButton.setShortcut(_translate("MainWindow", "8"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.multiplyButton.setShortcut(_translate("MainWindow", "*, X"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.sevenButton.setShortcut(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.nineButton.setShortcut(_translate("MainWindow", "9"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fiveButton.setShortcut(_translate("MainWindow", "5"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.minusButton.setShortcut(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fourButton.setShortcut(_translate("MainWindow", "4"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.sixButton.setShortcut(_translate("MainWindow", "6"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.twoButton.setShortcut(_translate("MainWindow", "2"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.addButton.setShortcut(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.oneButton.setShortcut(_translate("MainWindow", "1"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.threeButton.setShortcut(_translate("MainWindow", "3"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.equalButton.setShortcut(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.zeroButton.setShortcut(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.decimalButton.setShortcut(_translate("MainWindow", "."))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.outputLabel.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Form = QtWidgets.QWidget()
    ui2 = Ui_Form()
    ui2.setupUi(Form)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

