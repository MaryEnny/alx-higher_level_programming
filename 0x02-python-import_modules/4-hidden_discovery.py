#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = dir(hidden_4)
    for b in a:
        if b[:2] != "__":
            print("{}".format(b))
