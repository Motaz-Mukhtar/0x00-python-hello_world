#!/usr/bin/python3
# rectangle.py
"""Define Rectangle Class"""
from base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilize The Attributes, and set it as
            Private Attributes

            Args:
                width (int): width of the Rectangle
                height (int): height of the Rectangle
                x (int): Horazental of the Rectangle
                y (int): Vertical of the Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Getter of the width Attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width Attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the height Attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height Attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of the x Attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of the x Attribute"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of the y Attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y Attribute"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return The Area value for The instance
        """
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance in stdout"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return The __str__ of the Rectangle"""
        s = f"[Rectangle] ({self.id}) {self.__x}"
        st = s + f"/{self.__y} - {self.__width}"
        return st + f"/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute:

            Args:
                *args (list): the argument
                **kwargs (dcit): key/value

            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        #**kwargs
        if kwargs != None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        # *args
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
        
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance"""
        string1 = "'x': {}, 'y': {}, ".format(self.__x, self.__y)
        string2 = "'id': {}, 'height': {}, ".format(self.id, self.__height)
        strgin4 = string1 + string2 + "'width': {}".format(self.__width)
        string5 = '{' + strgin4 + '}'
        return eval(string5)
