#from helpers import sum_
#from output import trigger
#from events import Action
from helpers import *
from output import *
from events import *
from errors import *

#
# CLASS DEFINITIONS
#

class Key:

	name = ""

	# e.g. nameToVKey["shift"].expand() == [nameToPKey["lshift"], nameToPKey["rshift"]]
	def expand(self):
	
		
		if(type(self) == PKey):
			return [self]
		elif(type(self) == VKey):
			return sum_([subkey.expand() for subkey in self.keyset], start=[])
		else:
			raise InvalidKeyType(type(self))

	@staticmethod
	def fromStr(str_):
		global nameToKey
		if str_ in nameToKey:
			nameToKey[str_]
		else:
			raise InvalidKeyStr(str_)

#
# PHYSICAL KEYS
#

class PKey(Key):
	
	code = -1

	def __init__(self, tuple_):
		name, code = tuple_
		self.name = name
		self.code = code

	def trigger(self, action):
		trigger(self.code, int(action))

	@staticmethod
	def fromStr(str_):
		global nameToPKey
		if str_ in nameToPKey:
			nameToPKey[str_]
		else:
			raise InvalidKeyStr(str_)

pkeytuples = [
	("a", 30),
	("lshift", 42),
	("rshift", 54)
]

pkeys = [ PKey(tuple_) for tuple_ in pkeytuples ]
nameToPKey = { tuple_[0]: pkeys[i] for (i,tuple_) in enumerate(pkeytuples) }
codeToPKey = { tuple_[1]: pkeys[i] for (i,tuple_) in enumerate(pkeytuples) }

#
# VIRTUAL KEYS
#

class VKey(Key):
	
	keyset = frozenset()	
	
	def __init__(self, tuple_):
		name, keyset = tuple_
		self.name = name
		self.keyset = frozenset(keyset)

	@staticmethod
	def fromStr(str_):
		global nameToVKey
		if str_ in nameToVKey:
			nameToVKey[str_]
		else:
			raise InvalidKeyStr(str_)

vkeytuples = [
	("shift", {PKey.fromStr("lshift"), PKey.fromStr("rshift")})
]

vkeys = [ VKey(tuple_) for tuple_ in vkeytuples ]
nameToVKey = { tuple_[0]: vkeys[i] for (i,tuple_) in enumerate(vkeytuples) }

#
# Key format conversion dictionaries
#

nameToKey = { **nameToPKey, **nameToVKey }





