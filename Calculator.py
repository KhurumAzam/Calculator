class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self, num1, num2): return num1 + num2
    def sub(self, num1, num2): return num1 - num2
    def multi(self, num1, num2): return num1 * num2
    def div(self, num1, num2): return num1 / num2
    def pow(self, num1, num2): return num1 ** num2
    def mod(self, num1, num2): return num1 % num2
    def flo(self, num1, num2): return num1 // num2
