#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    if a % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(a - diff)), end='')
