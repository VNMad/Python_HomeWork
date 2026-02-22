#____________________________________________________________________
#1. Число в конце
#____________________________________________________________________
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# new_strings = []
# for string in strings:
#     if string.rstrip("0123456789").isalpha():
#         new_strings.append(string)
# print("Строки с цифрами только в конце: ", new_strings)

#____________________________________________________________________
#2. Удаление кратных
#____________________________________________________________________
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# n = int(input("Введите число для удаления кратных ему элементов: "))
# new_numbers = []
# for i in numbers:
#     if i % n != 0:
#         new_numbers.append(i)
# print("Список без кратных значений:", new_numbers)

#____________________________________________________________________
#3. Порядок четных
#____________________________________________________________________
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
even.sort(reverse=True)

even_i = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = even[even_i]
        even_i += 1
print("Список после сортировки:", numbers)

