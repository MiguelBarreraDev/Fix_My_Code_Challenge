#!/usr/bin/python3
"""This module provide a Class to instance geometry objects"""


class Square():
    """Provide methods fto calculate of the are and perimiter"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Constructor definition"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Permiter of my square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Representing of my object"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
