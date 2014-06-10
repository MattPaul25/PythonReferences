# example file for working with loops
#only two types of loops, while and for 

def main():
	x = 0
	#showing a while loops
	while (x < 5):
		print(x)
		x = x + 1

def func1():
	#showing a for loop
	for x in range(5, 10):
		print(x)

def func2():
	#for over array 
	days = ['mon', 'tues', 'wed', 'thurs', 'frid', 'sat', 'sun']
	for d in days:
		print(d)

def func3():
	for x in range(5, 10):
		if (x == 7): break
		print(x)

def func4():
	for x in range(5, 10):
		if ((x % 2) == 0): continue
		print(x)

def func5():
	days = ['mon', 'tues', 'wed', 'thurs', 'frid', 'sat', 'sun']
	for x, d in enumerate(days):
		print(x, d)

if __name__ == '__main__':
	main()

func1()
func2()
func3()
func4()
func5()
