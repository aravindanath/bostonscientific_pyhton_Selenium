

from  datetime import datetime

current = datetime.now()

stamp = current.timestamp()
print(current.timestamp())

str = "File"+str(stamp).replace(".","_")+".txt"

print(str)