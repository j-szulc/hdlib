#from helpers import product
#from keys import nameToKey
from helpers import *
from keys import *

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
	@staticmethod
	def fromStr(str_):
		splitted = str_.split("-")
		global nameToKey
		key = nameToKey[splitted[-1]]
		modifiers = [nameToKey[x] for x in splitted[:-1]]
		return Combo(key, modifiers)

	@staticmethod
	def fromSth(sth):
		if isinstance(sth,Combo):
			return sth
		elif isinstance(sth,str):
			return Combo.fromStr(sth)
		else:
			raise InvalidSth(sth)

	def expand(self):
		if self.isP():
			return [self]
		else:
			# e.g. [(Key.fromStr("lctrl"),Key.fromStr("lshift")),(Key.fromStr("lctrl"),Key.fromStr("rshift")),...]
			modifiersVariants= product([ m.expand() for m in self.modifiers ])

			return sum_([Combo(k,m).expand() for k in self.key.expand() for m in modifiersVariants],start=[])
	
	def send(self, action):		
		for m in self.modifiers:
			m.send(action)
		self.key.send(action)

	def isPhysical(self):
		return self.key.isPhysical() and all( m.isPhysical() for m in self.modifiers )
	
	def __repr__(self):
		return str(self)

	def __str__(self):
		return sum_([repr(m)+"-" for m in self.modifiers], start="") + repr(self.key)

	def __hash__(self):
		return hash((self.key,self.modifiers))

	def __eq__(self,obj):
		return isinstance(obj,Combo) and (self.key,self.modifiers) == (obj.key, obj.modifiers)
		
