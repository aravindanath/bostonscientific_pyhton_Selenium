# from tkinter import *
#
#
# root = Tk()
#
# myLabel1 = Label(root,text="Hello World!")
# myLabel2 = Label(root,text="Welcome to Automation world")
#
# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=5)
#
# root.mainloop()
#
class Employer:

    def __init__(self):
        print("Employee created")

    def temp(self):
        print("I am temp")

    def __del__(self):
        print("Destructor called and emp deleted")


e = Employer()
e.temp()
e.__del__()

#//tagname[@id='2345234' or @id='3445674']

# idevicesinstaller -l


