import math

a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)
print(c)
d = int(round(math.degrees(math.acos(b/c))))
print(d)

t = u"\u00b0"
print (str(d) + t)
