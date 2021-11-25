import re

txt =  "The rain in Spain and Spain is great city"

x = re.search("^The.*Spain$",txt)
x = re.findall("Spain",txt)

y = re.split("\s",txt)
z = re.sub("\s","_",txt)
print(z)


"""
[]  [a-z]
\   \d
.   he..o
^   ^hello
$   spain$
*
+
{}
|
()
"""