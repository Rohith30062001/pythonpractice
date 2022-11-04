class test:
    def __init__(self,a):
        self.a=a
 
    def display(self):
        print(self.a,"hi bro")
obj=test(10)
obj2=test(20)
obj.display()
obj2.display()
class Test:
    def display(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
obj=Test()
obj.display(5,6)
        
