class calculator:
    """ A simple calculator class.   """

    def add(self, a,b):
        return a+b
    
    def divide(self, a,b):
        return a/b

    def sub(self,a,b):
        return a-b
    

# main function
if __name__ == "__main__":
    calc = calculator()
    print("Addition: ", calc.add(5,3))
    print("Division: ", calc.divide(5,3))
    print("Subtraction: ", calc.sub(5,3))
