from evdev import ecodes, InputDevice, list_devices
from select import select
from evdev.uinput import UInput

uinput = UInput()

def output_sync():
	uinput.syn()

def send(key, action):
	uinput.write(ecodes.EV_KEY, key, action)
	output_sync()
	
