import hdlib

@hdlib.listenAnyKey("PRESS")
@hdlib.listenAnyKey("REPEAT")
def double(event):
	key = event.key().name
	hdlib.pressOnce(key,outside = True)

	# Not neccessary:
	# return False

hdlib.run("/dev/input/event3")

from time import sleep
sleep(10)

hdlib.kill()
