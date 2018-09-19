import sys

s = "AABCAAADA"
k = 3
l = []

for i in range(0,len(s),k):
        l.append(s[i:k])
        print(s[i:k])
        k = k * 2

        

s1 = ""
for j in l:
        for k in j:
                if(k not in s1):
                       s1 = s1 + k         
                
        print(s1)
        s1 = ""
