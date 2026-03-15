#____________________________________________________________________
#1. Реверс словаря
#____________________________________________________________________
data = {"a": 1, "b": 2, "c": 1, "d": 3}
new_dict = {}

for key, value in data.items():
#    if value not in new_dict:
#        new_dict[value] = [key]
#    else:
#        new_dict[value].append(key)
    new_dict.setdefault(value, []).append(key)
print(f"Перевернутый словарь:", new_dict)

#____________________________________________________________________
#2. Счётчик букв в словах
#____________________________________________________________________
words = ["anna", "bennet", "john"]
res = {}

for word in words:
    res.setdefault(word, {})
    for char in word:
        res[word].get(char, 0) + 1
        #res[word].setdefault(char, 0)
        #res[word][char] += 1
print(res)

#____________________________________________________________________
#3. Распределение студентов по группам
#____________________________________________________________________

students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

grades = [85, 70, 50, 0]
result = {}

for group in groups:
    result.setdefault(group, {})

for student, score in students.items():
    for group, min_score in zip(groups, grades):
        if score >= min_score:
            result[group][student] = score
            break

print(f"Распределение по группам:\n{result}")