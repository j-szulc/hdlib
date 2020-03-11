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

@listen("a")
def f(e):
	print("Hello")


def handlingFun(pkey, action):

	pcombo = Combo(pkey, currentModifiers)

	pkeyevent = KeyEvent(pkey, action)				
	pcomboevent = ComboEvent(pcombo, action)

	for e in [pkeyevent, pcomboevent]:
		MAP.execute(e)

