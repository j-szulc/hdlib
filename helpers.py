from operator import add
from itertools import product as itertools_product
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
