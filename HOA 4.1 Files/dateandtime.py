# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:54:29 2026

@author: Shin
"""

import time

def pause():
    for i in range(10, 0, -1):
        print(f"The program will end in {i}..")
        time.sleep(1)


def current_time():
    t = time.strftime("%I:%M %p")
    return t

    
def current_date():
    d = time.strftime("%b %d %Y")
    return d