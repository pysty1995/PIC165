import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        quit_button = QtGui.QPushButton('Quit', self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        QtGui.QToolTip.setFont(QtGui.QFont('Times', 10))
        quit_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.setToolTip('Quit Button')
        quit_button.move(50, 50) # int ax, int ay
        self.setGeometry(600, 300, 300, 150) #(self, int ax, int ay, int aw, int ah)
        self.setWindowTitle('Program')
        self.show()
    def closeEvent(self, QCloseEvent):
        reply = QtGui.QMessageBox.question(self, 'Message', 'Are you sure to quit?', QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()