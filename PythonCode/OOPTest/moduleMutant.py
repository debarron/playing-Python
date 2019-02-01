from moduleAnimal import Animal

class Human:
	def __init__(self, humanAge, humanOffice):
		self._age = humanAge
		self._office = humanOffice
	
	def doHumanStuff(self):
		print("I'm a human")

	def doTheThing(self):
		pass

class Foo:
	def __init__(self):
		pass

class Mutant(Animal, Human, Foo):

	def __init__(self):
		Animal.__init__(self, "Daniel", "Programmer")
		Human.__init__(self, "27", "Developer")
		Foo.__init__(self)

		self._alive = True
	
	def doTheThing(self):
		print("This is object extends from two classes")
		print("Do the harlem shake")

		self.doHumanStuff()
		self.printInfo()

testMult = Mutant()
print ">>>>>>>>>"

testMult.doTheThing()

