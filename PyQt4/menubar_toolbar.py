import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 600
        self.initUI()
    # Main UI
    def initUI(self):
        #self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        label1 = QtGui.QLabel('Demo PyQt', self)
        label1.move(250, 20)
        #Quit button on toolbar
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        # Open button on toolbar
        open_button = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        open_button.setShortcut('Ctrl+O')
        open_button.setStatusTip('Open')
        open_button.triggered.connect(self.open_file)
        # Save button
        save_button = QtGui.QAction(QtGui.QIcon('save.png'), 'Save', self)
        save_button.setShortcut('Ctrl+S')
        save_button.setStatusTip('Save')
        save_button.triggered.connect(self.save_file)
        # Check box
        check_box = QtGui.QCheckBox('Check box',self)
        check_box.move(1, 60)
        check_box.stateChanged.connect(self.ChangeTitle)

        check_box1 = QtGui.QCheckBox('Button1', self)
        check_box1.move(1, 80)
        check_box1.stateChanged.connect(self.button1)

        check_box2 = QtGui.QCheckBox('Button2', self)
        check_box2.move(1, 100)
        check_box2.stateChanged.connect(self.button2)
        #####################
        self.statusBar()
        # Enclare window:
        zoom_button = QtGui.QAction(QtGui.QIcon('zoom+.png'), 'Zoom +', self)
        zoom_button.setShortcut('Ctrl + +')
        zoom_button.setStatusTip('Zoom out')
        zoom_button.triggered.connect(self.zoom_window_out)
        # Zoom in window:
        zoom_button_in = QtGui.QAction(QtGui.QIcon('zoom-.png'), 'Zoom -', self)
        zoom_button_in.setShortcut('Ctrl + -')
        zoom_button_in.setStatusTip('Zoom in')
        zoom_button_in.triggered.connect(self.zoom_window_in)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(open_button)
        fileMenu.addAction(save_button)
        fileMenu1 = self.menuBar()
        fileMenu1=menubar.addMenu('&Tool')
        fileMenu1.addAction(zoom_button)
        fileMenu1.addAction(zoom_button_in)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(open_button)
        toolbar.addAction(save_button)
        toolbar.addAction(zoom_button)
        toolbar.addAction(zoom_button_in)
        toolbar.addAction(exitAction)


        ####################################
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Main window')
        self.show()

    # Sub-def
    def open_file(self):
        fname = QtGui.QFileDialog.getOpenFileName(self,
                                                  'Open file',
                                                  '/home')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
    def closeEvent(self, QCloseEvent):
        reply = QtGui.QMessageBox.question(self,
                                           'Message',
                                           'Are you sure to quit?',
                                           QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    def zoom_window_out(self):
            self.setGeometry(300, 200, 1200, 1200)
    def zoom_window_in(self):
        self.setGeometry(300, 200, 300, 300)
    def ChangeTitle(self, state):
        if state == QtCore.Qt.Checked:
            print("Pressed")
        else:
            print('Not pressed')
    def button1(self, state):
        if state == QtCore.Qt.Checked:
            print('button 1 was pressed')
        else:
            print('button 1 was released')
    def button2(self, state):
        if state == QtCore.Qt.Checked:
            print('button 2 was pressed')
        else:
            print('button 2 was released')
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()