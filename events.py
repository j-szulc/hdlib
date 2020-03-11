from enum import IntEnum
#from output import trigger
#from keys import Key
#from combos import Combo
from output import *
from keys import *
from combos import *

class Action(IntEnum):
	
	RELEASE = 0
	PRESS = 1
	REPEAT = 2

# Event occuring when pressing key regardless of modifiers
class PKeyEvent:

	key = None
	action = None
	
	# pass the event back to the system if there's nothing to capture it
	# i.e. trigger it back to the system	
	passthrough = True

	def __init__(self, key, action):
		self.key = key
		self.action = action

	def trigger(self):
		self.key.trigger(self.action)

# Event occuring when pressing exact pcombo
class PComboEvent:

	combo = None
	action = None
	
	# do not trigger it back to the system 
	# any key pressed will invoke both PKeyEvent, PComboEvent
	# and PKeyEvent will trigger it back
	# setting it to true will double every character typed
	passthrough = False

	def __init__(self, combo, action):
		self.combo = combo
		self.action = action

	def trigger(self):
		self.combo.trigger(self.action)

