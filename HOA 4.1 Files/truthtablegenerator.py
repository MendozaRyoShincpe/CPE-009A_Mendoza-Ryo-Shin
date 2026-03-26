# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:52:43 2026

@author: Shin
"""
def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0:
        return "You need to enter an integer"
    else:
        total_combinations = 2 ** number_of_variables
        combinations_list = []
        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:]
            while len(bin_equivalent) < number_of_variables:
                bin_equivalent = "0" + bin_equivalent
            combinations_list.append(tuple(int(val) for val in bin_equivalent))
        return combinations_list

print(generate_truthtable())   # Will show the error message
print(generate_truthtable(3))  # Will generate combinations