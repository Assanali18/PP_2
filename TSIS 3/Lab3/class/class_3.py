class Shape():
    def Area(self):
        print("Square:", self.area)

class Rectangle(Shape):
    def __init__(self, length, weigth):
        self.area = length * weigth
        Shape.Area(self)
        
Rectangle(int(input('Enter length: ')), int(input('Enter weigth: ')))
