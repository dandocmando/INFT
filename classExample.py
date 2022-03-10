import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x  # takes outside variable / input x and turns it into a var local to Class Point
        self.y = y

    def __add__(self, other):  # overloads the + sign, allowing its use on two points which normally wouldn't add
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.x + other.y
            return Point(x, y)
        else:
            x = self.x + other
            y = self.y + other
            return Point(x, y)

    def plot(self):
        plt.scatter(self.x, self.y)


#  ex1
# a = Point(1, 1)
# b = Point(2, 2)
# c = a + b

# print(c.x, c.y)

a = Point(0, 2)
d = a + 5

print(d.x, d.y)
