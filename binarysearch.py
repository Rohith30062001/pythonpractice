def binarysearch(a,key,start,end):
    if end>=start:
        mid=(start+end)//2
        if(a[mid]==key):
            print("key found")
            return 
        elif(a[mid]>key):
            return binarysearch(a,key,start,mid)
        elif(a[mid]<key):
            return binarysearch(a,key,mid+1,end)
        else:
            print("element not found")
inp=input()
a=""
n=len(a)
for i in inp:
    if (i==" "):
        pass
    else:
        a=a+i
key=input("enter element to find:-")
binarysearch(a,key,0,n-1)

