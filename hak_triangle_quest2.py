import sys

a = int(input())

for i in range(0,a):
    
    for j in range(1,i+2):
        sys.stdout.write("%s" % j)  
    
    for k in range(i,0,-1):
        sys.stdout.write("%s" % k)

    print()

