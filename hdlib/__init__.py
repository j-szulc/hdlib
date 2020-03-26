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
hdThread = None
stopFlag = Flag()

def kill():
	stopFlag.set(True)

def join():
	if hdThread != None:
		hdThread.join()

def run(inputDevice = None, daemon = True):
	if inputDevice == None:
		inputDevice = selectDevice()

	if isinstance(inputDevice, str):
		inputDeviceName = inputDevice
		inputDevice = InputDevice(inputDeviceName)
	
	kill()
	stopFlag.set(False)	

	global hdThread
	hdThread = threading.Thread(daemon = daemon,target = hd.run, args = (inputDevice, stopFlag))
	hdThread.start()

	if not daemon:
		join()

	return hdThread


def send(comboSth, actionSth = "PRESS", outside = False):
	combo = hd.keyboard.comboFrom(comboSth)
	action = Action.fromSth(actionSth)
	comboEvent = ComboEvent(combo, action)

	hd.sendComboEvent(comboEvent, outside)

def pressOnce(comboSth, outside = False):
	send(comboSth,"PRESS", outside)
	send(comboSth,"RELEASE", outside)

# Ugly list of repeatable functions

def listenCombo(comboSth, actionSth = "PRESS"):
	combo = hd.keyboard.comboFrom(comboSth)
	action = Action.fromSth(actionSth)
	comboEvent = ComboEvent(combo, action)

	return hd.eventMap.listenEvent(comboEvent)

def listenKey(keySth, actionSth = "PRESS"):
	key = hd.keyboard.keyFrom(keySth)
	action = Action.fromSth(actionSth)
	keyEvent = KeyEvent(key, action)

	return hd.eventMap.listenEvent(keyEvent)

def listenAnyKey(actionSth = "PRESS"):
	action = Action.fromSth(actionSth)
	anyKeyEvent = AnyKeyEvent(None, action)
	
	return hd.eventMap.listenEvent(anyKeyEvent)

def unlistenCombo(comboSth, actionSth = "PRESS"):
	combo = hd.keyboard.comboFrom(comboSth)
	action = Action.fromSth(actionSth)
	comboEvent = ComboEvent(combo, action)

	return hd.eventMap.unlistenEvent(comboEvent)

def unlistenKey(keySth, actionSth = "PRESS"):
	key = hd.keyboard.keyFrom(keySth)
	action = Action.fromSth(actionSth)
	keyEvent = KeyEvent(key, action)

	return hd.eventMap.unlistenEvent(keyEvent)

def unlistenAnyKey(actionSth = "PRESS"):
	action = Action.fromSth(actionSth)
	anyKeyEvent = AnyKeyEvent(None, action)
	
	return hd.eventMap.unlistenEvent(anyKeyEvent)

listen = listenCombo
unlisten = unlistenCombo


