l = []

for i in range(int(input())):
    s = str(input())
    l.append(s)

dist = []
dic = {}
for i in l:
    dic[i] = 1
    if i not in dist:
        dist.append(i)
    else:
        dic[i] += 1

print(len(dist))

for i in dic.values():
    print(i, end = " ")
