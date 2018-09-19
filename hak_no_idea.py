m_n = input().split()
print(m)
print(n)
N = []
A = []
B = []
hap = 0

N = (input().split())
A = (input().split())
B = (input().split())

for i in N:
    if(i in A):
        hap += 1
    elif(i in B):
        hap -= 1
        

print (hap)
