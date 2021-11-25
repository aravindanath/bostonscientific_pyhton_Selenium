"""
list -- []
set -- {}
set ---> set()
dict --> {key,val}
nestedDic = {key{key,value}}
tuple --> ()
"""


std = {"Arvind","Rohit","Umesh","Ahsul","Arvind"}
print(std)

std.add("Ravi")
print(std)

std.remove("Rohit")
print(std)

std.pop()
print(std)