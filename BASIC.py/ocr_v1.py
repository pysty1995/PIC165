#coding:utf-8

"""
CRAVIS-mini sample script "OCR"
scripted by toriihara.shigeru@canon.co.jp

20161109-11:00 鳥井原 バーコードリーダをベースに作成
20170119-11:00 鳥井原 サンプルスクリプトとして提供する前に、各部点検
"""
	
import sys
import signal
import traceback
from datetime import datetime
from multiprocessing import Process

import picamera
import picamera.array
import numpy
import cv2

from cmlib import piLib

class OCR(object):
	#コンストラクタ
	def __init__(self,source='picamera', uid=0, resolution=(400,400), framerate=60):
		#super(OCR, self).__init__()
		#self.parent = parent
		#self.source.title("Cravis_ver1")
		signal.signal(signal.SIGINT, self._raiseSystemExit) #CTRL+Cで安全な終了
		signal.signal(signal.SIGHUP, self._raiseSystemExit) #ターミナルを閉じて〃
		signal.signal(signal.SIGTERM, self._raiseSystemExit) #シャットダウン1で〃
		signal.signal(signal.SIGQUIT, self._raiseSystemExit) #シャットダウン2で〃
		signal.signal(signal.SIGABRT, self._raiseSystemExit) #シャットダウン3で〃
		
		self._source = source
		
		if self._source is 'picamera':
			self._camera = picamera.PiCamera()
			self._camera.resolution = resolution
			self._camera.framerate = framerate
		elif self._source is 'usb':
			self._uid = uid
			self._camera = cv2.VideoCapture(self._uid) #uidはUSBカメラのID、接続した順に0、1、2…になる
			ret = self._camera.set(3, resolution[0]) #width　※非対応解像度だと画像が化ける
			ret = self._camera.set(4, resolution[1]) #height　※非対応解像度だと画像が化ける

		self._ocr = cv2.text.OCRTesseract_create()
		
	#オブジェクトの破棄を明示できる、"with"で宣言するために必要
	def __enter__(self):
		return self
		
	#オブジェクトの破棄を明示できる、"with"で宣言するために必要
	def __exit__(self, type, value, traceback):
		if self._source is 'picamera':
			self._camera.close()
		elif self._source is 'usb':
			self._camera.release()
			cv2.destroyAllWindows()
		
	#メイン処理、カメラから画像取得→文字認識の繰り返し
	def run(self, iteration=None, preview=True, multicore=True):
		print '{0:%Y%m%d-%H%M%S}: start.'.format(datetime.now())
		#self.parent = parent
		if self._source is 'picamera' and preview:
			print "sds"
			self._camera.start_preview(fullscreen = True, window = (30,30) + self._camera.resolution)
		
		imageNo = 0
		while iteration is None or imageNo < iteration:
			now = datetime.now()
			print '{0:%Y%m%d-%H%M%S}.{1:03d}: capture image[{2}]'.format(now,now.microsecond%1000,imageNo),
			if self._source is 'picamera':
				stream = picamera.array.PiRGBArray(self._camera)
				self._camera.capture(stream, format='bgr', use_video_port=True)
				frame = stream.array
			elif self._source is 'usb':
				ret, frame = self._camera.read()
				if preview:
					cv2.imshow('{0}'.format(self._source), frame)
					cv2.waitKey(1)
			image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #グレイスケールに変換
			#~ image = 255 - image #色調反転

			print 'and analysing...'
			if multicore is True:
				Process(target = self._detect, args = (image, imageNo)).start() #OSが複数コアにプロセスを割り振る
			else:
				self._detect(image, imageNo) #シングルコアで実行
			
			imageNo += 1
		
	#文字を認識する
	def _detect(self, image, imageNo):
		text = self._ocr.run(image, 10)
		
		if text is not ' ':
			print '  detected![{0}] >'.format(imageNo), text
			
	#あらゆるユーザ操作で安全な終了へ
	def _raiseSystemExit(self, signal, frame):
		raise SystemExit
		
def main(argv):
	print 'CRAVIS-mini sample script "OCR"'
	print 'scripted by toriihara.shigeru@canon.co.jp'
	
	piLib.GpioInit()
	piLib.ErrorClear() #エラーLED消灯

	with OCR() as ocr:
		try:
			ocr.run(multicore=False)
		except SystemExit:
			pass
		except:
			piLib.OutError() #エラーLED点灯
			traceback.print_exc()
		finally:
			print '\n{0:%Y%m%d-%H%M%S}: finish.'.format(datetime.now())

if __name__ == '__main__':
	sys.exit(main(sys.argv))
