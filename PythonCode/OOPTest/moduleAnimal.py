class Animal:
	def __init__(self, animalName, animalType):
		self._name = animalName
		self._type = animalType
	
	def printName(self):
		print("The animal name is: ", self._name)
	
	def printType(self):
		print("The animal type is: ", self._type)

	def printInfo(self):
		self.printName()
		self.printType()
	
	def doSomething(self):
		pass


class Dog(Animal):
	def __init__(self):
		Animal.__init__(self, "Dog", "Noisy")

	def doSomething(self):
		print("Im a ", self._name, ", so i'll barc")

'''
test1 = Animal("Cat", "Smelly")
test2 = Dog()

test1.printInfo()
test1.doSomething()

print ">>>>>>>"

test2.printInfo()
test2.doSomething()
'''
