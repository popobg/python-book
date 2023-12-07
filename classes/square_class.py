#! /usr/bin/env python3

class Square:
    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, l):
        self.__length = l

    def area(self):
        return (self.__length **2)

class Button(Square):
    def __init__(self, x, y):
        # coords of the upper left point of the square
        self.__x = x
        self.__y = y
        self.__label = ""
        Square.__init__(self, 10)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self. __y

    def get_label(self):
        return self.__label

    def get_coords(self):
        return (self.__x, self.__y)

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__x = y

    def set_label(self, s):
        """set the value of a text label to be drawn to s"""
        if isinstance(s, str):
            self.__label = s

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def center(self):
        """return the center of the square from the coords of the point we have"""
        cent_x = (self.__x + (self.__x + self.get_length())) / 2
        cent_y = (self.__y + (self.__y + self.get_length())) / 2
        return (cent_x, cent_y)

sqr = Button(0, 0)
print(sqr.center())
print(sqr.get_label())
sqr.set_label("coucou")
print(sqr.get_label())