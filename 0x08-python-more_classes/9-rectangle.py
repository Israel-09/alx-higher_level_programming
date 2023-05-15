#!/usr/bin/python3
"""module to create a square class"""


class Rectangle:
    """a class that defines a square"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        __init__: initializes the properties of a square object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if type(width) is not int and type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0 and height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        width(getter): returns the value of attribute width
        width(Setter): sets the value of size to new width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height(getter): returns the value of attribute height
        height(Setter): sets the value of size to new height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def print_rect(self):
        """creates a string representing
        the shape of a rectangle"""
        rectangle = []
        if self.__height == 0 or self.__width == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i < self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """computes the biggest rectangle between rect1 and rect2
        based on their area

        Args:
            rect1 (Rectangle): first rectangle object
            rect2 (Rectangle): second rectangle object

        Raises:
            TypeError: if rect1 or rect2 is not of type Rectangle.
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    def __del__(self):
        """prints a statement whenever an instance
        of a class is deleted and reduces number of instaces
        by one
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        '''creates a square setting height and width to size

        Args (int): size of the square

        Returns: a square with size of size
        '''
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size < 0:
            raise ValueError('width must be >= 0')
        new_obj = cls()
        new_obj.height = size
        new_obj.width = size
        return new_obj

    def __str__(self):
        """string representations of a rectangle object
        Return:
            The string representaion of the rectangle object
        """
        return (self.print_rect())

    def __repr__(self):
        """official string representations of a rectangle object
        Return:
            The official string representaion of the rectangle object
        """
        return (f"Rectangle({self.__width}, {self.__height})")
