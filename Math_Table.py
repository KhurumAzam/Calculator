class Math_Table(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def print_table(self, operator):
        for i in range(super().num1):
            for j in range(super().num2):
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
