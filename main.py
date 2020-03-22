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
listenKey = MAP.listenKey
captureKey = MAP.captureKey

modifierList = ["shift"]
MODIFIERS = ModifierSet(modifierList)
for m in modifierList:
	listenKey(m,Action.PRESS)(MODIFIERS.update)
	listenKey(m,Action.RELEASE)(MODIFIERS.update)

@MAP.listenCombo("shift-a")
def f(e):
	print("Hello")


def handlingFun(key, action):
	
	combo = Combo(key, MODIFIERS.current)

	keyevent = KeyEvent(key, action)				
	comboevent = ComboEvent(combo, action)

	for e in [keyevent, comboevent]:
		MAP.execute(e)

loop(handlingFun = handlingFun, nOfIterations=100)

for m in modifierList:
	Key.fromSth(m).send(Action.RELEASE)

