import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.op = ""
        self.num_1, self.num_2 = 0.0, 0.0
        self.vbox = QVBoxLayout(self)
        self.font = QFont()
        self.font.setPointSize(16)
        self.setWindowTitle("Калькулятор")
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Ошибка!")
        self.msg.setFont(self.font)
        self.font.setPointSize(24)

        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_thrid = QHBoxLayout()
        self.hbox_forth = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_thrid)
        self.vbox.addLayout(self.hbox_forth)

        self.input = QLineEdit(self)
        self.input.setFont(self.font)
        self.hbox_input.addWidget(self.input)

        for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0"]:
            buttonTemp = QPushButton(i, self)
            buttonTemp.clicked.connect(lambda state, x=i: self._button(x))
            buttonTemp.setFont(self.font)
            if i in ["1", "2", "3"]:
                self.hbox_first.addWidget(buttonTemp)
            elif i in ["4", "5", "6"]:
                self.hbox_second.addWidget(buttonTemp)
            elif i in ["7", "8", "9"]:
                self.hbox_thrid.addWidget(buttonTemp)
            elif i in [".", "0"]:
                self.hbox_forth.addWidget(buttonTemp)


        b_plus = QPushButton("+", self)
        b_plus.clicked.connect(lambda: self._operation("+"))
        b_plus.setFont(self.font)

        b_minus = QPushButton("-", self)
        b_minus.clicked.connect(lambda: self._operation("-"))
        b_minus.setFont(self.font)

        b_divide = QPushButton("/", self)
        b_divide.clicked.connect(lambda: self._operation("/"))
        b_divide.setFont(self.font)

        b_Multiply = QPushButton("*", self)
        b_Multiply.clicked.connect(lambda: self._operation("*"))
        b_Multiply.setFont(self.font)

        b_result = QPushButton("=", self)
        b_result.clicked.connect(self._result)
        b_result.setFont(self.font)

        self.hbox_first.addWidget(b_plus)
        self.hbox_second.addWidget(b_minus)
        self.hbox_thrid.addWidget(b_divide)
        self.hbox_forth.addWidget(b_result)
        self.hbox_forth.addWidget(b_Multiply)


    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)


    def _operation(self, op):
        if self.input.text()=="":
            self.input.setText("")
            self.msg.setText("Пустой ввод!")
            self.msg.exec_()
        else:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")


    def _result(self):
        if self.input.text() == "":
            self.input.setText("")
            self.msg.setText("Пустой ввод!")
            self.msg.exec_()
        elif self.op == "":
            self.input.setText(self.input.text())
        else:
            self.num_2 = float(self.input.text())
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))
            if self.op == "/":
                if self.num_2 == 0:
                    self.input.setText("")
                    self.msg.setText("На ноль делить нельзя!")
                    self.msg.exec_()
                else:
                    self.input.setText(str(self.num_1 / self.num_2))


app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())
