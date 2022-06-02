#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    names = dir(hid)
    for i in names:
        if i[:2] != "__":
            print("{:s}".format(i))
