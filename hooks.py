from collections import defaultdict

class WhatToDo:

	listeners = []
	capturer = None

	def listen(self, func):
		if(self.capturer == None):
			self.listeners.append(func)

	def capture(self, func):
		self.capturer = func
	
MAP = defaultdict(lambda: WhatToDo())


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
			
