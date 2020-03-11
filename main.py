

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

def f(e):
	print(e)
	print("Testing")

(MAP.captureEvent(KeyEvent("a","PRESS")))(f)

#exit()

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

				action = Action.fromSth(event.value)
				pkey = Key.fromSth(event.code)
				pcombo = Combo(pkey, currentModifiers)
				
				pkeyevent = KeyEvent(pkey, action)				
				pcomboevent = ComboEvent(pcombo, action)
				
				for e in [pkeyevent, pcomboevent]:
					#print(e.passthrough)
					MAP.execute(e)

finally:
	device.ungrab()
