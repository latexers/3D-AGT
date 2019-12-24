import sys
from PyQt5.QtWidgets import QApplication
from GUI import mainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())