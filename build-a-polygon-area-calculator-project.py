class Rectangle:
    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Set a new width for the rectangle.
        """
        self.width = width

    def set_height(self, height):
        """
        Set a new height for the rectangle.
        """
        self.height = height

    def get_area(self):
        """
        Calculate and return the area of the rectangle.
        Area = width * height
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        Perimeter = 2 * (width + height)
        """
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """
        Calculate and return the diagonal of the rectangle.
        Diagonal = sqrt(width^2 + height^2)
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Return a string representation of the rectangle using lines of '*' characters.
        If the width or height is greater than 50, return 'Too big for picture.'
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        """
        Return the number of times the given shape (Rectangle or Square) can fit inside this rectangle.
        """
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        """
        Return the string representation of the rectangle.
        Example: 'Rectangle(width=4, height=8)'
        """
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        """
        Initialize the square with a single side. The side will be set for both width and height.
        """
        super().__init__(side, side)

    def set_side(self, side):
        """
        Set the side of the square, which sets both the width and height.
        """
        self.width = side
        self.height = side

    def set_width(self, width):
        """
        Set the width of the square, which also sets the height.
        """
        self.set_side(width)

    def set_height(self, height):
        """
        Set the height of the square, which also sets the width.
        """
        self.set_side(height)

    def __str__(self):
        """
        Return the string representation of the square.
        Example: 'Square(side=5)'
        """
        return f"Square(side={self.width})"


# Usage Example

if __name__ == "__main__":
    # Rectangle example
    rect = Rectangle(10, 5)
    print(rect.get_area())        # 50
    rect.set_height(3)
    print(rect.get_perimeter())   # 26
    print(rect)                   # Rectangle(width=10, height=3)
    print(rect.get_picture())     # Picture of the rectangle

    # Square example
    sq = Square(9)
    print(sq.get_area())          # 81
    sq.set_side(4)
    print(sq.get_diagonal())      # 5.656854249492381
    print(sq)                     # Square(side=4)
    print(sq.get_picture())       # Picture of the square

    # Rectangle fitting example
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))  # 8
