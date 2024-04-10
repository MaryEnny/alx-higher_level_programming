#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    c = len(sys.argv) - 1
    if c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"*", "-", "/", "+"}
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, (a - b)))
    elif sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, (a + b)))
    elif sys.argv[2] == "/":
        print("{} / {} = {:1}".format(a, b, (a / b)))
    else:
        print("{} * {} = {}".format(a, b, (a * b)))
