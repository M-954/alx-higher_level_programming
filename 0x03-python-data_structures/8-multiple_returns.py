#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple = (0, None)
        return(tuple)
    else:
        tuple = (len(sentence), sentence[:1])
    return(tuple)
