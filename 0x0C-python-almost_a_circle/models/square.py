#!/usr/bin/python3
"""Square Class"""
from asyncio import protocols
from ctypes import sizeof
from ctypes.wintypes import SIZE
from msilib.schema import PublishComponent
from multiprocessing.sharedctypes import Value
from turtle import width
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)
    
    @property
    def size(self):
        """Get width/height Attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of the width/height Attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.heigth = value
    
    def __str__(self):
        """__str__ Method for Square Class"""
        string = f"[Square] ({self.id}) {self.x}/"
        return string + f"{self.y} - {self.width}"
    
    def update(self, *args, **kwargs):
        """update attribute of Square instance:

            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute

            Args:
                args (list): list of argument
                kwargs (dict): key/value argument

        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance"""
        string1 = "'id': {}, 'x': {}, ".format(self.id, self.x)
        string2 = "'size': {}, 'y': {}, ".format(self.size, self.y)
        string3 = '{' + string1 + string2 + '}'
        return eval(string3)



# {'id': 1, 'x': 2, 'size': 10, 'y': 1}
# {'id': 1, 'x': 2, 'size': 10, 'y': 1}


if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
