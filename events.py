from enum import Enum

class Action(Enum):
	
	PRESSED = 0
	RELEASED = 1
	HELD = 2

class Event:

	combo = None
	action = None
	
	def __init__(self, combo, action):
		self.combo = combo
		self.action = action

