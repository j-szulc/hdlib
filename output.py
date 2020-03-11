from main import uinput, device
from evdev import ecodes
#from select import select

def output_sync():
	uinput.syn()

def trigger(key, action):
	#select([], [device], [])
	uinput.write(ecodes.EV_KEY, key, action)
	output_sync()
	
