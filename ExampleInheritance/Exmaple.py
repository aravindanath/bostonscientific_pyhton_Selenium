
#Parent Class
class Person:
    def __init__(self,fn, ln):
        self.firstName = fn
        self.lastName = ln
        print("im parent")

    def printName(self):
        print(self.firstName, self.lastName)


class School:
    def __init__(self, fn, ln,):
        self.firstName = fn
        self.lastName = ln
        print("Im student")


    def classRoom(self):
        print("Class room")

# Child class
class Student(Person,School):

     def std(self):
         print(self.firstName, self.lastName)




z = Student("Sundar","Raj")
z.std()
z.classRoom()