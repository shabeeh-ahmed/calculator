from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator project')
        self.setFixedSize(560,890)

        self.x=''
        self.sign=''
        self.y=''

        self.result=True
        self.allow_dot=True

        self.output=QLineEdit()

        self.output.setObjectName('out')
        self.output.setAlignment(Qt.AlignRight)
        self.output.setReadOnly(True)

        #----------number-----------
        self.o0 = QPushButton('0')
        self.o0.clicked.connect(self.zero)
        self.o00=QPushButton('00')
        self.o00.clicked.connect(self.two_zero)
        self.o1 = QPushButton('1')
        self.o1.clicked.connect(self.one)
        self.o2 = QPushButton('2')
        self.o2.clicked.connect(self.two)
        self.o3 = QPushButton('3')
        self.o3.clicked.connect(self.three)
        self.o4 = QPushButton('4')
        self.o4.clicked.connect(self.four)
        self.o5 = QPushButton('5')
        self.o5.clicked.connect(self.five)
        self.o6 = QPushButton('6')
        self.o6.clicked.connect(self.six)
        self.o7 = QPushButton('7')
        self.o7.clicked.connect(self.seven)
        self.o8 = QPushButton('8')
        self.o8.clicked.connect(self.eight)
        self.o9 = QPushButton('9')
        self.o9.clicked.connect(self.nine)
        self.odot = QPushButton('.')
        self.odot.clicked.connect(self.dot)
        #------------------------
        #--------sign---------------
        self.plus=QPushButton('+')
        self.plus.clicked.connect(self.add)
        self.minus = QPushButton('-')
        self.minus.clicked.connect(self.substract)
        self.mul = QPushButton('x')
        self.mul.clicked.connect(self.multiply)
        self.div = QPushButton('÷')
        self.div.clicked.connect(self.division)
        self.perc = QPushButton('%')
        self.eq = QPushButton('=')
        self.eq.clicked.connect(self.equal)

        self.c=QPushButton('C')
        self.c.clicked.connect(self.clear)
        self.backspace=QPushButton('⌫')
        self.backspace.clicked.connect(self.remove)
        #-------------------

        self.design()

    def design(self):
        self.setStyleSheet("""#out{background-color: #f0f0f0;
        border: 2px solid #a0a0a0;
        border-radius: 5px;
        padding: 10px;
        font-size: 24px;
        font-family: 'Courier'; /* Or any digital font you like */
        color: #333333;
        height:110px}
        
        QPushButton {
        background-color: #e5e5e5;
        height:130px;
        border: 1px solid #d0d0d0;
        border-radius: 10px;
        color: #333333;
        font-size: 22px;
        font-weight: bold;
        padding: 15px;
    }
    QPushButton:hover {
        background-color: #d4d4d4;
    }
    QPushButton:pressed {
        background-color: #c0c0c0;
    }
        """)


        box=QVBoxLayout()
        box.addWidget(self.output)
#-------------------grid -------------------------------------
        self.grid = QGridLayout()
        self.grid.addWidget(self.c, 0, 0)
        self.grid.addWidget(self.perc, 0, 1)
        self.grid.addWidget(self.backspace, 0, 2)
        self.grid.addWidget(self.div, 0, 4)

        self.grid.addWidget(self.o7, 1, 0)
        self.grid.addWidget(self.o8, 1, 1)
        self.grid.addWidget(self.o9, 1, 2)
        self.grid.addWidget(self.mul, 1, 4)

        self.grid.addWidget(self.o4, 2, 0)
        self.grid.addWidget(self.o5, 2, 1)
        self.grid.addWidget(self.o6, 2, 2)
        self.grid.addWidget(self.minus, 2, 4)

        self.grid.addWidget(self.o1, 3, 0)
        self.grid.addWidget(self.o2, 3, 1)
        self.grid.addWidget(self.o3, 3, 2)
        self.grid.addWidget(self.plus, 3, 4)

        self.grid.addWidget(self.o00, 4, 0)
        self.grid.addWidget(self.o0,4,1)
        self.grid.addWidget(self.odot,4,2)
        self.grid.addWidget(self.eq, 4, 4)

        box.addLayout(self.grid)
        self.setLayout(box)
# ---------------------- -------------------------------------

    #----------numbers--------------
    def zero(self):
        self.verify_num(0)
    def two_zero(self):#when clear enters two zero wanted one zero
        self.verify_num(00)
    def one(self):
        self.verify_num(1)
    def two(self):
        self.verify_num(2)
    def three(self):
        self.verify_num(3)
    def four(self):
        self.verify_num(4)
    def five(self):
        self.verify_num(5)
    def six(self):
        self.verify_num(6)
    def seven(self):
        self.verify_num(7)
    def eight(self):
        self.verify_num(8)
    def nine(self):
        self.verify_num(9)

    # ----------numbers--------------

    # ------------ sign------------------
    def add(self):
        self.verify_sign('+')
    def substract(self):
        self.verify_sign('-')
    def multiply(self):
        self.verify_sign('*')
    def division(self):
        self.verify_sign('/')

    # ------------ sign------------------


    def dot(self):
        #to do:
        #1)allow single dot before a sign and after a sign
        #2)if no sign there allow one .
        #cleared✅
        if self.allow_dot:
            self.x += '.'
            self.output.setText(self.x)
            self.allow_dot=False

    def remove(self):
        if self.x:
            self.x = self.x[:-1]
            self.output.setText(self.x)


    def clear(self):
        self.x=''
        self.output.setText(self.x)
        self.result=True
        self.allow_dot=True

    def equal(self):
        try:
            result = eval(self.x)
            result=str(round(result,2))
            #if int(res)==float(res)==int(res)
            if int(float(result))==float(result):
                result=str(int(float(result)))
            else:result=result


            self.result = False
            self.output.setText(result)
            self.x = result

        except ZeroDivisionError:#handling 0 div error
            self.output.setText('Cannot divide by zero')
        except SyntaxError:
            pass

    #-----------------------------------------------------------------------------
                            #operation for numbers
    #-----------------------------------------------------------------------------
    def verify_num(self,num):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += str(num)
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+=str(num)
            self.output.setText(self.x)
            self.result = True

    #---------------------------------------------------------------------------------
                                #operation for signs
    # ---------------------------------------------------------------------------------
    def verify_sign(self,sign):
        if not self.x:
            return
        if self.x[-1] in ['+', '-', '*', '/']:
            self.x = self.x[:-1] + str(sign)
        else:
            self.x += str(sign)

        self.sign = str(sign)
        self.output.setText(self.x)
        self.allow_dot=True

    #-----------------------------------------------------------------------------------

window=QApplication([])
app=Calculator()
app.show()
window.exec()