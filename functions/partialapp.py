'''
PARTIAL APPLICATION
Modifies an existing function by accepting it as as the first parameter
and simplifies its functionality.
Used to interface with library functions to simplify their functionality
'''
from functools import partial
from math import sqrt
def add(m,n):
    return m + n

m = int(input('M: '))
adds = partial(add, m)

n = int(input('N: '))
print(adds(n))