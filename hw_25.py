#____________________________________________________________________
#1. Деление без ошибок
#____________________________________________________________________,
def div(a: int, b: int) -> float:
    """
    Performs division of two numbers.

    :param a: Dividend
    :param b: Divisor
    :return: The quotient of the division
    """
    return a / b


while True:
    try:
        a_num = int(input("Введите делимое: "))
        b_num = int(input("Введите делитель: "))

        result = div(a_num, b_num)

    except ValueError:
        print("Ошибка: Введено некорректное число")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
    except Exception as e:
        print("Error:", e)
    else:
        print(f"Результат: {result:.3f}")
        break

#____________________________________________________________________
#2. Логирование ошибок
#____________________________________________________________________
import logging

logging.basicConfig(
    filename="errors_divide.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s", encoding="utf-8"
    )


def div(a: int, b: int) -> float:
    """
    Performs division of two numbers.

    :param a: Dividend
    :param b: Divisor
    :return: The quotient of the division
    """
    return a / b


while True:
    try:
        a_num = int(input("Введите делимое: "))
        b_num = int(input("Введите делитель: "))

        result = div(a_num, b_num)

    except ValueError:
        print("Ошибка: Введено некорректное число")
        logging.error("Ошибка: Введено некорректное число")

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
        logging.error("Ошибка: Деление на ноль")

    except Exception as e:
        print("Error:", e)
        logging.error(f"Error: {e}")

    else:
        print(f"Результат: {result:.3f}")
        break
