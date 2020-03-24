
from .structs.keyboard import *
from .eventmap import *
from .structs.actions import *
from .structs.modifiers import *
from .io.output import *
from .io.input import *

from evdev import InputDevice

class HotkeyDaemon:

	def sendEvent(self, event):
		self.output.send(event.key(),event.action)	

	def sendAll(self, action):
		for key in self.keyboard.keys:
			self.output.send(key,action)

	def sendKey(self, keySth, actionSth = Action.PRESS):
		self.sendEvent(self.keyEventFrom(keySth, actionSth))

	def keyEventFrom(self, keySth, actionSth = Action.PRESS):
		key = self.keyboard.keyFrom(keySth)
		action = Action.fromSth(actionSth)

		return KeyEvent(key, action)

	def comboEventFrom(self, comboSth, actionSth = Action.PRESS):
		combo = self.keyboard.comboFrom(comboSth)
		action = Action.fromSth(actionSth)

		return ComboEvent(combo, action)

	def __init__(self, keyboard = Keyboard(), allModifiersNames = ["shift", "ctrl", "alt", "mod"]):
		self.keyboard = keyboard

		self.output = Output()

		# Fallback is a function that is executed once nobody captured
		self.eventMap = EventMap(fallback = self.sendEvent)

		self.modifierSet = ModifierSet(tracked = [self.keyboard.keyFrom(m) for m in allModifiersNames])
		# tracked = all modifiers that we track the state of

		for m in self.modifierSet.tracked:
			self.eventMap.listenEvent(KeyEvent(m,Action.PRESS))(self.modifierSet.update)
			self.eventMap.listenEvent(KeyEvent(m,Action.RELEASE))(self.modifierSet.update)


	# handle the event in a format used by the evdev library
	def handleEvdevEvent(self, eventCode, eventValue):

		key = self.keyboard.keyFrom(eventCode)
		combo = Combo(key, self.modifierSet.current)
		action = Action.fromSth(eventValue)

		keyEvent = KeyEvent(key, action)
		comboEvent = ComboEvent(combo, action)
		
		for event in [keyEvent, comboEvent]:
			self.eventMap.execute(event)


	def run(self, inputDevice, stopFlag):
		if stopFlag.isSet():
			return
		try:
			loop(inputDevice, self.handleEvdevEvent, stopFlag)
		finally:
			# Optional
			#self.sendAll(Action.RELEASE)
			pass
	
	def kill(self):
		exit(0)
	#	
	# An ugly list of repeatable functions
	#

	def listenKey(self, keySth, actionSth = Action.PRESS, suppress=False):
		keyevent = self.keyEventFrom(keySth, actionSth)
		return self.eventMap.listenEvent(keyevent,suppress)

	def listenCombo(self, comboSth, actionSth = Action.PRESS, suppress=False):
		comboevent = self.comboEventFrom(comboSth, actionSth)
		return self.eventMap.listenEvent(comboevent,suppress)

	def captureKey(self, keySth, actionSth = Action.PRESS): 
		return self.listenKey(keySth,actionSth,True)

	def captureCombo(self, comboSth, actionSth = Action.PRESS): 
		return self.listenCombo(comboSth,actionSth,True)

	#	
	# An ugly list of repeatable functions
	# for undoing the result of functions 
	# from the previous ugly list of repeatable functions
	#

	def unlistenKey(self, keySth, actionSth = Action.PRESS, suppress=False):
		keyevent = self.keyEventFrom(keySth, actionSth)
		return self.eventMap.unlistenEvent(keyevent,suppress)

	def unlistenCombo(self, comboSth, actionSth = Action.PRESS, suppress=False):
		comboevent = self.comboEventFrom(comboSth, actionSth)
		return self.eventMap.unlistenEvent(comboevent,suppress)

	def uncaptureKey(self, keySth, actionSth = Action.PRESS): 
		return self.unlistenKey(keySth,actionSth,True)

	def uncaptureCombo(self, comboSth, actionSth = Action.PRESS): 
		return self.unlistenCombo(comboSth,actionSth,True)

	

