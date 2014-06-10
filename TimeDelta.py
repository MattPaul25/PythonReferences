from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


#construct a basic time delta and print it 
print (timedelta(days = 365, hours = 5, minutes = 1)) #365 days, 5:01:00
#print one year from now
print(" one year from now is", str(datetime.now() + timedelta(days = 365)))
print("in two weeks and 3 days it will be", str(datetime.now() + timedelta(weeks = 2, days = 3)))

#calculate the date one week ago - formmated as a string
t = datetime.now() - timedelta(weeks = 1)
s = t.strftime("%A %B %d, %Y") #strftime is a function that does text manipulation on date
print ("one week ago was " + s)

#calculate how many days till next april fools days
today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
	print ("April fool's day already went by %d days ago" % ((today-afd).days))
	afd = afd.replace(year = today.year + 1)
	print ("Next year it will be " + str((afd - today).days) + " days")
else:
	print ("It will be " + str(((today-afd).days)) + " days")