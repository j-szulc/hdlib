from collections import defaultdict
from .structs.errors import InvalidListener

class WhatToDo:

	def __init__(self):
		self.listeners = []

	def listen(self, func):
		self.listeners.append(func)

	def unlisten(self, func):
		try:
			self.listeners.remove(func)
		except ValueError:
			raise InvalidListener(func)

	# The WhatToDo class does not store the event it's being run upon
	# It is passed to each listener
	# So that they know why they've been triggered
	# (in a case they listen to multiple events)
	# Returns whether to suppress the event or not
	def execute(self, event):
		for l in self.listeners:
			if l(event) and event.allowSuppress:
				# If function returns True we capture the event
				# i.e. we stop doing anything with it
				# and we do not put it back into system
				return True
		return False

# Maps events to WhatToDo with them
class EventMap:

	
	def __init__(self):
		self.dict_ = defaultdict(lambda: WhatToDo())

	def listenEvent(self,event):
		def decorator(func):
			self.dict_[event].listen(func)
			return func
		return decorator

	def unlistenEvent(self,event):
		def decorator(func):
			self.dict_[event].unlisten(func)
			return func
		return decorator

	# The WhatToDo class does not store the event it's being run upon
	# It is passed to each listener
	# So that they know why they've been triggered
	# (in a case they listen to multiple events)
	# Executes fallback if nobody captured the event
	def execute(self, fallback, events):
		for event in events:
			if self.dict_[event].execute(event):
				return True
		fallback()
		return False


