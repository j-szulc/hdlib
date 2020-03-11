from enum import IntEnum
#from output import trigger
#from keys import Key
#from combos import Combo
from output import *
from keys import *
from combos import *
from helpers import *

class Action(IntEnum):
	
	RELEASE = 0
	PRESS = 1
	REPEAT = 2

	@staticmethod
	def fromSth(sth):
		if isinstance(sth,int):
			return Action(sth)
		elif isinstance(sth,str):
			return Action[sth.upper()]
		else:
			raise InvalidSth(sth)
		
# Event occuring when pressing key regardless of modifiers
class KeyEvent:

	key = None
	action = None

	def __init__(self, key, action = Action.PRESS):
		self.key = Key.fromSth(key)
		self.action = Action.fromSth(action)

	def expand(self):
		if self.isPhysical():
			return [self]
		else:
			return sum_([KeyEvent(k,action).expand() for k in self.key.expand()],start=[])

	# pass the event back to the system if there's nothing to capture it
	# i.e. trigger it back to the system	
	passthrough = True

	def send(self):
		self.key.send(self.action)

	def __hash__(self):
		return hash((self.key,self.action))

	def __eq__(self,obj):
		return isinstance(obj,KeyEvent) and (self.key, self.action) == (obj.key, obj.action)

	def __str__(self):
		return str(self.key) + " " + str(self.action)

	def __repr__(self):
		return str(self)

	# is Physical Key Event
	def isPhysical(self):
		return self.key.isPhysical()

# The same as KeyEvent but only allows physical keys
class PKeyEvent(KeyEvent):
	pass

# Event occuring when pressing exact pcombo
class ComboEvent:

	combo = None
	action = None

	def __init__(self, combo, action = Action.PRESS):
		self.combo = Combo.fromSth(combo)
		self.action = Action.fromSth(action)
	
	def expand(self):
		if self.isPhysical():
			return [self]
		else:
			return sum_([ComboEvent[c,action].expand() for c in self.combo.expand()], start = [])
	# do not trigger it back to the system 
	# any key pressed will invoke both PKeyEvent, PComboEvent
	# and PKeyEvent will trigger it back
	# setting it to true will double every character typed
	passthrough = False

	def send(self):
		self.combo.send(self.action)

	def __hash__(self):
		return hash((self.combo,self.action))

	def __eq__(self,obj):
		return isinstance(obj,ComboEvent) and (self.combo, self.action) == (obj.combo, obj.action)

	def __str__(self):
		return str(self.combo) + " " + str(self.action)

	def __repr__(self):
		return str(self)

	# is Physical Key Combination Event
	def isPhysical(self):
		return self.combo.isPhysical()

# The same as ComboEvent but only allows physical keys
class PComboEvent(KeyEvent):

	pass

	

