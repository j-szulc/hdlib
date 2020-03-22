# Regenerate the key (name,code) tuple list:

from evdev import ecodes
from collections import defaultdict

nameToCode = defaultdict(lambda: [])

alias = {
	"leftshift": "shift",
	"rightshift": "shift",
	"leftalt": "alt",
	"rightalt": "alt",
	"leftctrl": "ctrl",
	"rightctrl": "ctrl",
	"leftmeta": "mod"
}

for k in dir(ecodes):
	if k[:4] == "KEY_":
		keyname = k[4:].lower()
		if keyname in alias:
			keyname = alias[keyname]
		print(keyname)
		nameToCode[keyname].append(getattr(ecodes,k))


keytuples = [ (n, tuple(c)) for n,c in nameToCode.items()]

with open("./keylist.py","w") as f:
	f.write("keytuples = [\n")
	for keytuple in keytuples:
		f.write("\t"+str(keytuple)+",\n")
	f.write("]\n")
