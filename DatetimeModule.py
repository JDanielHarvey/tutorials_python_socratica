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
daysprior100 = datetime.timedelta(-100)

print(firstofJuly)
print()

print(firstofJuly.year)
print(firstofJuly.month)
print(firstofJuly.day)
print()

print(type(firstofJuly))
print()

print(firstofJuly + daysprior100)
print()
print((firstofJuly+daysprior100).strftime("%A, %B, %d, %Y"))
print()

datemessage = "One hundred days prior to July 1st 2020 was {:%A, %B, %d, %Y}"
print(datemessage.format(firstofJuly+daysprior100))
print()

jdh_bday_date = datetime.date(1988, 9, 16)
jdh_bday_time = datetime.time(21, 9, 16)
jdh_bday_datetime = datetime.datetime(1988, 9, 16, 21, 9, 16)

print(jdh_bday_date)
print(jdh_bday_time)
print(jdh_bday_datetime)
print()

print(jdh_bday_datetime.hour) # or
print(jdh_bday_time.hour)

print(jdh_bday_datetime.minute)
print()

# use datetime module with datetime class with method today()
today = datetime.datetime.today()
print(today)
print(today.microsecond)
print() 

# use dates from string to objets
# the format has to match exactly and by not including forward slashes
# an error will be thrown

moon_landing = '7/20/1969'

moon_landing_convert = datetime.datetime.strptime('9/16/1988', '%m/%d/%Y')

print(moon_landing_convert)
print(type(moon_landing_convert))