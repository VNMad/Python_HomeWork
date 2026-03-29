#____________________________________________________________________
#1. Объединение данных в строку
#____________________________________________________________________
from typing import Any

def union_data(data: list[Any]) -> str:
    """
    Takes a list of any data and returns a string with separator "|".

    :param data: List of any type.
    :return: A string with the concatenated values.
    """

    return " | ".join(map(str, data))


data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
result = union_data(data)
print(result)

#____________________________________________________________________
#2. Объединение данных в строку
#____________________________________________________________________
from typing import Any

def sum_scores(data: list[dict[str, Any]]) -> int:
    """
    Takes a list of dictionaries and returns the sum of all scores.

    :param data: List of dictionaries with keys "name" and "scores".
    :return: Sum of all scores.
    """

    return sum(map(lambda name: sum(name["scores"]), data))


data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]
result = sum_scores(data)
print("Итоговый балл:", result)