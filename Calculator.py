class Calculator:
    def add(self, num1, num2): return num1 + num2
    def sub(self, num1, num2): return num1 - num2
    def multi(self, num1, num2): return num1 * num2
    def div(self, num1, num2): return num1 / num2
    def pow(self, num1, num2): return num1 ** num2
    def mod(self, num1, num2): return num1 % num2
    def flo(self, num1, num2): return num1 // num2

    def print_table(self, operator):
        for i in range(999):
            for j in range(999):
                try:
                    if operator == "Addition":
                        print(i, " + ", j, " = ", self.add(i,j))
                    elif operator == "Subtraction":
                        print(i, " - ", j, " = ", self.sub(i,j))
                    elif operator == "Multiplication":
                        print(i, " * ", j, " = ", self.multi(i,j))
                    elif operator == "Division":
                        print(i, " / ", j, " = ", self.div(i,j))
                    elif operator == "Power":
                        print(i, " ** ", j, " = ", self.pow(i,j))
                    elif operator == "Modulus":
                        print(i, " % ", j, " = ", self.mod(i,j))
                    elif operator == "Float":
                        print(i, " // ", j, " = ", self.flo(i,j))
                except:
                    print ("An error occurred")