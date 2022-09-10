class Calculator:
    a = 0
    b = 0
    res = 0

    def add(self):
        self.res = self.a + self.b
        print(f"the result of the addition is {self.res}")

    def mul(self):
        self.res = self.a * self.b
        print(f"the result of the multiplication is {self.res}")

    def sub(self):
        self.res = self.a - self.b
        print(f"the result of substraction is {self.res}")

    def div(self):
        if self.b != 0:

            self.res = self.a / self.b
            print(f"the result of the division is {self.res}")
        else:
            print("please b must be distinct than zero ")
        

    
    

cal= Calculator()
cal.a = 5 
cal.b = 20
cal.mul()
print(cal.res)



cal.a = 5
cal.b = 10
cal.add()
print(cal.res)

cal.a = 20
cal.b = 60
cal.sub()

cal.a = 50 
cal.b = 0
cal.div()


