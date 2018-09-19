n = int(input()) - 1
z = 1
f = int(n * (n + 1)/2)

for i in range(1, f + 1):
    print(z, end = "")
    if((z*(z+1))/2==i ):
        
        z+=1
        print()
