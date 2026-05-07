#____________________________________________________________________
#1. Класс Rectangle
#____________________________________________________________________
class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def get_square(self):
        return self.w * self.h


rect = Rectangle(4, 5)

print(f"Площадь: {rect.get_square()}")

rect.width = 5
rect.height = 7

print(f"Новая площадь: {rect.get_square()}")

#____________________________________________________________________
#2. Класс Counter
#____________________________________________________________________
class Counter:
    def __init__(self):
        self.value = 0

    def next_plus(self):
        self.value += 1

    def next_minus(self):
        self.value -= 1

    def get_current(self):
        return self.value


counter = Counter()
counter.next_plus()
print(f"Значение увеличено, текущее: {counter.get_current()}")
counter.next_plus()
print(f"Значение увеличено, текущее: {counter.get_current()}")
counter.next_plus()
print(f"Значение увеличено, текущее: {counter.get_current()}")
counter.next_minus()
print(f"Значение уменьшено, текущее: {counter.get_current()}")
print(f"Текущее значение: {counter.get_current()}")
