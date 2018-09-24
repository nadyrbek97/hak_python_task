from itertools import combinations

n = int(input())
s = input().split()
k = int(input())
print(s)
print(k)

t = list(combinations(list(s),k))

print(t)
p = 0
c = 0

l1 = []
for i in range(0,k):
    if(s[i] not in l1):
        l1.append(s[i])

print(l1)

count = 0

for i in range(0,len(l1)):
    for j in t:
        if(l1[i] in j):
            count += 1
print(len(t))
print(len(l1))
print(count)
print(count/len(t))        
