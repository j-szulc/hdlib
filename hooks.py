#from events import PKeyEvent, PComboEvent
from events import *
from collections import defaultdict

class WhatToDo:

	listeners = []

	# Do not send back the event
	# Setting it to true overwrites event.passthrough
	suppress = False

	#Function to execute if there's no capturer
	def fallback(self, event):
		# If we have nothing to capture then pass it through to the system
		# (trigger the event back)
		try:
			if (not self.suppress) and event.passthrough:		
				event.trigger()
		except AttributeError:
			# do nothing by default
			pass

	def listen(self, func, suppress = False):
		#Stop adding listeners when supressing
		if not self.suppress:
			self.listeners.append(func)
		self.suppress = suppress

	def execute(self, event):
		for l in self.listeners:
			l(event)
		if not self.suppress:
			self.fallback(event)

class Map:

	d = defaultdict(lambda: WhatToDo())

	def listenEvent(self,event,suppress = False):
		def decorator(func):
			for pevent in event.expand():
				self.d[pevent].listen(func, suppress)
		return decorator
	
	def execute(self, pevent):
		print(pevent)
		print(type(pevent))
		print(hash(pevent))
		print(len(MAP.d))
		try:
			print(hash(pevent.key))
		except AttributeError:
			pass
		self.d[pevent].execute(pevent)

MAP = Map()

#def listenKey(key, suppressaction = Action.PRESS):
#	return Map.captureEvent(KeyEvent(

#from keys import *
#(listenEvent(PKeyEvent(nameToPKey["a"],Action.PRESS))(print)

