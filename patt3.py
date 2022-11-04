n=9
for i in range(n):
    for j in range(n):
        if((i<=n//2) and (j<=n//2)and(i+j>=n//2))or((i<=n//2)and(j>=n//2)and(i-j>=-(n//2))):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()