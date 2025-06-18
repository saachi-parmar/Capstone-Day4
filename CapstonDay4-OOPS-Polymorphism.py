# Polymorphism ----------------------------------------------------

class shape:
    def area(self):
        pass
class circle(shape):
    def area(self, radius):
        return 3.14*radius*radius
class rectangle(shape):
    def area(self, length, breadth):
        return length*breadth
    
circle = circle()
rectangle = rectangle()

print('The are of the circle: ', circle.area(5))
print('The are of the rectangle: ',rectangle.area(4,5))

print("\n")