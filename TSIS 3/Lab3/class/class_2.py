class Shape():
    def Area(self):
        print('Square:', self.area)

class Square(Shape):
    def __init__(self, length):
        self.area = length**2
        Shape.Area(self)
        
Square(int(input('Enter length of square: ')))




