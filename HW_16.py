#____________________________________________________________________
#1. Оценки текстом
#____________________________________________________________________
grades = [5, 3, 4, 2, 1, 5, 3]
print([[item, ('отлично' if item==5 else 'хорошо' if 3<=item<=4 else 'неудовлетворительно')]
       for item in grades])

#____________________________________________________________________
#2. Правильные скобки
#____________________________________________________________________
#string = "({[}])"
string = "([({}()){}])"
stack = []

for char in string:
    if char in '([{':
        stack.append(char)
    elif ((char == ')' and stack and stack[-1] == '(') or
          (char == ']' and stack and stack[-1] == '[') or
          (char == '}' and stack and stack[-1] == '{')):
        stack.pop()
    else:
        print("Валидны: False")
        break
else:
    if stack:
        print("Валидны: False")
    else:
        print("Валидны: True")

#-------------------- Teacher Variant
# test = '({[}])'
# stack = []
#
# brackets_valid = {
#     '(': ')',
#     '[': ']',
#     '{': '}'
# }
#
# is_valid = True
# for char in test:
#     if char in brackets_valid.keys():
#         stack.append(char)
#
#     elif char in brackets_valid.values():
#         if stack:
#             last_open_char = stack.pop()
#             if brackets_valid[last_open_char] != char:
#                 is_valid = False
#                 break
# if stack:
#     is_valid = False
#
# print(f'Is valid: {is_valid}')