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
        self.o0 = QPushButton('0',self);self.o0.clicked.connect(self.zero)
        self.o00=QPushButton('00',self);self.o00.clicked.connect(self.two_zero)
        self.o1 = QPushButton('1',self);self.o1.clicked.connect(self.one)
        self.o2 = QPushButton('2',self);self.o2.clicked.connect(self.two)
        self.o3 = QPushButton('3',self);self.o3.clicked.connect(self.three)
        self.o4 = QPushButton('4',self);self.o4.clicked.connect(self.four)
        self.o5 = QPushButton('5',self);self.o5.clicked.connect(self.five)
        self.o6 = QPushButton('6',self);self.o6.clicked.connect(self.six)
        self.o7 = QPushButton('7',self);self.o7.clicked.connect(self.seven)
        self.o8 = QPushButton('8',self);self.o8.clicked.connect(self.eight)
        self.o9 = QPushButton('9',self);self.o9.clicked.connect(self.nine)

        self.odot = QPushButton('.',self);self.odot.clicked.connect(self.dot)

        #---------------------------
        #--------sign---------------
        self.plus=QPushButton('+',self);self.plus.clicked.connect(self.add)
        self.minus = QPushButton('-',self);self.minus.clicked.connect(self.substract)
        self.mul = QPushButton('x',self);self.mul.clicked.connect(self.multiply)
        self.div = QPushButton('÷',self);self.div.clicked.connect(self.division)
        self.perc = QPushButton('%',self)
        self.eq = QPushButton('=',self);self.eq.clicked.connect(self.equal)
        self.c=QPushButton('C',self);self.c.clicked.connect(self.clear)
        self.backspace=QPushButton('⌫',self);self.backspace.clicked.connect(self.remove)
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

#-------------------grid position-------------------------------------
        self.grid = QGridLayout()

        x = [self.c, self.perc, self.backspace, self.div, self.o7, self.o8, self.o9, self.mul, self.o4, self.o5,
             self.o6, self.minus, self.o1, self.o2, self.o3, self.plus, self.o00, self.o0, self.odot, self.eq]
        n = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if j == 3:continue
                self.grid.addWidget(x[n], i, j)
                n+=1

        box.addLayout(self.grid)
        self.setLayout(box)

# ----------------------------------------------------------------

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

    # ---------------------------------

    # ------------ sign------------------
    def add(self):
        self.verify_sign('+')
    def substract(self):
        self.verify_sign('-')
    def multiply(self):
        self.verify_sign('*')
    def division(self):
        self.verify_sign('/')

    # ------------ special ------------------
    def dot(self):
        self.verify_special('.')
    def remove(self):
        self.verify_special('⌫')
    def clear(self):
        self.verify_special('c')
    def equal(self):
        self.verify_special('=')

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
                          #operation for ( ⌫,  c , . , = )
    #-----------------------------------------------------------------------------------
    def verify_special(self,symbol):
        if symbol=='⌫':
            if self.x:
                self.x = self.x[:-1]
                self.output.setText(self.x)
        if symbol=='c':
            self.x = ''
            self.output.setText(self.x)
            self.result = True
            self.allow_dot = True
        if symbol=='.':
            if self.allow_dot:
                self.x += '.'
                self.output.setText(self.x)
                self.allow_dot = False
        if symbol=='=':
            try:
                result = eval(self.x)
                result = str(round(result, 2))
                # if int(res)==float(res)==int(res)
                if int(float(result)) == float(result):
                    result = str(int(float(result)))
                else:
                    result = result

                self.result = False
                self.output.setText(result)
                self.x = result

            except ZeroDivisionError:  # handling 0 div error
                self.output.setText('Cannot divide by zero')
            except SyntaxError:
                pass

    #--------------------------------------------------------------------------------

window=QApplication([])
app=Calculator()
app.show()
window.exec()
