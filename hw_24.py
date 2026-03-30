#____________________________________________________________________
#1. Сумма цифр числа
#____________________________________________________________________
#from functools import lru_cache

#@lru_cache(maxsize=None)
def sum_digits(n: int) -> int:

    if n == 0:
        return 0

    return sum_digits(n // 10) + n % 10


num = 43197
print(sum_digits(num))

#____________________________________________________________________
#2. Сумма вложенных чисел
#____________________________________________________________________
from typing import Any

def sum_num(data: list[Any]) -> int:
    summa = 0
    for i in data:
        if isinstance(i, list):
            summa += sum_num(i)
        else:
            summa += i
    return summa


nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(sum_num(nested_numbers))