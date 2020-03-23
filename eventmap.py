
from collections import defaultdict

class WhatToDo:

	listeners = None

	# Do not send back the event
	# Setting it to true overwrites event.suppress
	suppress = False

	# Fallback is a function, which is called when the event is not supposed to be suppressed
	# i.e. we need to send it back through Output class
	def __init__(self, listeners, fallback):
		self.listeners = listeners
		self.fallback = fallback

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
		try:
			if (not self.suppress) and (not event.suppress):		
				self.fallback(event)
		except AttributeError:
			pass

# Maps events to WhatToDo with them
class EventMap:

	
	def __init__(self, fallback):
		self.dict_ = defaultdict(lambda: WhatToDo([],fallback))

	def listenEvent(self,event,suppress = False):
		def decorator(func):
			self.dict_[event].listen(func, suppress)
			return func
		return decorator

	# The WhatToDo class does not store the event it's being run upon
	# It is passed to each listener
	# So that they know why they've been triggered
	# (in a case they listen to multiple events)
	def execute(self, event):
		self.dict_[event].execute(event)


