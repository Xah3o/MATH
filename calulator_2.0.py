class Calculator:
    res = 0


    def add(self, *args):
        self.res = 0
        for item in args:
            self.res += item
        print(f"the result of the addition is {self.res}")


    def sub(self, *args):
        self.res = 0
        i = 0

        for item in args:
            if i == 0:
                self.res += item
            else:
                self.res -= item
            i += 1
        print(f"the result of the substraction is {self.res}")

    def mul(self, *args):
        self.res = 0
        i= 0
        for item in args:
            if i == 0:
                self.res += item
            else:
                self.res *= item
            if item == 0:
                self.res = 0
                break
            i += 1    
        print(f"the result of multiplication is {self.res}")

    def div(self, *args):
        self.res = 0
        i = 0
        for item in args:
            if i == 0:
                self.res += item
            else:
                if item ==0:
                    self.res = 0
                    print("the numbers must be distinct than zero")
                    break
                self.res /= item
            i += 1
        print(f"the result of the division is {self.res}")                       
cal = Calculator()

cal.add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

cal.sub(2, 2)

cal.mul(0, 10, 20, 123123, 1231231231231231)
cal.mul(10, 20, 123123, 1231231231231231)


cal.div(10, 20, 0, 1231231231231231)
cal.div(10, 5)
