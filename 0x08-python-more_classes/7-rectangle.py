#!/usr/bin/python3
"""Contains the Rectangle class implementation"""


class Rectangle():
    """Defines a rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructs a new rectangle
        Args:
            width (int, optional): width of the rectangle
            height (int, optional): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        res = ""
        for i in range(self.__height):
            for row in range(self.__width):
                try:
                    res += str(self.print_symbol)
                except Exception:
                    res += type(self).print_symbol
            if i < self.__height - 1:
                res += "\n"
        return res

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
