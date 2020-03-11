#!/usr/bin/python3 -i

from ioio.output import *
from structs.events import *
from structs.keys import * 
from structs.combos import *
from structs.modifiers import *
from hooks import *
from ioio.input import *

MAP = Map()

listen = MAP.listenCombo
capture = MAP.captureCombo

modifierList = ["lshift","rshift"]
MODIFIERS = ModifierSet(modifierList)
for m in modifierList:
	(listen(m))(MODIFIERS.update)


@listen("a")
def f(e):
	print("Hello")


def handlingFun(pkey, action):

	pcombo = Combo(pkey, MODIFIERS.current)

	pkeyevent = KeyEvent(pkey, action)				
	pcomboevent = ComboEvent(pcombo, action)

	for e in [pkeyevent, pcomboevent]:
		MAP.execute(e)

loop(handlingFun = handlingFun)
