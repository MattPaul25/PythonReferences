#Dealing with dates and times

#import dates from classes built into python libraries
from datetime import date
from datetime import time
from datetime import datetime

def usingDates():
	today = date.today()
	print ("Today's date is ", today)
	print("date components", today.day, today.month, today.year)
	print("Today's weekday #:", today.weekday())

def usingDateTime():
	now = datetime.now()
	time = datetime.time(now)
	print("the date and time is", now)
	print("the time is", time)

def getWeekDay():
	today = date.today()
	days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
	print("Today is a", days[today.weekday()])
	
usingDates()
usingDateTime()
getWeekDay()