#____________________________________________________________________
#1. Генератор Фибоначчи
#____________________________________________________________________
from typing import Any, Generator


def fibonacci():
    """
    Generates an infinite Fibonacci sequence.

    :return: Next number in Fibonacci sequence
    """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def validate_limit(value: str) -> int:
    """
    Validates user input and converts it to integer.

    :param value: Input value as string
    :return: Positive integer
    :raises ValueError: If input is not a valid positive integer
    """
    if not value.isdigit():
        raise ValueError("Введено некорректное число")

    limit = int(value)

    if limit <= 0:
        raise ValueError("Число должно быть больше 0")

    return limit


while True:
    try:
        user_input = input("Введите кол-во: ")
        limits = validate_limit(user_input)

        fib_gen = fibonacci()

        for _ in range(limits):
            print(next(fib_gen))

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print("Error:", e)
    else:
        break
#____________________________________________________________________
#2. Генератор уникальных элементов
#____________________________________________________________________
def unique_gen(n: list) -> Generator[Any, Any, None]:
    """
    Generates unique elements from the input list preserving order.

    :param n: List of elements
    :return: List of unique elements
    :raises TypeError: If input is not a list
    """
    if not isinstance(n, list):
        raise TypeError("Аргумент должен быть списком")

    wo_repeat = set()

    for i in n:
        if i not in wo_repeat:
            wo_repeat.add(i)
            yield i


data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

try:
    result = list(unique_gen(data))
except Exception as e:
    print(f"Ошибка: {e}")
else:
    print(result)