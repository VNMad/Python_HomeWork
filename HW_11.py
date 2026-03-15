#-----------------------------------------------------------------------------
#1.Звёздочки вместо чисел
#-----------------------------------------------------------------------------
# text = "123-456-789"
# symbols = []
# for char in text:
#     if char.isdigit():
#         symbols.append('*')
#     else:
#         symbols.append(char)
# result = ''.join(symbols)
# print("Результат:", result)
#-----------------------------------------------------------------------------
#2.Количество символов # V.2.1
#-----------------------------------------------------------------------------
# text = "Programming in python"
# print("Строка:", text)
# for char in text.casefold():
#     if text.count(char) > 1:
#         print("Символ '", char, "' встречается ", text.count(char), " раз(а)", sep="")
#     text = text.replace(char,"")
#-----------------------------------------------------------------------------
#2.Количество символов V.2.2
#-----------------------------------------------------------------------------
# text = "Programming in python".casefold()
# printed = ""
# print("Строка:", text)
# for ch in text:
#     if ch in printed:
#         continue
#     count = text.count(ch)
#     if count > 1:
#         print(f"Символ '{ch}' встречается {count} раз(а)")
#         printed += ch
#-----------------------------------------------------------------------------
#3.Увеличение чисел
#-----------------------------------------------------------------------------
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# new_symbols = []
# for char in text.split():
#     if char.replace('.', '', 1).isdigit():
#          char = str(float(char) * 10)
#          #text = text.replace(char, str(char2))
#     #new_symbols += [char]
#     new_symbols.append(char)
# new_text = " ".join(new_symbols)
# print(new_text)

# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# new_symbols = []
#
# for char in text.split():
#     if char.count('.') <= 1 and char.replace('.', '').isdigit():
# #     #if char.isdigit() or char == '.':
# #         #char2 = float(char) * 10
# #         #print(char2)
# #         #text = text.replace(char, str(char2))
#         digit = str(float(char) * 10)
#         new_symbols.append(digit)
#     else:
#         new_symbols.append(char)
# new_text = " ".join(new_symbols)
# print(new_text)

# # Домашка №11 п.3 "Увеличение чисел" одной строкой (если интересно)
# print(" ".join([str(int(x) * 10) if x.isdigit() else str(float(x) * 10) if len(
#     x.split(".")) == 2 and x.split(".")[0].isdigit() and x.split(".")[1].isdigit() else x for x in
#                "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()]))
#
#
# text = []
# for x in "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split():
#
#     if x.isdigit():
#         text += [str(int(x) * 10)]
#     elif len(x.split(".")) == 2 and x.split(".")[0].isdigit(): and x.split(".")[1].isdigit():
#              text += [str(float(x) * 10)]
#     else:
#         text += [x]
# print(" ".join(text))

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()

for i in text:
    #x = i.rstrip('.')
    if i.replace('.', '', 1).isdigit():
        i = float(i) * 10
    print(i, end=" ")

