#from keys import nameToKey
#from events import Action
from keys import *
from events import *

allModifiersNames = {"lshift","rshift"}
allModifiers = {nameToKey[name] for name in allModifiersNames}

class ModifierSet:

	tracked = None
	current = frozenset()

	def __init__(self, allModifiers):
		tracked = { PKey.fromSth(m) for m in allModifiers }

	def update(event):
		key = event.key
		action = event.action

		if(key in tracked):
			if(action == Action.PRESS):
				current |= frozenset({key})	
			elif(action == Action.RELEASE):
				current -= frozenset({key})
