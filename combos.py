from helpers import product
from keys import nameToKey

#
# COMBO
#

class Combo:

	key = None
	modifiers = frozenset()
	
	def __init__(self, key, modifiers):
		self.key = key
		self.modifiers = frozenset(modifiers)	
	
	# e.g. Combo.fromString("ctrl-c")
	#@static
	def fromStr(str_):
		splitted = str_.split("-")
		global nameToKey
		key = nameToKey[splitted[-1]]
		modifiers = [nameToKey[x] for x in splitted[:-1]]
		return Combo(key, modifiers)

	def expand(self):
		# e.g. [(nameToKey("lctrl"),nameToKey("lshift")),(nameToKey("lctrl"),nameToKey("rshift")),...]
		modifiersVariants= product([ m.expand() for m in self.modifiers ])

		return [Combo(k,m) for k in self.key.expand() for m in modifiersVariants]

#
# PHYSICAL COMBO
#

class PCombo(Combo):
	
	pass
