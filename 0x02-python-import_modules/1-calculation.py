#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, cal.add(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, cal.sub(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, cal.mul(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, cal.div(a, b)))
