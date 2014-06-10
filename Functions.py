#Example file working with functions


def func1():
	print ('I AM A FUCKING FUNCTION')

func1()

#this function simply adds (or concatentates) two arguments
# it does not print those arguments
def func2(arg1, arg2):
	return arg1 + arg2

print(func2(10, 20))
print(func2('a', 'b'))

def cube(x):
	return x*x*x

print(cube(3))

#function with default value for an arguments
def power(num, x=1):
	result = 1; 
	for i in range(x):
		result = result * num
	return result

print(power(2, 3))

#function with variable number of arguments
def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result


print(multi_add(1,5,3,2,1,2,3,34,1))