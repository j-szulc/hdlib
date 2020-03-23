
from .structs.events import *
from .structs.keys import *
from collections import defaultdict

class WhatToDo:

	listeners = None

	# Do not send back the event
	# Setting it to true overwrites event.passthrough
	suppress = False

	def __init__(self, listeners):
		self.listeners = listeners

	#Function to execute after all the listeners have finished
	def fallback(self, event):
		# If we're not suppressing the event
		# We send it back to the system
		try:
			if (not self.suppress) and (not event.suppress):		
				event.send()
		except AttributeError:
			# Supress the event if we don't know if we should or not
			pass

	def listen(self, func, suppress = False):
		# Stop adding listeners after supressed flag's been set
		if not self.suppress:
			self.listeners.append(func)
			self.suppress = suppress

	# The WhatToDo class does not store the event it's being run upon
	# It is passed to each listener
	# So that they know why they've been triggered
	# (in a case they listen to multiple events)
	def execute(self, event):
		for l in self.listeners:
			l(event)
		self.fallback(event)

# Maps events to WhatToDo with them
class Map:

	dict_ = defaultdict(lambda: WhatToDo([]))

	def listenEvent(self,event,suppress = False):
		def decorator(func):
			self.dict_[event].listen(func, suppress)
			return func
		return decorator

	# Listen to a key (regardless of modifiers)
	def listenKey(self,key,action = Action.PRESS, suppress = False):
		return self.listenEvent(KeyEvent(key,action),suppress)

	# Listen to an exact combo
	def listenCombo(self,combo,action = Action.PRESS, suppress = False):
		return self.listenEvent(ComboEvent(combo,action),suppress)

	# Listen to a key and capture it
	# (Do not pass it to the system)
	def captureKey(self,key,action = Action.PRESS):
		return self.listenKey(key,action,suppress=True)

	# Listen to an exact combo and capture it
	# (Do not pass it to the system)
	def captureCombo(self,combo,action = Action.PRESS):
		return self.listenCombo(combo,action,suppress=True)

	# Listen to all the keys
	def listenEveryKey(self,action = Action.PRESS, suppress = False):
		def decorator(func):
			for key in keys:
				self.listenKey(key,action,suppress)(func)
		return decorator
	
	# Capture all the keys
	def captureEveryKey(self,action = Action.PRESS):
		return self.listenEveryKey(action, True)

	# The WhatToDo class does not store the event it's being run upon
	# It is passed to each listener
	# So that they know why they've been triggered
	# (in a case they listen to multiple events)
	def execute(self, event):
		self.dict_[event].execute(event)


