#!/usr/bin/python3 
# usage: ./main.py examples/config.py examples/config2.py ...
from ioio.input import *
from structs.keys import *
from structs.combos import *
from structs.events import *
from structs.modifiers import *
from structs.actions import *
from hooks import *

import os, pwd, grp
import sys
from time import sleep
def drop_privileges(uid_name='nobody', gid_name='nobody'):
    if os.getuid() != 0:
        # We're not root so, like, whatever dude
        return

    # Get the uid/gid from the name
    running_uid = pwd.getpwnam(uid_name).pw_uid
    running_gid = grp.getgrnam(gid_name).gr_gid

    # Remove group privileges
    os.setgroups([])

    # Try setting the new uid/gid
    os.setgid(running_gid)
    os.setuid(running_uid)

    # Ensure a very conservative umask
    old_umask = os.umask(77)

if(__name__ == "__main__"):
	
	def execConfigs(configs):
		for config in configs:
			with open(config,"r") as f:
				exec(f.read())


	MAP = Map()

	listen = MAP.listenCombo
	capture = MAP.captureCombo
	listenKey = MAP.listenKey
	captureKey = MAP.captureKey

	modifierList = ["shift","ctrl","alt","mod"]
	MODIFIERS = ModifierSet(modifierList)
	for m in modifierList:
		listenKey(m,Action.PRESS)(MODIFIERS.update)
		listenKey(m,Action.RELEASE)(MODIFIERS.update)

	runConfigs = False
	configs = sys.argv[1:]

	def handlingFun(key, action):

		drop_privileges()

		global runConfigs
		if not runConfigs:
			execConfigs(configs)
			runConfigs=True

		combo = Combo(key, MODIFIERS.current)

		keyevent = KeyEvent(key, action)				
		comboevent = ComboEvent(combo, action)

		for e in [keyevent, comboevent]:
			MAP.execute(e)

	loop(handlingFun = handlingFun, nOfIterations=100)

	for m in modifierList:
		Key.fromSth(m).send(Action.RELEASE)

