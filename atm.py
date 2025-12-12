class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    
    def menu(self):
        while True:
            user_input=input("""
 How would you like to proceed?
 1.Enter 1 too create pin :
 2.Enter 2 to deposit : 
 3.Enter 3 to withdraw : 
 4.Enter 4 for  balance: 
 5.Enter 5 to exit: 
 """)
    
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.balance_atm()
            else:
                print("exit")
                
            
    def create_pin(self):
        self.pin=input('enter your pin: ')
        print("pin set")
        
    def deposit(self):
        temp=input("enter your pin: ")
        if temp== self.pin:
            amount = int(input('enter amt: '))   
            self.balance=self.balance+amount
            print("deposit succesfull")
        else:
            print("invalid pin")
            
    def withdraw(self):
        temp=input("enter your pin: ")
        if temp== self.pin:
            amount = int(input('enter amt: '))   
            if amount < self.balance:
                self.balance =self.balance - amount
                print("successful")
            else:
                print("insufficient")
        else:
            print("invalid pin")
            
    def balance_atm(self):
        temp=input("enter your pin: ")
        if temp== self.pin:
            print(self.balance)
        else:
            print("incorrect")
        
atm = Atm()
