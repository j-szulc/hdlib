from helpers import key_dependent_dict

class WhatToDo:
	
	event = None

	listeners = []
	capturer = None

	#Function to execute if there's no capturer
	def fallback(self):
		#If we have nothing to do then trigger the event back (to the system)
		self.event.trigger()

	def __init__	
	
	def listen(self, func):
		if(self.capturer == None):
			self.listeners.append(func)

	def capture(self, func):
		self.capturer = func
	
	def empty():
		return self.listeners == [] and self.capturer == None

	def execute(self):
		for l in self.listeners:
			l()
		if(self.capturer != None):
			self.capturer()
		else:
			self.fallback()

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
			
