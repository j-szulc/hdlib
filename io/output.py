from evdev import ecodes, InputDevice, list_devices
from select import select
from evdev.uinput import UInput, UInputError

try:
	uinput = UInput()
except UInputError:
	print("Error when opening /dev/uinput")
	print("Run the script as root")
	exit(1)

def output_sync(uinput):
	uinput.syn()

def send(key, action):
	uinput.write(ecodes.EV_KEY, key, action)
	output_sync(uinput)
	
