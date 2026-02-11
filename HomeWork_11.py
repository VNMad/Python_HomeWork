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
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
new_symbols = []
for char in text.split():
    if char.count('.') <= 1 and char.replace('.', '').isdigit():
         char = str(float(char) * 10)
         #text = text.replace(char, str(char2))
    #new_symbols += [char]
    new_symbols.append(char)
new_text = " ".join(new_symbols)
print(new_text)

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