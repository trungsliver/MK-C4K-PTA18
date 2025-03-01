from PyQt6 import QtWidgets as qtw
from PyQt6 import uic
import sys 

page = 1
class Main(qtw.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("lesson4.ui", self)
    
                            
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()