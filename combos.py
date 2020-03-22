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
		self.key = Key.fromSth(key)
		self.modifiers = frozenset([Key.fromSth(m) for m in modifiers])	
	
	# e.g. Combo.fromString("ctrl-c")
	@staticmethod
	def fromStr(str_):
		splitted = str_.split("-")

		key = splitted[-1]
		modifiers = splitted[:-1]

		return Combo(key, modifiers)

	@staticmethod
	def fromSth(sth):
		if isinstance(sth,Combo):
			return sth
		elif isinstance(sth,str):
			return Combo.fromStr(sth)
		else:
			raise InvalidSth(sth)

	
	def send(self, action):		
		for m in self.modifiers:
			m.send(action)
		self.key.send(action)
	
	def __repr__(self):
		return sum_([repr(m)+"-" for m in self.modifiers], start="") + repr(self.key)

	def __str__(self):
		return sum_([str(m)+"-" for m in self.modifiers], start="") + str(self.key)

	def __hash__(self):
		return hash((self.key,self.modifiers))

	def __eq__(self,obj):
		return isinstance(obj,Combo) and (self.key,self.modifiers) == (obj.key, obj.modifiers)
		
