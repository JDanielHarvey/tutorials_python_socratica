'''
	Python Functions
	https://www.youtube.com/watch?v=NE97ylAnrz4&
	list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-
'''

import math

# def ping():
# 	return "Ping!"

# print(ping)
# print()
# print(ping())
# print()
# print(dir())
# print()

# x = ping()

# print(f'This is my ping function with the returned value {x}')
# print()
# print(dir())

print(math.pi)
print()

# required argument but no keyword
def volume(r):
	'''Returns the volume of a sphere
	with radius r'''
	v = (4.0/3.0) * math.pi * 4**3
	return v

print(volume(10))
print()

def triangle_area(b, h):
	'''Returns the are of the triangle with
	base b and height h'''
	return 0.5 * b * h

print(triangle_area(3,6))
print()

# keyword arguments also called default arguments
def cm(feet = 0, inches = 0):
	'''Converts a length from feet and inches to centimeters'''
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm

print(cm(feet = 6))
print(cm(inches = 3))

yaoming_cm = cm(feet = 7, inches = 2)
print(yaoming_cm)
print()


def g(y, x=2):
	return x*y

print(g(5))
print()



