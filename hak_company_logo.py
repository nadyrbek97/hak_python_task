import itertools
a = str(input("Put your logo name: "))
l = []
n = []
l = [ i for i in a ] 
l = sorted(l)
keys = []
groups = []

for k,g in itertools.groupby(l):
    keys.append(k)
    groups.append(list(g))

for i in range(0,3):
    n.append(max(groups, key = len))    
    groups.remove(max(groups, key = len))

for i in n:
    print(i[0],len(i))

