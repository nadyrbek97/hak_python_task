import itertools

a = str(input(""))
l = []
for i in a:
    l.append(i)

keys = []
groups = []

for k, g in itertools.groupby(l):
    keys.append(k)
    groups.append(list(g))
    
s = "("
for i in groups:
    s += str(len(i))
    s += ", "
    s += i[0]
    s += ") ("
print(s[:len(s)-2])

