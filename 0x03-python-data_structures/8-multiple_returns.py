#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_c = (len(sentence), None)
    else:
        tuple_c = (len(sentence), sentence[0])
    return tuple_c
