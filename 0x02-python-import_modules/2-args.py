#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    ln = len(args)-1
    if ln == 0:
        print("{} arguments.".format(ln))
    elif ln == 1:
        print("{} argument:".format(ln))
    else:
        print("{} arguments:".format(ln))
    for i in range(1, (ln+1)):
        print("{:d}: {}".format(i, args[i]))
