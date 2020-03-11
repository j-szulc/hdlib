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
				event.send()
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

	def listenKey(self,key,action = Action.PRESS, suppress = False):
		return self.listenEvent(KeyEvent(key,action),suppress)

	def listenCombo(self,combo,action = Action.PRESS, suppress = False):
		return self.listenEvent(ComboEvent(combo,action),suppress)

	def captureKey(self,key,action = Action.PRESS):
		return self.listenKey(key,action,suppress=True)

	def captureCombo(self,combo,action = Action.PRESS):
		return self.listenCombo(combo,action,suppress=True)
	
	def execute(self, pevent):
		self.dict_[pevent].execute(pevent)

MAP = Map()

listen = MAP.listenCombo
capture = MAP.captureCombo

#def listenKey(key, suppressaction = Action.PRESS):
#	return Map.captureEvent(KeyEvent(

#from keys import *
#(listenEvent(PKeyEvent(nameToPKey["a"],Action.PRESS))(print)

