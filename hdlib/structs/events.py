
from .actions import *


class Event:

	keyOrCombo = None
	action = None

	def __hash__(self):
		return hash((self.keyOrCombo,self.action))

	def __eq__(self,obj):
		return isinstance(obj,type(self)) and (self.keyOrCombo, self.action) == (obj.keyOrCombo, obj.action)

	def __str__(self):
		return str(self.keyOrCombo) + " " + str(self.action)

	def __repr__(self):
		return repr(self.keyOrCombo) + " " + repr(self.action)

# Event occuring when pressing a key regardless of modifiers
class KeyEvent(Event):

	def __init__(self, key, actionSth = Action.PRESS):
		self.keyOrCombo = key
		self.action = Action.fromSth(actionSth)

	def key(self):
		return self.keyOrCombo

	# allow stopping the event from reaching the system
	allowSuppress = True

# Event occuring when pressing an exact combo
class ComboEvent(Event):

	def __init__(self, combo, actionSth = Action.PRESS):
		self.keyOrCombo = combo
		self.action = Action.fromSth(actionSth)

	def combo(self):
		return self.keyOrCombo
	
	# allow stopping the event from reaching the system
	allowSuppress = True

# Event that carries all the information that KeyEvent does
# But is recognized as the same event regardless of what key has been pressed
# Used to listen to every key pressed
class AnyKeyEvent(KeyEvent):

	def __hash__(self):
		return hash(self.action)

	def __eq__(self, obj):
		return isinstance(obj,AnyKeyEvent) and self.action == obj.action
