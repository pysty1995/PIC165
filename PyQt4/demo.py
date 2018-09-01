import sys
from PyQt4 import QtGui, QtCore
import cv2
import numpy as np
import time
import importlib.util
try:
    importlib.util.find_spec('Rpi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

class Demo(QtGui.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        GPIO.setmode(GPIO.BOARD)
        self.trigger  = 12
        self.ng_return = 11
        GPIO.setup(self.trigger, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ng_return, GPIO.OUTPUT)
        GPIO.output(self.ng_return, GPIO.LOW)
        self.left = 10
        self.top = 10
        self.width = 860
        self.height = 750
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        self.threshold_img = 0
        self.threshold = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.plc_value = 1
        self.lcd = QtGui.QLCDNumber(self)
        self.image_origin = QtGui.QLabel(self)
        self.image_analyzed = QtGui.QLabel(self)
        self.image_to_analyzed = QtGui.QLabel(self)
        self.show_result = QtGui.QLabel(self)
        self.start_row = 100
        self.end_row = 115
        self.start_col = 300
        self.end_col = 185
        self.white = 0
        self.black = 0
        self.show_area = QtGui.QCheckBox('Show Area', self)
        self.show_area_value = 0
        self.is_ok = 0
        self.is_ng = 0
        self.total = 0
        self.product_ok = QtGui.QLabel(self)
        self.product_ng = QtGui.QLabel(self)
        self.product_total = QtGui.QLabel(self)
        self.product_ok.setText(str(self.is_ok))
        self.product_ng.setText(str(self.is_ng))
        self.product_total.setText(str(self.total))
        self.product_ok.move(740, 70)
        self.product_ng.move(740, 85)
        self.product_total.move(750, 100)
        self.time_stamp = QtGui.QLabel(self)
        self.time_stamp.setText(QtCore.QDateTime.currentDateTime().toString(QtCore.Qt.DefaultLocaleShortDate))
        self.time_stamp.move(430, 120)
        self.initUI()
    # Main UI, everything happens here
    def initUI(self):

        vbox = QtGui.QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('setting.png'))
        # Quit button
        quit_button = QtGui.QAction(QtGui.QIcon('exit.png'),
                                    'Exit',
                                    self)
        quit_button.setShortcut('Ctrl+Q')
        quit_button.setStatusTip('Exit application')
        quit_button.triggered.connect(self.close)

        # Auto_mode
        auto_mode = QtGui.QCheckBox('Auto Mode', self)
        auto_mode.move(200, 60)
        auto_mode.setStatusTip('Turn on Auto mode')
        auto_mode.stateChanged.connect(self.auto_mode)

        # PLC signal
        plc_checker = QtGui.QCheckBox('PLC', self)
        plc_checker.move(280, 60)
        plc_checker.setStatusTip('PLC signal')
        plc_checker.stateChanged.connect(self.plc_checker)

        # Video stream
        show_video = QtGui.QCheckBox('Show Online', self)
        show_video.move(120, 60)
        show_video.setStatusTip('Show Video online')
        show_video.stateChanged.connect(self.show_online)

        # Take picture
        take_pic = QtGui.QPushButton('TakePicture', self)
        take_pic.move(320, 60)
        take_pic.setStatusTip('Take picture')
        take_pic.clicked.connect(self.take_picture)

        # Show Status
        show_status = QtGui.QLabel('Status:', self)
        show_status.move(430, 60)
        self.show_result.setGeometry(10, 10, 50, 50)
        self.show_result.move(470, 60)

        # Slider to adjust Threshold
        self.threshold.setMinimum(0)
        self.threshold.setMaximum(255)
        self.threshold.setValue(0)
        self.threshold.move(200, 110)
        label_threshold = QtGui.QLabel('Threshold(0-255)', self)
        label_threshold.move(205, 90)
        self.lcd.setGeometry(20, 20, 100, 30)
        self.lcd.setStatusTip('Threshold value')
        self.lcd.move(300, 97)

        # Threshold
        self.threshold.setTickPosition(QtGui.QSlider.TicksAbove)
        self.threshold.setTickInterval(1)
        self.threshold.valueChanged.connect(self.value_threshold)
        self.threshold.valueChanged.connect(self.lcd.display)

        # Display image
        label_origin = QtGui.QLabel('Origin', self)
        label_origin.move(180, 220)
        label_analyzed = QtGui.QLabel('Analyzed', self)
        label_analyzed.move(600, 220)
        label_crop = QtGui.QLabel('Crop IMG', self)
        label_crop.move(180, 560)

        # Load image
        load_image = QtGui.QPushButton('Load Image', self)
        load_image.move(10, 60)
        load_image.clicked.connect(self.loadimage)

        # Area
        self.show_area.move(50, 130)
        self.show_area.stateChanged.connect(self.area_value)
        label_start_row = QtGui.QLabel('Start_Row', self)
        label_start_row.move(50, 150)
        start_row = QtGui.QLineEdit(self)
        start_row.setGeometry(10, 10, 40, 20)
        start_row.move(50, 170)
        start_row.textChanged.connect(self.start_row_value)

        label_end_row = QtGui.QLabel('Start_Col', self)
        label_end_row.move(120, 150)
        end_row = QtGui.QLineEdit(self)
        end_row.setGeometry(10, 10, 40, 20)
        end_row.move(120, 170)
        end_row.textChanged.connect(self.end_row_value)

        label_start_col = QtGui.QLabel('End_Row', self)
        label_start_col.move(190, 150)
        start_col = QtGui.QLineEdit(self)
        start_col.setGeometry(10, 10, 40, 20)
        start_col.move(190, 170)
        start_col.textChanged.connect(self.start_col_value)

        label_end_col = QtGui.QLabel('End_Col', self)
        label_end_col.move(250, 150)
        end_col = QtGui.QLineEdit(self)
        end_col.setGeometry(10, 10, 40, 20)
        end_col.move(250, 170)
        end_col.textChanged.connect(self.end_col_value)

        # Show product:
        ok = QtGui.QLabel('OK:', self)
        ng = QtGui.QLabel('NG:', self)
        total = QtGui.QLabel('Total:', self)
        ok.move(700, 70)
        ng.move(700, 85)
        total.move(700, 100)

        self.product_ok.move(740, 70)
        self.product_ng.move(740, 85)
        self.product_total.move(750, 100)

        # Tool bar
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(quit_button)
        self.statusBar()

        # Menu bar
        menubar= self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(quit_button)



        # init UI
        vbox.addWidget(self.threshold)
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height)
        self.setWindowTitle('Main Window')
        self.show()
    # Sub-def

    def closeEvent(self, QCloseEvent): # Dialog to confirm to quit
        reply = QtGui.QMessageBox.question(self,
                                           'Message',
                                           'Are you sure want to quit?',
                                           QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def auto_mode(self, state): # Auto mode
        if state == QtCore.Qt.Checked:
            print('Auto mode is on')
            self.white = 0
            self.black = 0
            if(self.plc_value == 1):
                if not GPIO.input(self.trigger):
                    frame, img = self.cap.read()
                    if (self.show_area_value == 1):
                        cv2.rectangle(img,
                                      (self.start_row, self.end_row),
                                      (self.start_col, self.end_col),
                                      (0, 255, 0),
                                      1)
                    else:
                        pass
                    cv2.imwrite('capture.png', img)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    thr = cv2.adaptiveThreshold(gray, self.threshold_img,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 7, 1)
                    crop_image = thr[self.end_row:self.end_col,
                                 self.start_row:self.start_col]
                    height = crop_image.shape[0]
                    width = crop_image.shape[1]
                    split = cv2.split(crop_image)
                    data = split[0]
                    for i in range(height):
                        for j in range(width):
                            if data[i][j] == 255:
                                self.black += 1
                            else:
                                self.white += 1

                    if self.white > self.black:
                        self.show_result.setPixmap(QtGui.QPixmap('ok_icon.png'))
                        self.is_ok = self.is_ok + 1
                        self.product_ok.setText(str(self.is_ok))

                    else:
                        self.show_result.setPixmap(QtGui.QPixmap('ng_icon.png'))
                        self.is_ng = self.is_ng + 1
                        self.product_ng.setText(str(self.is_ng))
                    self.total = self.is_ok + self.is_ng
                    self.product_total.setText(str(self.total))
                    cv2.imwrite('analyzed.png', thr)
                    cv2.imwrite('crop.png', crop_image)
                    self.image_origin.setPixmap(QtGui.QPixmap('capture.png'))
                    self.image_origin.setGeometry(100, 100, 400, 300)
                    self.image_origin.move(1, 250)
                    self.image_analyzed.setPixmap(QtGui.QPixmap('analyzed.png'))
                    self.image_analyzed.setGeometry(100, 100, 400, 300)
                    self.image_analyzed.move(430, 250)
                    self.image_to_analyzed.setPixmap(QtGui.QPixmap('crop.png'))
                    self.image_to_analyzed.setGeometry(100, 100, 200, 300)
                    self.image_to_analyzed.move(100, 500)
        else:
            print('Auto mode is off')

    def take_picture(self): # Manual process image
        self.white = 0
        self.black = 0
        print('Take picture')
        frame, img = self.cap.read()
        if(self.show_area_value == 1):
            cv2.rectangle(img,
                      (self.start_row, self.end_row),
                      (self.start_col, self.end_col),
                      (0, 255, 0),
                      1)
        else:
            pass
        cv2.imwrite('capture.png', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thr= cv2.adaptiveThreshold(gray, self.threshold_img,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 7, 1)
        crop_image = thr[self.end_row:self.end_col,
                         self.start_row:self.start_col]
        height = crop_image.shape[0]
        width = crop_image.shape[1]
        split = cv2.split(crop_image)
        data = split[0]
        for i in range(height):
            for j in range(width):
                if data[i][j] == 255:
                    self.black+=1
                else:
                    self.white+=1

        if self.white > self.black:
            self.show_result.setPixmap(QtGui.QPixmap('ok_icon.png'))
            self.is_ok = self.is_ok + 1
            self.product_ok.setText(str(self.is_ok))

        else:
            self.show_result.setPixmap(QtGui.QPixmap('ng_icon.png'))
            self.is_ng = self.is_ng + 1
            self.product_ng.setText(str(self.is_ng))
        self.total = self.is_ok + self.is_ng
        self.product_total.setText(str(self.total))
        cv2.imwrite('analyzed.png', thr)
        cv2.imwrite('crop.png', crop_image)
        self.image_origin.setPixmap(QtGui.QPixmap('capture.png'))
        self.image_origin.setGeometry(100, 100, 400, 300)
        self.image_origin.move(1, 250)
        self.image_analyzed.setPixmap(QtGui.QPixmap('analyzed.png'))
        self.image_analyzed.setGeometry(100, 100, 400, 300)
        self.image_analyzed.move(430, 250)
        self.image_to_analyzed.setPixmap(QtGui.QPixmap('crop.png'))
        self.image_to_analyzed.setGeometry(100, 100, 200, 300)
        self.image_to_analyzed.move(100, 500)

    def value_threshold(self):
        self.threshold_img = self.threshold.value()

    def plc_checker(self, state):
        if state == QtCore.Qt.Checked:
            print('Debug with PLC is ON')
            self.plc_value = 1
        else:
            print('Debug with PLC is OFF')
            self.plc_value = 0

    def take_pic(self):
        if not GPIO.input(self.trigger):
            print('Falling edge')
        else:
            print('Rising edge')

    def start_row_value(self, text):
        self.start_row = int(text)

    def end_row_value(self, text):
        self.end_row = int(text)

    def start_col_value(self, text):
        self.start_col = int(text)

    def end_col_value(self, text):
        self.end_col = int(text)
        print(self.start_col, self.end_col,
              self.start_col, self.end_col)

    def area_value(self, state):
        if state == QtCore.Qt.Checked:
            self.show_area_value = 1
        else:
            self.show_area_value = 0
    def show_online(self, state):
        if state == QtCore.Qt.Checked:
            print('Show Video is on')
        else:
            print('Show Video is off')

    def loadimage(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Choose image', '.',
                                                     'Images (*.png *.xpm *.jpg *.bmp *.gif) ')
        if filename:
            image = QtGui.QImage(filename)
            if image.isNull():
                popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                          'Image load error',
                                          'Could not load image',
                                          QtGui.QMessageBox.Ok,
                                          self)
                popup.show()
            else:
                self.white = 0
                self.black = 0
                image.save('capture.png')
                img = cv2.imread('capture.png', 1)
                if (self.show_area_value == 1):
                    cv2.rectangle(img,
                                  (self.start_row, self.end_row),
                                  (self.start_col, self.end_col),
                                  (0, 255, 0),
                                  1)
                else:
                    pass

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                thr = cv2.adaptiveThreshold(gray, self.threshold_img,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 7, 1)
                crop_image = thr[self.end_row:self.end_col,
                             self.start_row:self.start_col]
                height = crop_image.shape[0]
                width = crop_image.shape[1]
                split = cv2.split(crop_image)
                data = split[0]
                for i in range(height):
                    for j in range(width):
                        if data[i][j] == 255:
                            self.black += 1
                        else:
                            self.white += 1
                if self.white > self.black:
                    self.show_result.setPixmap(QtGui.QPixmap('ok_icon.png'))
                    self.is_ok = self.is_ok + 1
                    self.product_ok.setText(str(self.is_ok))

                else:
                    self.show_result.setPixmap(QtGui.QPixmap('ng_icon.png'))
                    self.is_ng = self.is_ng + 1
                    self.product_ng.setText(str(self.is_ng))
                self.total = self.is_ok + self.is_ng
                self.product_total.setText(str(self.total))
                cv2.imwrite('analyzed.png', thr)
                cv2.imwrite('crop.png', crop_image)
                self.image_origin.setPixmap(QtGui.QPixmap('capture.png'))
                self.image_origin.setGeometry(100, 100, 400, 300)
                self.image_origin.move(1, 250)
                self.image_analyzed.setPixmap(QtGui.QPixmap('analyzed.png'))
                self.image_analyzed.setGeometry(100, 100, 400, 300)
                self.image_analyzed.move(430, 250)
                self.image_to_analyzed.setPixmap(QtGui.QPixmap('crop.png'))
                self.image_to_analyzed.setGeometry(100, 100, 200, 300)
                self.image_to_analyzed.move(100, 500)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Demo()
    sys.exit(app.exec_())

if __name__ == '__main__': # run point
    main()
