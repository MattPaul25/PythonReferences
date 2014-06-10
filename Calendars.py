#working with calendars

import calendar

#create a plain text calendar
def makeCal():
	c = calendar.TextCalendar(calendar.SUNDAY)
	str = c.formatmonth(2013,1,0,0)
	print (str)

def makeHTMLCal():
	hc = calendar.HTMLCalendar(calendar.SUNDAY)
	str = hc.formatmonth(2013,1)
	print (str)

def loopMonths():
	for name in calendar.month_name:
		print (name)

def loopDay():
	for day in calendar.day_name:
		print (day)

#calculate days based on a rule first friday of eah month
def calcFriday():
	for m in range(1,13):
		cal = calendar.monthcalendar(2014, m)
		weekone = cal[0]
		weektwo = cal[1]

		if weekone[calendar.FRIDAY] != 0:
			meetday = weekone[calendar.FRIDAY]
		else:
			meetday = weektwo[calendar.FRIDAY]
		print("%10s %2d"  % (calendar.month_name[m], meetday))


makeHTMLCal()
makeCal	()
loopMonths()
print()
loopDay()
print()
calcFriday()