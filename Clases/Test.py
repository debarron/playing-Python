class MyTest:
    count = 0


    def __init__(self):
        MyTest.count = MyTest.count + 1
        self.count = 0

    def aMethod(self):
        print("Hello from aMethod!")




myOb = MyTest()
myOb.aMethod()

myOb2 = MyTest()
myOb2.aMethod()

myOb3 = MyTest()
myOb3.aMethod()


print("Instances: " + str(myOb3.count))

print("Instances: " + str(MyTest.count))


