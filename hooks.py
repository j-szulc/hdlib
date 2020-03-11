#from events import PKeyEvent, PComboEvent
from events import *
from collections import defaultdict

class WhatToDo:

	listeners = None

	# Do not send back the event
	# Setting it to true overwrites event.passthrough
	suppress = False

	def __init__(self):
		self.listeners = []

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
		print("I'm listening")
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

	dict_ = defaultdict(lambda: WhatToDo())

	def listenEvent(self,event,suppress = False):
		def decorator(func):
			for pevent in event.expand():
				print(pevent)
				self.dict_[pevent].listen(func, suppress)
		return decorator
	
	def execute(self, pevent):
		self.dict_[pevent].execute(pevent)

MAP = Map()

def listenKey(key,action = Action.PRESS, suppress = False):
	return MAP.listenEvent(KeyEvent(key,action),suppress)

def listenCombo(combo,action = Action.PRESS, suppress = False):
	return MAP.listenEvent(ComboEvent(combo,action),suppress)

def captureKey(key,action = Action.PRESS):
	return listenKey(key,action,True)

def captureCombo(combo,action = Action.PRESS):
	return listenCombo(combo,action,True)

listen = listenCombo
capture = captureCombo

#def listenKey(key, suppressaction = Action.PRESS):
#	return Map.captureEvent(KeyEvent(

#from keys import *
#(listenEvent(PKeyEvent(nameToPKey["a"],Action.PRESS))(print)

