class Salary:
    def __init__(self,name,id,salary,depart,years):
        self.name= name
        self.id = id
        self.salary = salary
        self.depart=depart
        self.years=years
    
    def increment(self,percent):
        percent = (self.salary * percent ) //100
        self.salary += percent
        print(f"you salary is {self.salary} congratsss!!!")
                
    def experienced(self):
        if self.years <=3:
            print("you are fresher")
        elif self.years == 4:
            print("you r intermediate")
        else:
            print("you are pro")









name=input("enter your name: ")
id=int(input("enter employee id: "))
salary=float(input("enter salary amount: "))
depart=input("enter your department: ")
percent = float(input("Enter increment percentage: "))
years=int(input("enter your experience: "))

x=Salary(name,id,salary,depart,years)


x.increment(percent)
x.experienced()

print(x)