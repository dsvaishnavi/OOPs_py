class Student:
    def __init__(self,name,rollno,department):
        self.name =name
        self.rollno=rollno
        self.department=department
        
       
   
        
    def marks(self):
        self.sub1=int(input('enter marks1 '))
        self.sub2=int(input("enter marks2 "))
        self.sub3=int(input("enter marks3 "))
        print(self.sub1,self.sub2,self.sub3)
    
    def percentage_marks(self):
        total = self.sub1 +self.sub2 +self.sub3
        percentage = (total/300) * 100
        print( percentage)

    def rank(self):
        if self.percentage <= 30:
            print("you failed")
        
        
        
name=input("enter your name: ")
rollno= int(input("enter roll no: "))
department=input("enter your department : ")
# percentage= int(input("enter percentage: "))
    
        
        
x=Student(name,rollno,department)
x.marks()
x.percentage_marks()
print(x)