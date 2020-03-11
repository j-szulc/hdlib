from enum import IntEnum
from output import trigger

class Action(IntEnum):
	
	RELEASE = 0
	PRESS = 1
	REPEAT = 2

class Event:

	combo = None
	action = None
	
	def __init__(self, combo, action):
		self.combo = combo
		self.action = action

	def trigger(self):
		pass
