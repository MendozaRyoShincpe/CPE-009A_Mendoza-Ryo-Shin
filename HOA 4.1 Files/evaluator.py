# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:16:07 2026

@author: Shin
"""

# Propositional Logic evaluator for discrete math (2–3 variables)

print("Propositional logic evaluator for discrete math")

# Ask how many variables to use
variables = int(input("How many variables? "))
total_combinations = 2 ** variables

combinations_list = []  # store all possible combinations

# Generate the combinations
for i in range(total_combinations):
    bin_equivalent = bin(i)[2:]  # binary string without '0b'
    while len(bin_equivalent) < variables:
        bin_equivalent = "0" + bin_equivalent
    combinations_list.append(tuple(int(val) for val in bin_equivalent))
    # Example for 2 variables: [(0,0), (0,1), (1,0), (1,1)]

# Main program
expression = input("Enter the propositional logic expression: ")
# Note: Only the letters A, B, and C are allowed
# Example: not(A and B) or (A and C)

if variables == 2:
    print("A B f")
    for A, B in combinations_list:
        evaluated_expression = eval(expression)
        print(A, B, evaluated_expression)

elif variables == 3:
    print("A B C f")
    for A, B, C in combinations_list:
        evaluated_expression = eval(expression)
        print(A, B, C, evaluated_expression)