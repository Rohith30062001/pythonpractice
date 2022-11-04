n=9
for i in range(n):
    for j in range(n):
        if((i<=n//2)and(j<=n//2)and(i+j>=n)) or(i<n//2)and(j>=n//2)and(i-j>=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()