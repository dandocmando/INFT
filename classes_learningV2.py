import turtle


class Polygon:  # initial class, this holds the default values we want to use or call
    def __init__(self, sides, name, size=100, color="black", line_thickness=1):  # constructor
        self.name = name  # this is how we initialise our variables
        self.sides = sides
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interiorAngles = (self.sides - 2) * 180
        self.angle = self.interiorAngles / self.sides

    def draw(self):
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
            turtle.pensize(self.line_thickness)


class Square(Polygon):  # Square is a child of Polygon, inherits all its values
    def __init__(self, size=100, color="black", line_thickness=1):
        super().__init__(4, "Square", size, color, line_thickness)  # super() allows access to methods and properties
        # of a parent or sibling class

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


square = Square(color="#abc123", size=100)
print(square.sides)
print(square.angle)

print(square.draw())

turtle.done()
