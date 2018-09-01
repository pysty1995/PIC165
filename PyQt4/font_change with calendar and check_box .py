import sys
from PyQt4 import QtGui, QtCore
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QtGui.QIcon('setting.png'))

        action = QtGui.QAction('Quit', self)
        action.setShortcut('Ctrl+Q')
        action.setStatusTip('Quit')
        action.triggered.connect(self.close_application)

        editor = QtGui.QAction('Editor', self)
        editor.setShortcut('Ctrl+E')
        editor.setStatusTip('Open editor')
        editor.triggered.connect(self.editor_application)

        open_file = QtGui.QAction('Open file', self)
        open_file.setShortcut('Ctrl + 0')
        open_file.setStatusTip('Open Editor')
        open_file.triggered.connect(self.file_open)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(action)
        fileMenu.addAction(editor)

        self.home()
    def home(self):
        button = QtGui.QPushButton('Quit', self)
        button.clicked.connect(self.close_application)
        button.resize(button.minimumSizeHint())
        button.move(0, 100)
        action = QtGui.QAction(QtGui.QIcon('exit.png'), 'QUITTT', self)
        action.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('Quitt')
        self.toolBar.addAction(action)
        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)

        color = QtGui.QColor(0, 0, 0)
        fontColor = QtGui.QAction('Choose background color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)
        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(300, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.button = QtGui.QPushButton('Download', self)
        self.button.move(200, 120)
        self.button.clicked.connect(self.download)

        self.styleChoice = QtGui.QLabel('Window Vista', self)
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('cleanlook')
        comboBox.addItem('vista')
        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        cal = QtGui.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)
        self.show()
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, '...',
                                            'Are you really want to quit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No )
        if choice == QtGui.QMessageBox.Yes:
            print("quitt")
        else:
            pass
    def editor_application(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        file = open(name, 'r')
        self.editor_application()
        with file:
            text = file.read()
            self.textEdit.setText(text)
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background: %s}' % color.name())
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
run()