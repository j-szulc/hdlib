

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



try:
	device.grab()
except IOError:
	print("IOError when grabbing device")
	exit(1)
try:
	for i in range(100):
		select([device], [], [])
		for event in device.read():
			if event.type == ecodes.EV_KEY:
				
				if event.code not in codeToPKey:
					continue
	
				print(event.code,event.value)

				action = Action(int(event.value))
				pkey = codeToPKey[event.code]
				pcombo = PCombo(pkey, currentModifiers)
				
				pkeyevent = PKeyEvent(pkey, action)				
				pcomboevent = PComboEvent(pcombo, action)
				
				WhatToDo(pkeyevent).fallback()
				print(type(pkeyevent)==PKeyEvent)
				#for e in [pkeyevent, pcomboevent]:
				#	MAP[e].execute()

finally:
	device.ungrab()
