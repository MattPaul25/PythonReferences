# Path utilities #

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def pathAttributes():
	print (os.name)
	print ("Item exists: " + str(path.exists("textfile.txt")))
	print ("Item is a file: " + str(path.isfile("textfile.txt")))
	print ("Item is a directory: " + str(path.isdir("textfile.txt")))

	print ("Items Path: " + str(path.realpath("textfile.txt")))
	print ("Items Path: " + str(path.split(path.realpath("textfile.txt"))))

def pathModified():
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	t = time.ctime(path.getmtime("textfile.txt"))
	print("it has been " + str(td) + " since the file was last modified")
	print ("the path was last modified: " + t)
	print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

pathAttributes()
pathModified()