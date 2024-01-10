#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        den = 0
        for tuples in my_list:
            num += (tuples[0] * tuples[1])
            den += (tuples[1])
        return (num/den)
    return 0
