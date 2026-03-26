# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:47:53 2026

@author: Shin
"""

import math

def angle_demo():
    angle = math.sin(math.pi / 2)  # default input is in radians
    # sin(90°) = 1 in degrees = sin(pi/2) = 1 in radians
    print(angle)

    # convert degrees to radians for convenience
    angle = math.sin(math.radians(90))
    print(angle)

    # similar for cosine and other trigonometric/hyperbolic functions

angle_demo()
