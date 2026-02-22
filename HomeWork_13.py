#____________________________________________________________________
#1. Прогрессия увеличения
#____________________________________________________________________
# numbers = (3, 7, 2, 8, 5, 10, 1)
#
# result = []
# max_digit = 0
#
# for i in numbers:
#     if i > max_digit:
#         result.append(i)
#         max_digit = i
#
# print("Кортеж по возрастанию:", tuple(result))

#____________________________________________________________________
#2. Повторяющиеся элементы v.2.1
#____________________________________________________________________
# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# checked = []
#
# for num in numbers:
#     if num not in checked and numbers.count(num) > 1:
#         print(f"Индексы элемента {num}:", end=" ")
#         for i in range(len(numbers)):
#             if numbers[i] == num:
#                 print(i, end=" ")
#         checked.append(num)
#         print()
#____________________________________________________________________
#2. Повторяющиеся элементы v.2.2
#____________________________________________________________________
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
checked = []

for num in numbers:
    if num not in checked and numbers.count(num) > 1:
        list_index = []
        for i, item in enumerate(numbers):
            if item == num:
                list_index.append(i)
        print(f"Индексы элемента {num}:", *list_index)
        checked.append(num)
