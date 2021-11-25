
class Student:

    def __init__(self,name,age,roll):
        print("Name is",name)
        print(name,"age is", age)
        print(name, "roll no is", roll)

    def reg(self,name,score,sub):
        print("Name is ", name)
        print(name,"has scored", score)
        print(name, "has opted", sub)

    # Protected member
    def _exampleProtected(self):
        print("I am protected method")
    #     private member
    def __exampleProtected(self):
        print("I am protected method")

c = Student("Arvind",34,201)
c.reg("Arvind",99,"Pyhton")