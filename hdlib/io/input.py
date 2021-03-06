from evdev import ecodes, InputDevice, list_devices
from select import select
import asyncio

def selectDevice():
    """Select a device from the list of accessible input devices."""

    devices = [InputDevice(device_fn) for device_fn in reversed(list_devices())]
    if not devices:
        print('eerror: no input devices found (do you have rw permission on /dev/input/*?)')
        exit(1)

    device_format = '{0:<3} {1.fn:<20} {1.name:<35} {1.phys}'
    device_lines = [device_format.format(n, d) for n, d in enumerate(devices)]

    print('ID  {:<20} {:<35} {}'.format('Device', 'Name', 'Phys'))
    print('-' * len(max(device_lines, key=len)))
    print('\n'.join(device_lines))
    print('')

    choice = input('Select device [0-{}]:'.format(len(device_lines) - 1))
    return devices[int(choice)]


def loop(device, handlingFun, stopFlag):
	try:
		device.grab()
	except IOError:
		print("IOError when grabbing device")
		print("Ensure you have write permissions")
		exit(1)
	try:
		asyncio.set_event_loop(asyncio.new_event_loop())
		while not stopFlag.isSet():
			select([device], [], [])
			for event in device.read():
				if event.type == ecodes.EV_KEY:
					handlingFun(event.code, event.value)
	finally:
		device.ungrab()
	
