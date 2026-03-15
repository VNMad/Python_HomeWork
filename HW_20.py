#____________________________________________________________________
#1. Простое число
#____________________________________________________________________


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = 17
print(f"Число {n} {'является' if is_prime(n) else 'не является'} простым")

#____________________________________________________________________
#2. Фильтрация чисел по чётности
#____________________________________________________________________


def filter_numbers(filter_type, *args):

    if filter_type == "even":
        return [num for num in args if num % 2 == 0]
    elif filter_type == "odd":
        return [num for num in args if num % 2 != 0]
    else:
        print("Некорректный фильтр")
        return []


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

#____________________________________________________________________
#3. Объединение словарей
#____________________________________________________________________


def merge_dicts(*args):

    result = {}
    for d in args:
        result.update(d)
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

print(merge_dicts(dict1, dict2, dict3))