'''
	Datetime Module (Dates and Times)
	https://www.youtube.com/watch?v=RjMbCUpvIgw&
	list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=11&t=0s
'''

import datetime

# print(dir(datetime))
# print()
# print(help(datetime.date))
# print()

firstofJuly = datetime.date(2020, 7, 1)

print(firstofJuly)
print()

print(firstofJuly.year)
print(firstofJuly.month)
print(firstofJuly.day)
print()

print(type(firstofJuly))