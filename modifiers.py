from keys import nameToKey
from events import Action

allModifersNames = {"lshift","rshift"}
allModifiers = {nameToKey(name) for name in allModifiersNames}

currentModifiers = frozenset()

def updateModifiers(event):
	key = event.pcombo.key
	action = event.action
	if(key in allModifiers):
		if(action = Action.PRESSED):
			currentModifiers |= frozenset({key})	
		elif(action = Action.RELEASED):
			currentModifiers -= frozenset({key})
