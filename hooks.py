#from events import PKeyEvent, PComboEvent
from events import *
from collections import defaultdict

class WhatToDo:

	listeners = []
	capturer = None

	#Function to execute if there's no capturer
	def fallback(self, event):
		#If we have nothing to capture then trigger the event back (to the system)
		if(type(self.event) == PKeyEvent):		
			self.event.trigger()
			pass

	def listen(self, func):
		#Stop adding listeners when there's a capturer
		if(self.capturer == None):
			self.listeners.append(func)

	def capture(self, func):
		self.capturer = func

	def execute(self, event):
		for l in self.listeners:
			l(event)
		if(self.capturer != None):
			self.capturer(event)
		else:
			self.fallback(event)

class Map:

	d = defaultdict(lambda: WhatToDo())

	def captureEvent(self,event):
		def decorator(func):
			self.d[event].capture(func)
		return decorator

	def listenEvent(self,event):
		def decorator(func):
			self.d[event].capture(func)
		return decorator
	
	def execute(self, event):
		d[event].execute(event)

MAP = Map()


#from keys import *
#(listenEvent(PKeyEvent(nameToPKey["a"],Action.PRESS))(print)

