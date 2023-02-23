class OddorEven(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def OddorEven(self):
        try:
            if self.num1 % self.num2 == 0:
                return f"{self.num1} is Even"
            else:
                return f"{self.num1} is odd"
        except:
            return "Error in code"
