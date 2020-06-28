'''
	List Comprehensions
	https://www.youtube.com/watch?v=AhSvKGTh28Q&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-

	[exp for val in collection]
'''

# __ Example Number 1

squares = []

for i in range(1, 101):
	squares.append(i**2)

print(squares)
print()

squares_lc = [i**2 for i in range(1,101)]
print(squares_lc)
print()

first_names = ["Joshua", "Rebecca", "Diane", "John"]
last_names = ["Harvey", "Winter", "McCabe", "Marsh"]

names_lc = [{'first:'+fn} for fn in first_names]


print([f'{x} {y}' for x,y in zip(first_names,last_names)])
print()

# an alternative method only if lists are the same length
print([first_names[i] + '_' + last_names[i] for i in range(0, len(first_names))])
print()

# yet another approach written verbose
new_list = []
for index in range(len(first_names)):
    new_list.append(first_names[index] + ' : ' + last_names[index])
print(new_list)

print()



# __ Example Number 2

movies = ["Star Wars", "Ghandi", "Jungle Book", "Fight Club", "RainMan",
"The Walk", "Snowden", "Social Network", "Beautiful Mind", "Accountant",
"The Martian", "Exodus", "The Firm", "RainMaker"]

# this is the long written way without the use of list comprehension
S_movies=[]
for title in movies:
	if title.startswith("S"):
		S_movies.append(title)
print(S_movies)

print()

# this is with the use of list comprehension
S_movies_lc = [title for title in movies if title.startswith("S")]
print(S_movies_lc)

print()


# __ Example Number 3
movies = [("Star Wars", 1970), ("Ghandi", 1910), ("Jungle Book", 1990), 
("Fight Club", 1995), ("RainMan", 1998), ("The Walk", 2010), ("Snowden", 2015), 
("Social Network", 2012), ("Beautiful Mind", 2002), ("Accountant", 2017), 
("The Martian", 2018), ("Exodus", 2007), ("The Firm", 2001), ("RainMaker", 1992)]

# year can be excluded from the first arg in the list comprehension
print([(title,year) for (title, year) in movies if year > 2000])
print()

# __ Example Number 4
v = [2, -3, 1]

# this is the incorrect way to multiple by each value
print(4*v)

print([4*x for x in v])


# __ Example Number 5 - Cartesian Product
# A = {1,3} B = {x,y} Ax = {(1,x), (1,y), (3,x), (3,y)}

A = [1,3,5,7]
B = [2,4,6,8]

print([(a,b) for a in A for b in B])
