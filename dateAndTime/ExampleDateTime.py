from datetime import date
from datetime import time


current = date.today()

print(current)

print("Current day is ", current.day)
print("Current Month is ", current.month)
print("Current Year is ", current.year)


str = "file"+str(current.day)+".png"
print(str)