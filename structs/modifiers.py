from .events import *

class ModifierSet:

	# tracked = all modifiers that we track the state of
	tracked = None
	current = frozenset()

	def __init__(self, tracked):
		self.tracked = tracked

	def update(self,keyevent):
		# Not really neccessary, as update should only be listening to KeyEvents
		if not isinstance(keyevent,KeyEvent):
			return

		key = keyevent.keyOrCombo
		action = keyevent.action

		if(key in self.tracked):
			if(action == Action.PRESS):
				self.current |= frozenset({key})	
			elif(action == Action.RELEASE):
				self.current -= frozenset({key})
