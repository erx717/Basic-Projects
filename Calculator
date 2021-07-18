import math

class Calculator():
    def __init__(self):
        self.system = True

    def select(self):
        selection = self.menu()
        if selection != 6:
            number = self.selectNumber()

        if selection == 1:
            self.factorial(number)
        elif selection == 2:
            self.floor(number)
        elif selection == 3:
            self.ceil(number)
        elif selection == 4:
            self.sqrt(number)
        elif selection == 5:
            self.pow(number)
        elif selection == 6:
            self.exit()

    def selectNumber(self):
        number = 0
        while number == 0:
            try:
                number = float(input("Number:\n"))
            except:
                pass
        return number

    def menu(self):
        print("1. Factorial\n2. Floor\n3. Ceil\n4. Square Root\n5. Power\n6. Exit\n")
        selection = 0
        while selection < 1 or selection > 6:
            try:
                selection = int(input("Selection: (1-6)\n"))
            except:
                pass
        return selection

    def exit(self):
        print("Calculator Has Been Stopped\n")
        self.system = False

    def factorial(self, number):
        number = int(number)
        print(f"Factorial of the {number} is {math.factorial(number)}\n")

    def floor(self, number):
        print(f"Floor of the {number} is {math.floor(number)}\n")

    def ceil(self, number):
        print(f"Ceil of the {number} is {math.ceil(number)}\n")

    def sqrt(self, number):
        print(f"Square root of the {number} is {math.sqrt(number)}\n")

    def pow(self, number):
        power = 0
        while power == 0:
            try:
                power = int(input("Power:\n"))
            except:
                pass
        print(f"{power}. Power of the {number} is {math.pow(number, power)}\n")

calculator = Calculator()
while calculator.system:
    calculator.select()

