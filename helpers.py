from operator import add
from itertools import product as itertools_product
from collections import defaultdict, ChainMap
# Contains useful code snippets

def fold(list_, fun, start):
	for x in list_:
		start = fun(start, x)
	return start

# e.g. sum(["a","b"],"") == "ab"
def sum_(list_, start=0):
	return fold(list_, add, start)

# e.g. product([["a","b"],[1,2]]) == [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
def product(list_of_lists):
	return list(itertools_product(*list_of_lists))

def infinity():
	while True:
		yield None

def mergeDicts(l):
    return dict(ChainMap(*reversed(list(l))))

# UNUSED
#class key_dependent_dict(defaultdict):
#
#	def __init__(self,f_of_x):
#		super().__init__(None) # base class doesn't get a factory
#		self.f_of_x = f_of_x # save f(x)
#	def __missing__(self, key): # called when a default needed
#		ret = self.f_of_x(key) # calculate default value
#		self[key] = ret # and install it in the dict
#		return ret
