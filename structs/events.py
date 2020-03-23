
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

	def __init__(self, key, action = Action.PRESS):
		self.keyOrCombo = key
		self.action = action

	def key(self):
		return self.keyOrCombo

	# do not stop the event from reaching the system
	# i.e. send it back after proccessing
	suppress = False

# Event occuring when pressing an exact combo
class ComboEvent(Event):

	def __init__(self, combo, action = Action.PRESS):
		self.keyOrCombo = combo
		self.action = action

	def combo(self):
		return self.keyOrCombo
	
	# stop the event from reaching the system 
	# i.e. do not send it back after processing
	suppress = True


