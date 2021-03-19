# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:34:43 2020

@author: jari
"""

def lucky_number():
    name = input("enter the name\n")
    print("the lucky number of "+ str(name) +' is')
    from random import randint
    a = randint(1,100)
    print(a)

