#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newt = a_dictionary.copy()
    new_list = list(newt.keys())

    for i in new_list:
        newt[i] *= 2

    return (newt)
