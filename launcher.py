import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow,
                             QPushButton, QTabWidget, QVBoxLayout)


class CCLLauncher(QMainWindow):
    def __init__(self, parent=None):
        super(CCLLauncher, self).__init__(parent)

        self.doSomething("argument")

    def doSomething(self, text):
        print(text)


        print(self)





if __name__ == "__main__":
    app = QApplication([])
    window = CCLLauncher()
    window.show()
    sys.exit(app.exec_())
