import hdlib
import os
from time import sleep

@hdlib.listen("w")
@hdlib.listen("w","REPEAT")
def whoami(event):
	os.system("whoami")
	return True

hdlib.run("/dev/input/event3")
print("I no longer need root to work!")

sleep(5)
hdlib.dropPrivileges()
sleep(5)


