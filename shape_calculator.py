class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        self.height = height
        if type(self) is not Rectangle:
            self.height = width

    def set_side(self, side):
        self.width = self.height = side

    def set_width(self, width):
        self.width = width
        if type(self) is not Rectangle:
            self.height = width

    def set_height(self, height):
        self.height = height
        if type(self) is not Rectangle:
            self.width = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return f'{"*" * self.width}\n' * self.height

    def get_amount_inside(self, shape):
        if shape.width != shape.height:
            side = shape.width * shape.height
        else:
            side = shape.width ** 2
        return int((self.width * self.height) / side)

    def __str__(self):
        if type(self) is not Rectangle:
            return f'Square(side={self.width})'
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):

    pass
