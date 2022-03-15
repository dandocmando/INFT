import turtle


class Polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=1):
        self.name = name
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
        turtle.done()


square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)

print(pentagon.sides)
print(pentagon.name)

hexagon = Polygon(6, "Hexagon", 60, color="red")
hexagon.draw()
