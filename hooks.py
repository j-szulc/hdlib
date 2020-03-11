#from helpers import key_dependent_dict
#from events import PKeyEvent, PComboEvent
from helpers import *
from events import *

class WhatToDo:
	
	event = None

	listeners = []
	capturer = None

	#Function to execute if there's no capturer
	def fallback(self):
		#If we have nothing to do then trigger the event back (to the system)
		if(type(self.event) == PKeyEvent):		
			#self.event.trigger()
			pass

	def __init__(self, event):
		self.event = event	
	
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
			
