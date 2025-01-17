import math

class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []

    def discriminant(self):
        
        return self.b**2 - 4*self.a*self.c

    def hasRealRoots(self):
        
        return self.discriminant() >= 0

    def isFactorable(self):
        
        d = self.discriminant()
        return d >= 0 and math.isqrt(d)**2 == d

    def calcRoots(self):
        
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
        return self.roots

    

    

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

if __name__ == "__main__":
    q1 = quadratic(1, 4, 4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.roots == [-2, -2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2, 0]

    q2 = quadratic(1, 1, -6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.roots == [-3, 2]
    assert q2.axisOfSymmetry() == -0.5
    assert q2.vertex() == [-0.5, -6.25]

    q3 = quadratic(1, 1, 10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.roots == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1, 10, 1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.roots == [-9.9, -0.1]
    assert q4.axisOfSymmetry() == -5
    assert q4.vertex() == [-5, 26]
