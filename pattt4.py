n=10
for i in range(n):
    for j in range(n):
        if((i<=n//2)and(j<=n//2)and(i-j<=0)) or (i<=n//2)and(j>=n//2)and(i+j<=n):
            print(chr(65+j),end=" ")
        else:
            print(" ",end=" ")
    print()
            