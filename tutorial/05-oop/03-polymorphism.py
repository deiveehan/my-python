class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function that uses polymorphism
def print_area(shape):
    print(shape.area())

rect = Rectangle(10, 5)
circle = Circle(7)

print_area(rect)   # Outputs rectangle's area
print_area(circle) # Outputs circle's area
