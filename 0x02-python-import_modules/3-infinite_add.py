#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    ln = len(args)-1
    add = 0
    for i in range(1, (ln+1)):
        add = add + int(args[i])
    print("{:d}".format(add))
