#!/usr/bin/python3
# square.py
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get width/height Attribute"""
        return self.width

    @size.setter
    def size(self, value):
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
        # **kwargs
        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        # *args
        elif len(args) > 0:
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
