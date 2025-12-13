class Calci:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def __add__(self,new):
        new = self.a+self.b
        print(new)
    

    
a=int(input("Enter first number "))
b=int(input("Enter second number "))



x=Calci(a,b)
