n=int(input())
for i in range(n):
    for j in range(n):
        if not((i+j==n//2) or i-j==n//2 or i-j==-(n//2) or i+j==n+n//2) and(i or j>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")       
    print()
