'''
	Map, Filter, Reduce Functions
	https://www.youtube.com/watch?v=hUes6y2b--0&
	list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-
'''

# __ MAP FUNCTION

# -- Example Number 1
import math

def area(r):
	'''Area of a circle with radius 'r'.'''
	return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# verbose way of calling this function with the radii list
areas = []
for r in radii:
	a = area(r)
	areas.append(a)

print(areas)
print()

# the shorter way with the map function
circle_list = list(map(area, radii))
print(circle_list)
print()

# -- Example Number 2
peeps = [('Joshua', 31), ('Diane', 61), ('John', 59), ('Rebecca', 29)]


# harder way of iterating with a nameless function
age_in_seconds = lambda prsn: (prsn * 365 * 24 * 60 * 60)

# the problem with this is you cant use zip without 
leest = []
for name, age in peeps:
	leest.append(tuple((name,age_in_seconds(age))))

print(leest)
print()


# easier way of iterating with nameless function
age_in_seconds = lambda prsn: (prsn[0], prsn[1] * 365 * 24 * 60 * 60)

print(list(map(age_in_seconds, peeps)))
print()


# __ FILTER FUNCTION
import statistics 

# -- Example Number 1 
data = [1.3, 2.7, 0,8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)
print(avg)
print() 

abov_avg = list(filter(lambda x: x > avg, data))
print(abov_avg)
print()


# -- Example Number 2 
	# false values in python are: 
		# "", 0, 0.0, 0j, [], (), {}, False, None, 

states = ['Florida', 'Arizona', '', '', 'California', 'New Hampshire', '', '', '']

print(list(filter(None, states)))



