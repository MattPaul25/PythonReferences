from datetime import datetime

#how to format dates and times
def main():
	now = datetime.now()
	print(now.strftime("%Y")) #2014
	print(now.strftime("%y")) #14
	print(now.strftime("%a, %d %B, %y")) #mon, 09 June, 14
	print(now.strftime("%c")) #06/09/14 20:08:05
	print(now.strftime("%x")) #06/09/14
	print(now.strftime("%X")) #20:08:05
	print(now.strftime("%A")) #Monday
	print(now.strftime("%I:%M:%S %p")) #08:15:47 PM
	print(now.strftime("%H:%M")) #20:15

if __name__ == '__main__':
	main()