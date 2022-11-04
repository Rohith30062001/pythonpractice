n=int(input())
for i in range(n):
    for j in range(n):
        if(i<=n//2):
            if(j<=n//2):
                if(i+j<n//2):
                    print("*",end=" ")
            else:
                
                print(" ",end=" ")       
    print()
