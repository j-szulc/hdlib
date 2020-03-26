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

def run(inputDevice = None, dropPrivileges = False, daemon = True):
	if inputDevice == None:
		inputDevice = selectDevice()

	if isinstance(inputDevice, str):
		inputDeviceName = inputDevice
		inputDevice = InputDevice(inputDeviceName)
	
	stopFlag.set(False)
	hd_thread = threading.Thread(daemon = daemon,target = hd.run, args = (inputDevice, stopFlag))
	hd_thread.start()
	
	if dropPrivileges:
		dropPrivileges()

	if not daemon:
		hd_thread.join()

	return hd_thread

def kill():
	stopFlag.set(True)

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
	key = hd.keyboard.keyFrom(comboSth)
	action = Action.fromSth(actionSth)
	keyEvent = KeyEvent(key, action)

	return hd.eventMap.listenEvent(comboEvent)

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
	key = hd.keyboard.keyFrom(comboSth)
	action = Action.fromSth(actionSth)
	keyEvent = KeyEvent(key, action)

	return hd.eventMap.unlistenEvent(comboEvent)

def unlistenAnyKey(actionSth = "PRESS"):
	action = Action.fromSth(actionSth)
	anyKeyEvent = AnyKeyEvent(None, action)
	
	return hd.eventMap.unlistenEvent(anyKeyEvent)

listen = listenCombo
unlisten = unlistenCombo


