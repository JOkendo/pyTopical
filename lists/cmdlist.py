"""The sys module provides a global variable named argv that is a list of extra text that the user can supply
when launching an application from the operating system shell (normally called the command prompt in
Windows and terminal in OS X and Linux)."""

from sys import argv
from math import sqrt
if len(argv) < 3:
    print('Supply range of values')
else:
    for n in range(int(argv[1]), int(argv[2]) + 1):
        print(n, sqrt(n))
    print()