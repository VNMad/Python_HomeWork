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
    Custom exception for invalid figure sizes.

    Raised when:
        - value is not int or float
        - value is less than or equal to 0
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

    def _validate_value(self, name, value):

        if not isinstance(value, (int, float)):
            raise InvalidSizeError(f"{name} must be int or float: {value}")
        if value <= 0:
            raise InvalidSizeError(f"{name} must be more then 0: {value}")


class Circle(Shape):
    """
    Represents a circle.

    Attributes:
        radius (int | float): Circle radius.
    """
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self._validate_value("Radius", value)
        self.__radius = value

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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_value("Width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_value("Height", value)
        self.__height = value

    def area(self):
        return self.width * self.height


try:
    shapes = [Circle(3), Rectangle(-4, 5), Circle("abc")]
    print("\n".join(f"Area: {shape.area():.2f}" for shape in shapes))

except InvalidSizeError as e:
    print(f"Error: {e}")