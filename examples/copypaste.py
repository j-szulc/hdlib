import hdlib

@hdlib.listenCombo("ctrl-h")
@hdlib.listenCombo("ctrl-h","REPEAT")
def double(event):
	hdlib.pressOnce("ctrl-a")
	hdlib.pressOnce("ctrl-c")
	hdlib.pressOnce("ctrl-v")
	hdlib.pressOnce("ctrl-v")
	hdlib.send("ctrl","PRESS")
	return True

@hdlib.listen("ctrl-q")
def quit(event):
	hdlib.kill()

	return True

hdlib.run("/dev/input/event3", daemon = False)
