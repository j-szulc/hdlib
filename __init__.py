from .io.input import *
from .io.output import *
from .hotkeydaemon import *
from evdev import InputDevice
from .helpers import *

import threading

class Flag:
	
	def __init__(self):
		self.value = False

	def set(self, newValue = True):
		self.value = newValue

	def isSet(self):
		return self.value
	
# global variables
hd = HotkeyDaemon()
stopFlag = Flag()

def run(inputDevice = None):
	if inputDevice == None:
		inputDevice = selectDevice()

	if isinstance(inputDevice, str):
		inputDeviceName = inputDevice
		inputDevice = InputDevice(inputDeviceName)
	
	stopFlag.set(False)
	hd_thread = threading.Thread(daemon=True,target = hd.run, args = (inputDevice, stopFlag))
	hd_thread.start()
	
	return hd_thread

def kill():
	stopFlag.set(True)

listenKey = hd.listenKey
listenCombo = hd.listenCombo
captureKey = hd.captureKey
captureCombo = hd.captureCombo

listen = listenCombo
capture = captureCombo

send = hd.sendKey
