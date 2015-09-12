# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:45:03 2015

@author: rob

"""

conv  = input('Conversion : ')
value = input('Value      : ')

if conv == 'c' : 
    print((5 * (value - 32)) / 9)
else :
    print(((9 * value) / 5) + 32)

    