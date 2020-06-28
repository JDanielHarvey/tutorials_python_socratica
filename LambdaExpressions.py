'''
	Lambda Expessions & Anonymous Functions
	https://www.youtube.com/watch?v=25ovCm9jKfA&
	list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-

	Useful when you need a short quick throwaway function
'''

# the normal named function approach
def f(x):
	return 3*x + 1 

print(f(2))
print()

# the nameless way

g = lambda x: 3*x + 1
print(g(2))
print()


full_name = lambda fn, ln: dict(first = fn.lower().title(), last = ln.lower().title())
print(full_name("JOSHUA", "HaRvEy"))

print()


political_theorists = ["John Rawls", "John Locke", "John Ruskin", "Alex de Tocqueville"
"David Humme", "Jean Jaque Rousseau", "Ralph Waldo Emerson", "Immanuel Kant", 
"Thomas Hobbs", "John Stuart Mill", "Adam Smith"]

print(political_theorists.sort())
print()

political_theorists.sort(key=lambda name: name.split(" ")[-1].lower())
print(political_theorists)
print()

# this is an example of a re-usable math function that maintain it's...
# ...parameters but needs to be computedon a variable input (x)

def build_quadratic_functions(a, b, c):
	'''Returns the function f(x) = ax^2 + bx + c'''
	return lambda x: a*x**2 + b*x + c

print(build_quadratic_functions(2,3,-5)(2))

bqf = build_quadratic_functions(2,3,-5)
print(bqf(2))