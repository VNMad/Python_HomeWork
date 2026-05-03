#____________________________________________________________________
#1. Фабрика функций округления
#____________________________________________________________________

def make_rounder(digits: int):
    """
    Creates a rounding function with fixed number of digits.

    :param digits: Number of decimal places
    :return: Function that rounds a number
    :raises TypeError: If digits is not an integer
    :raises ValueError: If digits is negative
    """
    if not isinstance(digits, int):
        raise TypeError("Количество знаков должно быть целым числом")

    if digits < 0:
        raise ValueError("Количество знаков не может быть отрицательным")

    def round_func(number: float) -> float:
        """
        Rounds a number to predefined digits.

        :param number: Number to round
        :return: Rounded number
        """
        return round(number, digits)

    return round_func


try:
    round2 = make_rounder(2)
    round0 = make_rounder(0)

    print(round2(3.14159))
    print(round2(2.71828))
    print(round0(9.999))

except Exception as e:
    print(f"Ошибка: {e}")

#____________________________________________________________________
#2. Фабрика функций округления
#____________________________________________________________________
from datetime import datetime


def make_logger():
    """
    Creates an event logger.

    :return: Logger function
    """
    events = []

    def log_time(message: str = None) -> list:
        """
        Logs a message with current timestamp or returns all events.

        :param message: Event message
        :return: List of logged events
        :raises TypeError: If message is not a string
        """
        if message is None:
            return events

        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть строкой")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        events.append(f"{message}: {current_time}")

        return events

    return log_time


try:
    log = make_logger()

    log("Загрузка данных")
    log("Обработка завершена")
    log("Сохранение файла")

    for event in log():
        print(event)

except Exception as e:
    print(f"Ошибка: {e}")

#____________________________________________________________________
#3. Рамка вокруг вывода
#____________________________________________________________________
def frame(func):
    """
    Decorator that wraps function output with a frame.

    :param func: Function to decorate
    :return: Wrapped function
    """
    def wrapper():
        """
        Wrapper function that prints frame and calls original function.
        """
        print("-" * 50)
        func()
        print("-" * 50)

    return wrapper


@frame
def say_hello():
    """
    Prints greeting message.
    """
    print("Привет, игрок!")


say_hello()