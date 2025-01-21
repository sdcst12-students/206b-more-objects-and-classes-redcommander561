
#!python3
import math
class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []

    def discriminant(self):
        x = self.b**2 - 4*self.a*self.c
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the discriminant which is calculated as
        # b^2 - 4ac
        # return value should be a float type decimal
        pass
        return x
   
    def hasRealRoots(self):
        if self.discriminant() > 0:
            print("Two roots")
            return True
        elif self.discriminant() == 0:
            print("One root")
            return True
        else:
            print("No real roots")
            return False
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine if the quadratic has real roots
        # defined when the discriminant is non negative
        # return value should be True or False
        
    def isFactorable(self):
        x = [1,4,9,16,49,64,81,100,]
        if self.discriminant() in x:
            return True
        elif self.discriminant() >= 0 and math.isqrt(self.discriminant())**2 == self.discriminant():
            return True
        else:
            return False
        
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine if the quadratic can be factored
        # quadratic can be factored if the discriminant is a perfect square
        # return value is True or False
        
    def calcRoots(self):
        #google to the rescue
        if not self.hasRealRoots():
            self.roots = []
            return self.roots
        
        d = self.discriminant()
        if d == 0:
            root1 = root2 = -self.b / (2 * self.a)
        else:
            root1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        self.roots = sorted([round(root1, 2), round(root2, 2)])
        print(self.roots)
        return self.roots
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the roots of the quadratic if
        # the quadratic has real roots
        # should make use of the class methods:
        # self.hasRealRoots()
        # self.discriminant
        # method does not have a return value
        # but should store the values of the roots in the
        # list self.roots
        # list should be sorted in ascending order
        # roots should be rounded to 2 decimal places

    def axisOfSymmetry(self):
        what = -self.b / (2 * self.a)
        return what
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the x value that is for the equation
        # of the axis of symmetry
        # should return the x value for the axis of symmetry
       

    def vertex(self):
        x_vertex = -self.b / (2 * self.a)
        y_vertex = self.a * x_vertex**2 + self.b * x_vertex + self.c
        return [round(x_vertex, 2), round(y_vertex, 2)]
        # requires no positional arguments
        # will make use of class properties a,b and c
        # to determine the x,y value of the vertex
        # should return the a list with the x and y coordinates of the vertex
        
       
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        # this should require 3 positional arguments and assign the values
        # to self.a, self.b and self.c
        pass


if __name__ == "__main__":
    q1 = quadratic(1, 4, 4)
    q1.calcRoots() 
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2, -2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2, 0]

    q2 = quadratic(1, 1, -6)
    q2.calcRoots()  
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.roots == [-3, 2]
    assert q2.axisOfSymmetry() == -0.5
    assert q2.vertex() == [-0.5, -6.25]

    q3 = quadratic(1, 1, 10)
    q3.calcRoots() 
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1, 10, 1)
    q4.calcRoots()  
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.roots == [-9.9, -0.1]
    assert q4.axisOfSymmetry() == -5
    assert q4.vertex() == [-5, 24]