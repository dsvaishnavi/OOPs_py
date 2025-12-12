class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
        
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    
    def __add__(self,other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return '{}/{}'.format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return '{}/{}'.format(temp_num,temp_den)
    
    
n1 = int(input("Enter numerator for first fraction: "))
d1 = int(input("Enter denominator for first fraction: "))

n2 = int(input("Enter numerator for second fraction: "))
d2 = int(input("Enter denominator for second fraction: "))

op = input("Enter operation (+ or -): ")
x = Fraction(n1, d1)
y = Fraction(n2, d2)

if op == "+":
    print("Result =", x + y)
elif op == "-":
    print("Result =", x - y)
else:
    print("Invalid operation")
