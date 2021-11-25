#       0,1,2,3...
name = "aravind_12345"
#          0      1

print("Count "+str(name.count('a')))
fn = name.split("_")[0]
num = name.split("_")[1]
print(fn)
print(num)


print(name.startswith("ar"));
print(name.endswith("87"))

str = "hello world"
x = str.index("world")
print(x)