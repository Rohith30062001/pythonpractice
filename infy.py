s=input()
n=len(s)
print(n)
it=2**n
lst=list()
for i in range(0,it):
    lst.append(
        decimaltob(i))
    
def decimaltob(i):
    if i>=1:
        decimaltob(i//2)
        k=i%2
        return k
    