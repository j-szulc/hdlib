class InvalidKeyType(Exception):

	def __init__(self,type_):
		self.type_=type_


class InvalidKeyStr(Exception):

	def __init__(self,str_):
		self.str_=str_

