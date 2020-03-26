from .errors import *
from ..helpers import *
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

	def __str__(self):
		return str(self.name)

	def __repr__(self):
		return repr(self.name)+":"+repr(self.codes)	

class Combo:

	key = None
	modifiers = frozenset()
	
	def __init__(self, key, modifiers):
		self.key = key
		self.modifiers = frozenset(modifiers)
	

	def __repr__(self):
		return sum_([repr(m)+"-" for m in self.modifiers], start="") + repr(self.key)

	def __str__(self):
		return sum_([str(m)+"-" for m in self.modifiers], start="") + str(self.key)

	def __hash__(self):
		return hash((self.key,self.modifiers))

	def __eq__(self,obj):
		return isinstance(obj,Combo) and (self.key,self.modifiers) == (obj.key, obj.modifiers)
		
class Keyboard:

	def __init__(self,keytuples = keytuples):
		self.keys = [ Key(tuple_) for tuple_ in keytuples ]
		self.nameToKey = { key.name: key for key in self.keys }
		self.codeToKey = mergeDicts( {code:key for code in key.codes } for key in self.keys);

	def keyFromStr(self,str_):
		try:
			return self.nameToKey[str_]
		except KeyError:
			raise InvalidKeyStr(str_)

	def keyFromInt(self,int_):
		try:
			return self.codeToKey[int_]
		except KeyError:
			return Key(None,(int_,))

	# Key from something
	def keyFrom(self,sth):
		if isinstance(sth,Key):
			return sth
		if isinstance(sth,int):
			return self.keyFromInt(sth)
		elif isinstance(sth,str):
			return self.keyFromStr(sth)
		else:
			raise InvalidSth(sth)

	def comboFromStr(self,str_):
		splitted = str_.split("-")

		key = splitted[-1]
		modifiers = splitted[:-1]

		return Combo(self.keyFrom(key), [self.keyFrom(m) for m in modifiers])

	# Combo from something
	def comboFrom(self,sth):
		if isinstance(sth,Combo):
			return sth
		elif isinstance(sth,str):
			return self.comboFromStr(sth)
		else:
			raise InvalidSth(sth)
	

