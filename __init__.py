#!/usr/bin/python3 
# usage: ./main.py examples/config.py examples/config2.py ...
from .io.input import *
from .structs.keys import *
from .structs.combos import *
from .structs.events import *
from .structs.modifiers import *
from .structs.actions import *
from .hooks import *

import threading
from evdev import InputDevice

MAP = Map()

listen = MAP.listenCombo
capture = MAP.captureCombo
listenKey = MAP.listenKey
captureKey = MAP.captureKey

modifierList = ["shift","ctrl","alt","mod"]
MODIFIERS = ModifierSet(modifierList)
for m in modifierList:
	listenKey(m,Action.PRESS)(MODIFIERS.update)
	listenKey(m,Action.RELEASE)(MODIFIERS.update)

def handlingFun(key, action):

	combo = Combo(key, MODIFIERS.current)

	keyevent = KeyEvent(key, action)				
	comboevent = ComboEvent(combo, action)

	for e in [keyevent, comboevent]:
		MAP.execute(e)

def run(device = None):
	if device == None:
		device = selectDevice()
	elif isinstance(device,str):
		device = InputDevice(device)

	thread = threading.Thread(target=loop, kwargs = {'handlingFun': handlingFun, 'device': device, 'nOfIterations': 50})
	thread.start()

	for k in keys:
		k.send(Action.RELEASE)

	return thread
