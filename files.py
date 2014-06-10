# read and write files using the built-in python file methods

def createFile():
	#open a file for writing and create it if it doesnt exist
	f = open("textfile.txt", "w+") #w = write, + means that if its not already there then create it
	#write some lines of data to the file
	for i in range(10):
		f.write("this is line %d\r\n" % (i + 1))
	f.close()

def appendFile():
	f = open("textfile.txt", "a+") #a+ means to append data
	for i in range(10):
		f.write("this is line %d\r\n" % (i + 1))
	f.close()
	
def readFile(): #prints file into terminal
	f = open("textfile.txt", "r")
	if f.mode =='r':
		contents = f.read()
		print(contents)
	f.close()

def readLine(): #reads first line and then prints it by character
	f = open("textfile.txt", "r")
	if f.mode == 'r':
		lines = f.readline()
		for i in lines:
			print(i)
	f.close()		

def readLines(): #reads first line and then prints it by character
	f = open("textfile.txt", "r")
	if f.mode == 'r':
		lines = f.readlines()
		for i in lines:
			print(i)
	f.close()		



createFile()
appendFile()
readFile()
readLine()
readLines()