#!/usr/bin/python3
for a in range(0, 99):
    if a < 10:
        print("0{}, ".format(a),end='')
    else:
        print("{}, ".format(a),end='')
