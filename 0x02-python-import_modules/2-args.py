#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
if a == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(a))
for i in range(a):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
