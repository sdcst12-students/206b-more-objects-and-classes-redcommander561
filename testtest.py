import math

class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []


    def discriminant(self):
        x = self.b**2 - 4*self.a*self.c
        print(x)
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the discriminant which is calculated as
        # b^2 - 4ac
        # return value should be a float type decimal
        pass
        return x


    def hasRealRoots(self):
        print('checking roots')
        if self.discriminant() > 0:
    
            print("Two roots")
        elif self.discriminant() == 0:
            
            print("One root")
        else:

            print("No real roots")
    
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine if the quadratic has real roots
        # defined when the discriminant is non negative
        # return value should be True or False
        pass
        return True or False
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        # this should require 3 positional arguments and assign the values
        # to self.a, self.b and self.c
        pass



if __name__ == "__main__":
    q1 = quadratic(1,4,4)
    assert q1.hasRealRoots() == True