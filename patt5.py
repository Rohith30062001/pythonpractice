n=7
for i in range(n):
    for j in range(n):
        if(i==j)or(i+j==n-1):
            print(chr(65+j),end=" ")
        else:
            print(" ",end=" ")
    print()