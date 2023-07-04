
class Calculator():

    def add(self,a,b):

        return a + b 
    
    def subtract(self,a,b):

        return a - b
    
    def multiply(self,a,b):

        return a * b
    
    def divide(self,a,b):

        try:
            return a / b
        
        except:

            print("0으로 나눌 수 없습니다.")
            return

calculator = Calculator()

print(calculator.add(1,2)) #1+2

print(calculator.subtract(2,1)) #2-1

print(calculator.multiply(3,4)) #3*4

print(calculator.divide(4,0)) #4/0
