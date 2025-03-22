class calculator:
    """ A simple calculator class.   """

    def add(self, a,b):
        return a+b
    

# main function
if __name__ == "__main__":
    calc = calculator()
    print("Addition: ", calc.add(5,3))