from helpers import key_dependent_dict

class WhatToDo:
	
	event = None

	listeners = []
	capturer = None

	#Function to execute if empty()
	def fallback(self):
		pass

	def __init__	
	
	def listen(self, func):
		if(self.capturer == None):
			self.listeners.append(func)

	def capture(self, func):
		self.capturer = func
	
	def empty():
		return self.listeners == [] and self.capturer == None

	def execute(self):
		if self.empty():
			self.fallback()
		for l in self.listeners:
			l()
		if(self.capturer != None):
			self.capturer()

MAP = key_dependent_dict(lambda event: WhatToDo(event))


def captureEvent(event):
	def decorator(func):
		global MAP
		MAP[event].capture(func)
	return decorator

def listenEvent(event):
	def decorator(func):
		global MAP
		MAP[event].listen(func)
	return decorator
			
