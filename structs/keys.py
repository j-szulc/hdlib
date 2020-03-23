
from ..io.output import *
from ..helpers import *
from .errors import *
from ..keytuples.keytuples import keytuples

#
# CLASS DEFINITIONS
#

class Key:

	name = ""
	codes = ()

	def __init__(self, tuple_):
		name, codes = tuple_
		self.name = name
		self.codes = tuple(codes)

	@staticmethod
	def fromStr(str_):
		try:
			return nameToKey[str_]
		except KeyError:
			raise InvalidKeyStr(str_)

	@staticmethod
	def fromInt(int_):
		try:
			return codeToKey[int_]
		except KeyError:
			raise InvalidKeyCode(int_)

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

	def send(self, action):
		# The 0th code is sent by default
		send(self.codes[0], int(action))

	def __str__(self):
		return str(self.name)

	def __repr__(self):
		return repr(self.name)+":"+repr(self.codes)	

keys = [ Key(tuple_) for tuple_ in keytuples ]
nameToKey = { key.name: key for key in keys }
codeToKey = mergeDicts( {code:key for code in key.codes } for key in keys);

def sendall(action):
	for key in keys:
		key.send(action)




