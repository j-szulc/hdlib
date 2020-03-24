
from .structs.keyboard import *
from .eventmap import *
from .structs.actions import *
from .structs.modifiers import *
from .structs.events import *
from .io.output import *
from .io.input import *

from evdev import InputDevice

class HotkeyDaemon:

	
	def sendKey(self, key, action, outside = False):
		if not outside:
			self.handle(key,action)
		else:
			self.output.send(key,action)

	def sendKeyEvent(self, keyEvent, outside = False):
		self.sendKey(keyEvent.key(),keyEvent.action, outside)

	def sendComboEvent(self, comboEvent, outside = False):
		for m in comboEvent.combo().modifiers:
			self.sendKey(m,comboEvent.action, outside)
		self.sendKey(comboEvent.combo().key,comboEvent.action, outside)

	def __init__(self, keyboard = Keyboard(), allModifiersNames = ["shift", "ctrl", "alt", "mod"]):
		self.keyboard = keyboard

		self.output = Output()

		self.eventMap = EventMap()

		self.modifierSet = ModifierSet(tracked = [self.keyboard.keyFrom(m) for m in allModifiersNames])
		# tracked = all modifiers that we track the state of

		for m in self.modifierSet.tracked:
			self.eventMap.listenEvent(KeyEvent(m,Action.PRESS))(self.modifierSet.update)
			self.eventMap.listenEvent(KeyEvent(m,Action.RELEASE))(self.modifierSet.update)
	
	# A key has been physically pressed/repeated/released or sent from the HotkeyDaemon itself
	# 
	def handle(self, key, action):
		combo = Combo(key, self.modifierSet.current)

		keyEvent = KeyEvent(key, action)
		anyKeyEvent = AnyKeyEvent(key, action)
		comboEvent = ComboEvent(combo, action)

		# The order is important
		self.eventMap.execute(lambda: self.sendKeyEvent(keyEvent, True), [anyKeyEvent, keyEvent, comboEvent])

	# The same as self.handle but in a format used by the evdev library
	def handleEvdevEvent(self, eventCode, eventValue):

		key = self.keyboard.keyFrom(eventCode)
		action = Action.fromSth(eventValue)

		self.handle(key,action)


	def run(self, inputDevice, stopFlag):
		if stopFlag.isSet():
			return
		try:
			loop(inputDevice, self.handleEvdevEvent, stopFlag)
		finally:
			# Optional
			#self.sendAll(Action.RELEASE)
			pass

	

