from evdev import ecodes, InputDevice, list_devices
from select import select
from evdev.uinput import UInput, UInputError

class Output:

	def __init__(self):
		try:
			self.uinput = UInput()
		except UInputError:
			print("Error when opening /dev/uinput")
			print("Ensure you have write permissions")
			exit(1)

	def sync(self):
		self.uinput.syn()

	def send(self,key, action):
		self.uinput.write(ecodes.EV_KEY, key.codes[0], int(action))
		self.sync()

	def __del__(self):
		try:
			self.uinput.close()
		except ImportError:
			pass
