from helpers import sum

#
# PHYSICAL KEYS
#
class PKey:
	
	name = ""
	code = -1

	def __init__(self, tuple_):
		name, code = tuple_
		self.name = name
		self.code = code

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

class VKey:
	
	name = ""
	keylist = []	
	
	def __init__(self, tuple_):
		name, keylist = tuple_
		self.name = name
		self.keylist = keylist

vkeytuples = [
	("shift", [nameToPKey["lshift"], nameToPKey["rshift"]])
]

vkeys = [ VKey(tuple_) for tuple_ in vkeytuples ]

#
# ALL KEYS
#

# e.g. expandKey(nameToVKey["shift"]) == [nameToPKey["lshift"], nameToPKey["rshift"]]
def expandKey(key):
	class InvalidKeyType(Exception):
		pass
	
	if(type(key) == PKey):
		return [key]
	elif(type(key) == VKey):
		return sum([expand(subkey) for subkey in key.keylist], start=[])
	else:
		raise InvalidKeyType

