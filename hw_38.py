#____________________________________________________________________
#1. Фигуры и площади
#____________________________________________________________________
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class for geometric shapes.

    Methods:
        area(): Returns area of shape.
    """

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    """
    Represents a circle.

    Attributes:
        radius (int | float): Circle radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """
    Represents a rectangle.

    Attributes:
        width (int | float): Rectangle width.
        height (int | float): Rectangle height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(3), Rectangle(4, 5)]
print("\n".join(f"Area: {shape.area():.2f}" for shape in shapes))

#____________________________________________________________________
#2. Проверка размеров фигур
#____________________________________________________________________
from abc import ABC, abstractmethod
import math


class InvalidSizeError(ValueError):
    """
    Raised when figure size is invalid.
    """
    pass


class Shape(ABC):
    """
    Abstract class for geometric shapes.

    Methods:
        area(): Returns area of shape.
    """

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    """
    Represents a circle.

    Attributes:
        radius (int | float): Circle radius.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError(f"Radius must be more then 0: {radius}")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """
    Represents a rectangle.

    Attributes:
        width (int | float): Rectangle width.
        height (int | float): Rectangle height.
    """

    def __init__(self, width, height):
        if width <= 0:
            raise InvalidSizeError(f"Width must be more then 0: {width}")

        if height <= 0:
            raise InvalidSizeError(f"Height must be more then 0: {height}")

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


try:
    #shapes = [Circle(3), Rectangle(4, 5)]
    shapes = [Circle(3), Rectangle(-4, 5)]
    print("\n".join(f"Area: {shape.area():.2f}" for shape in shapes))
except InvalidSizeError as error:
    print(f"Error: {error}")