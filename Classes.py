#how classes work in python

#defining a class with two methods
class myClass():
	def method1(self):
		print("myClass method1")

	def method2(self, someString):
		print("myClass method2 " + someString)

#inherits from myclass - by passing myClass in teh constructor
class anotherClass(myClass):
	def method2(self):
		print ("anotherClass method2") #overrides methods from other class
	def method1(self):
		myClass.method1(self)
		print ("anotherClass method1")



def main():
	c = myClass()
	c.method1()
	c.method2("this string")

	c2 = anotherClass()
	c2.method1()
	c2.method2()


if __name__ == '__main__':
	main()