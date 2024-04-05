#!/usr/bin/python3
for a in range(ord('z'), ord('a') -1, -1):
    if a % 2 == 0:
        print(chr(a), end='')
    else:
        print(chr(a - 32), end='')
