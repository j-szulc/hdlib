from structs.keys import *
from structs.events import *

class ModifierSet:

	tracked = None
	current = frozenset()

	def __init__(self, allModifiers):
		self.tracked = { Key.fromSth(m) for m in allModifiers }

	def update(self,keyevent):
		if not isinstance(keyevent,KeyEvent):
			return

		key = keyevent.keyOrCombo
		action = keyevent.action

		if(key in self.tracked):
			if(action == Action.PRESS):
				self.current |= frozenset({key})	
			elif(action == Action.RELEASE):
				self.current -= frozenset({key})
