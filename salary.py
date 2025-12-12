class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary

    def __str__(self):
        return f"""
        Employee Details:
        -----------------
        ID      : {self.emp_id}
        Name    : {self.name}
        Dept    : {self.dept}
        Salary  : ₹{self.salary}
        """
    # def dept_val(self,amount):
    #     if self.dept=="IT":
    #         self.salary+=amount
    #     else:
    #         print("dept not match")  
            
    def increment(self,percent):
        increment=self.salary * (10 / 100)
        self.salary+=increment
        print(percent)
        
           

# Taking input from user
id = input("Enter Employee ID: ")
name = input("Enter Name: ")
dept = input("Enter Department: ")
salary = float(input("Enter Salary: "))

        


emp = Employee(id, name, dept, salary)
emp.increment(10)
# emp.dept_val(1000) 
# Display all details
print(emp)
