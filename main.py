#!/usr/bin/python3 -i

#from events import Action, PKeyEvent, PComboEvent
#from keys import codeToPKey
#from combos import PCombo
#from modifiers import currentModifiers, updateModifiers
#from hooks import MAP
from output import *
from events import *
from keys import * 
from combos import *
from modifiers import *
from hooks import *
from input import *

MAP = Map()

listen = MAP.listenCombo
capture = MAP.captureCombo

modifierList = ["shift"]
MODIFIERS = ModifierSet(modifierList)
for m in modifierList:
	(listen(m))(MODIFIERS.update)


#@listen("a")
#def f(e):
#	print("Hello")


def handlingFun(key, action):
	
	combo = Combo(key, MODIFIERS.current)

	keyevent = KeyEvent(key, action)				
	comboevent = ComboEvent(combo, action)

	print(repr(keyevent))

	for e in [keyevent, comboevent]:
		MAP.execute(e)

loop(handlingFun = handlingFun, nOfIterations=100)
