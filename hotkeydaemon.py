
from .structs.keyboard import *
from .eventmap import *
from .structs.actions import *
from .structs.modifiers import *
from .io.output import *
from .io.input import *

from .keytuples.keytuples import keytuples

class HotkeyDaemon:
	
	# What to execute if nobody wants to capture the event
	# i.e. event is not suppressed by us
	def fallback(self, event):
		self.output.send(event.key(),event.action)	

	def sendall(self, action = Action.RELEASE):
		for key in self.keyboard.keys:
			self.output.send(key,action)

	def __init__(self, keyboard = Keyboard(keytuples), allModifiers = ["shift", "ctrl", "alt", "mod"]):
		self.keyboard = keyboard

		self.output = Output()
		self.eventMap = EventMap(self.fallback)

		self.modifierSet = ModifierSet([self.keyboard.keyFrom(m) for m in allModifiers])
		for m in allModifiers:
			self.listenKey(m,Action.PRESS)(self.modifierSet.update)
			self.listenKey(m,Action.RELEASE)(self.modifierSet.update)

	def __del__(self):
		sendall(Action.RELEASE)

	def handleEvdevEvent(self, eventCode, eventValue):

		key = self.keyboard.keyFrom(eventCode)
		combo = Combo(key, self.modifierSet.current)
		action = Action.fromSth(eventValue)

		keyEvent = KeyEvent(key, action)
		comboEvent = ComboEvent(combo, action)
		
		for event in [keyEvent, comboEvent]:
			self.eventMap.execute(event)


	def run(self, inputDevice = None):
		if inputDevice == None:
			inputDevice = selectDevice()

		loop(inputDevice, self.handleEvdevEvent)
		
		
	def listenKey(self, keySth, actionSth = Action.PRESS, suppress=False):
		key = self.keyboard.keyFrom(keySth)
		action = Action.fromSth(actionSth)

		return self.eventMap.listenEvent(KeyEvent(key,action),suppress)

	def captureKey(self, keySth, actionSth = Action.PRESS): 
		return self.listenKey(keySth,actionSth,True)


	def listenCombo(self, comboSth, actionSth = Action.PRESS, suppress=False):
		combo = self.keyboard.comboFrom(comboSth)
		action = Action.fromSth(actionSth)

		return self.eventMap.listenEvent(ComboEvent(combo,action),suppress)

	def captureCombo(self, comboSth, actionSth = Action.PRESS): 
		return self.listenCombo(comboSth,actionSth,True)

	

