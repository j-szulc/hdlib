import hdlib

@hdlib.listenKey("y","PRESS")
@hdlib.listenKey("y","RELEASE")
@hdlib.listenKey("z","PRESS")
@hdlib.listenKey("z","RELEASE")
def swap(event):
	keyname = event.key().name
	action = event.action

	if(keyname == "y"):
		newkeyname = "z"
	elif(keyname == "z"):
		newkeyname = "y"

	# Setting outside to False results in a feedback loop
	hdlib.send(newkeyname,action,outside = True)
	# Capture the event
	return True

@hdlib.listen("ctrl-q")
def quit(event):
	hdlib.kill()

	return True

hdlib.run("/dev/input/event3", daemon = False)
