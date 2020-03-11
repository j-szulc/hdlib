from helpers import sum_
from output import trigger
from events import Action

#
# ALL KEYS
#

class Key:

	# e.g. nameToVKey["shift"].expand() == [nameToPKey["lshift"], nameToPKey["rshift"]]
	def expand(self):
		class InvalidKeyType(Exception):
			pass
		
		if(type(self) == PKey):
			return [self]
		elif(type(self) == VKey):
			return sum_([subkey.expand() for subkey in self.keyset], start=[])
		else:
			raise InvalidKeyType

#
# PHYSICAL KEYS
#

class PKey(Key):
	
	name = ""
	code = -1

	def __init__(self, tuple_):
		name, code = tuple_
		self.name = name
		self.code = code
	
	def trigger(self, action):
		trigger(self.code, int(action))

pkeytuples = [
	("a", 30),
	("lshift", 42),
	("rshift", 54)
]

pkeys = [ PKey(tuple_) for tuple_ in pkeytuples ]
nameToPKey = { tuple_[0]: pkeys[i] for (i,tuple_) in enumerate(pkeytuples) }

#
# VIRTUAL KEYS
#

class VKey(Key):
	
	name = ""
	keyset = frozenset()	
	
	def __init__(self, tuple_):
		name, keyset = tuple_
		self.name = name
		self.keyset = frozenset(keyset)

vkeytuples = [
	("shift", {nameToPKey["lshift"], nameToPKey["rshift"]})
]

vkeys = [ VKey(tuple_) for tuple_ in vkeytuples ]
nameToVKey = { tuple_[0]: vkeys[i] for (i,tuple_) in enumerate(vkeytuples) }

#
# ALL KEYS
#

nameToKey = { **nameToPKey, **nameToVKey }





