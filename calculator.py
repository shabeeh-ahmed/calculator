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
        self.o0.setObjectName('sh')
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
        self.mul = QPushButton('x')
        self.div = QPushButton('÷')
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

        #gave grid for calc
        self.grid = QGridLayout()
        self.grid.addWidget(self.o0,4,1)
        self.grid.addWidget(self.odot,4,2)
        self.grid.addWidget(self.o1, 3, 0)
        self.grid.addWidget(self.o2, 3, 1)
        self.grid.addWidget(self.o3, 3, 2)
        self.grid.addWidget(self.o4, 2, 0)
        self.grid.addWidget(self.o5, 2, 1)
        self.grid.addWidget(self.o6, 2, 2)
        self.grid.addWidget(self.o7, 1, 0)
        self.grid.addWidget(self.o8, 1, 1)
        self.grid.addWidget(self.o9, 1,2)
        self.grid.addWidget(self.c,0,0)
        self.grid.addWidget(self.backspace,0,1)
        #for sign

        self.grid.addWidget(self.eq,4,4)
        self.grid.addWidget(self.div,0,4)
        self.grid.addWidget(self.mul, 1, 4)
        self.grid.addWidget(self.minus, 2, 4)
        self.grid.addWidget(self.plus, 3, 4)
        self.grid.addWidget(self.perc,4,0)



        box.addLayout(self.grid)

        self.setLayout(box)

    def zero(self):
        if any(op in self.x for op in ['+', '-', '*', '/']):
            self.x += '0'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='0'
            self.output.setText(self.x)
            self.result = True

    def one(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '1'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='1'
            self.output.setText(self.x)
            self.result = True

    def two(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '2'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='2'
            self.output.setText(self.x)
            self.result = True

    def three(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '3'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='3'
            self.output.setText(self.x)
            self.result = True

    def four(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '4'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='4'
            self.output.setText(self.x)
            self.result = True
    def five(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '5'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='5'
            self.output.setText(self.x)
            self.result = True
    def six(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '6'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='6'
            self.output.setText(self.x)
            self.result = True

    def seven(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '7'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='7'
            self.output.setText(self.x)
            self.result = True

    def eight(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '8'
            self.output.setText(self.x)
        else:
            self.x=''
            self.x+='8'
            self.output.setText(self.x)
            self.result = True



    def nine(self):
        if any(op in self.x for op in ['+', '-', '*', '/']) or self.result:
            self.x += '8'
            self.output.setText(self.x)
        else:
            self.x = ''
            self.x += '8'
            self.output.setText(self.x)
            self.result=True



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



    #sign

    def add(self):
        if not self.x:
            return
        if self.x[-1] in ['+', '-', '*', '/']:
            # If it is, slice off the last character ([:-1]) and add the new '+'
            self.x = self.x[:-1] + '+'
        else:
            # If it is a normal number, just add the '+' normally
            self.x += '+'

        self.sign = '+'
        self.output.setText(self.x)
        self.allow_dot=True

    def equal(self):
        try:
            result = eval(self.x)
            result=str(round(result,2))
            self.result = False
            self.output.setText(result)
            self.x = result

        except SyntaxError:
            pass





window=QApplication([])
app=Calculator()
app.show()
window.exec()