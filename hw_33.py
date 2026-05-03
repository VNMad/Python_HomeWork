#____________________________________________________________________
#1. Среднее время выполнения
#____________________________________________________________________
import time


def measure_time(func):
    """
    Decorator that measures average execution time over 5 runs.
    """
    def wrapper():
        total_time = 0
        n = 5
        for _ in range(n):
            start = time.time()
            result = func()
            end = time.time()
            total_time += (end - start)

        avg_time = total_time / n

        print(f"Среднее время выполнения для {n} вызовов: {avg_time:.2f} секунд")
        print(f"Результат: {result}")

    return wrapper


@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()

#____________________________________________________________________
#2. Среднее время выполнения с количеством вызовов
#____________________________________________________________________
import time


def measure_time(repeats):
    """
    Decorator that measures average execution time over N runs.

    :param repeats: Number of function calls
    """
    def decorator(func):
        def wrapper():
            total_time = 0

            for _ in range(repeats):
                start = time.time()
                result = func()
                end = time.time()
                total_time += (end - start)

            avg_time = total_time / repeats

            print(f"Среднее время выполнения для {repeats} вызовов: {avg_time:.2f} секунд")
            print(f"Результат: {result}")

        return wrapper

    return decorator


@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()