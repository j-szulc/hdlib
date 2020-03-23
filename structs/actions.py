from enum import IntEnum

class Action(IntEnum):
	
	RELEASE = 0
	PRESS = 1
	REPEAT = 2

	@staticmethod
	def fromSth(sth):
		if isinstance(sth,int):
			return Action(sth)
		elif isinstance(sth,str):
			return Action[sth.upper()]
		else:
			raise InvalidSth(sth)
