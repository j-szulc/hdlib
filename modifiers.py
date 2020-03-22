#from keys import nameToKey
#from events import Action
from keys import *
from events import *

class ModifierSet:

	tracked = None
	current = frozenset()

	def __init__(self, allModifiers):
		tracked = { Key.fromSth(m) for m in allModifiers }

	def update(self,event):
		key = event.key
		action = event.action

		if(key in tracked):
			if(action == Action.PRESS):
				current |= frozenset({key})	
			elif(action == Action.RELEASE):
				current -= frozenset({key2})
