class InvalidKeyType(Exception):

	def __init__(self,type_):
		self.type_=type_


class InvalidKeyStr(Exception):

	def __init__(self,str_):
		self.str_=str_

class InvalidKeyCode(Exception):

	def __init__(self,int_):
		self.int_=int_

class InvalidSth(Exception):

	def __init__(self,sth):
		self.sth=sth
		self.type=type(sth)
