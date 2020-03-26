import hdlib

# The same as @hdl.listen("shift-a","PRESS")
# Actions are as follows: "PRESS", "RELEASE", "REPEAT"
@hdlib.listen("shift-a")
def hello(event):
	print("Hello")
	
	# Capture the keystroke
	# Comment it out if you don't want that 
	# (the default behaviour is to not capture)
	return True

@hdlib.listen("ctrl-q")
def quit(event):
	hdlib.kill()

	return True

hdlib.run("/dev/input/event3", daemon = False)
