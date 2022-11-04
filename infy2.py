a="000"
string="xyz"
new=""
for i in range(len(string)):
    ele=ord(string[i])
    if a[i]==str(0):
        new=new+chr(ele)
    if a[i]==str(1):
        new=new+chr(ele+32) 