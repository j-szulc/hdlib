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
	
		
		if isinstance(PKey):
			return [self]
		elif isinstance(VKey):
			return sum_([subkey.expand() for subkey in self.keyset], start=[])
		else:
			raise InvalidKeyType(type(self))

	@staticmethod
	def fromStr(str_):
		if "nameToKey" in globals():
			#global nameToKey
			dict_ = nameToKey
		else:
			dict_ = nameToPKey

		if str_ in dict_:
			return dict_[str_]
		else:
			raise InvalidKeyStr(str_)

	@staticmethod
	def fromInt(int_):
		#global codeToPkey
		if int_ in codeToPKey:
			return codeToPKey[int_]
		else:
			raise InvalidKeyCode[int_]

	@staticmethod
	def fromSth(sth):
		if isinstance(sth,Key):
			return sth
		if isinstance(sth,int):
			return Key.fromInt(sth)
		elif isinstance(sth,str):
			return Key.fromStr(sth)
		else:
			raise InvalidSth(sth)

	def isPhysical(self):
		return isinstance(self,PKey)

	def __str__(self):
		return name

#
# PHYSICAL KEYS
#

class PKey(Key):
	
	code = -1

	def __init__(self, tuple_):
		name, code = tuple_
		self.name = name
		self.code = code

	def send(self, action):
		send(self.code, int(action))


	def __repr__(self):
		return "P"+name+":"+str(code)	
		

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

	def __repr__(self):
		return "V"+self.name+":"+sum_([repr(k) for k in self.keyset],start="")

vkeytuples = [
	("shift", {PKey.fromStr("lshift"), PKey.fromStr("rshift")})
]

vkeys = [ VKey(tuple_) for tuple_ in vkeytuples ]
nameToVKey = { tuple_[0]: vkeys[i] for (i,tuple_) in enumerate(vkeytuples) }

#
# Key format conversion dictionaries
#

nameToKey = { **nameToPKey, **nameToVKey }





