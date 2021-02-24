"""
PIRPLE PYTHON IS EASY
Homework #3: If statements
File name: ifstatementhw.py
Description: Function that accepts 3 parameters and checks for equality between any two of them.
             The function returns True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
"""

def inte(a,b,c):
	if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
		print('True')
	else: print('False')

inte("5","1",2)