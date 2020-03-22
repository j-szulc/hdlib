#!/usr/bin/python3 -i

from ioio.input import *
from structs.keys import *
from structs.combos import *
from structs.events import *
from structs.modifiers import *
from structs.actions import *
from hooks import *

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

@listen("shift-a")
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

