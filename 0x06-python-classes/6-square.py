#!/usr/bin/python3
"""Implementation of Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructs a new square
        Args:
            size(int, optional): size of the Square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of a square object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of a square object"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) < 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of a Square object
        Returns:
            The area of a Square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square object using # characters"""
        if self.size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
