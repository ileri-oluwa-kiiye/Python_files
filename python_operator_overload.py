class myPoint:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y =  self.y + other.y
        return( x, y)

    def __ls__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y **2 )
        return self_mag< other_mag

    def __sub__(self, oth):
        x = self.x - oth.x
        y = self.y - oth.y
        return (x, y)

p1 = myPoint( 2, 3)
p2 = myPoint(4,5)
print(p1)
print(p1.__add__(p2))
print(p1.__ls__(p2))
print(p1.__sub__(p2))