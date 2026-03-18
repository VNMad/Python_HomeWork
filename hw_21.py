#____________________________________________________________________
#1. Повторения букв
#____________________________________________________________________
from collections import Counter

def letter_counting(text):
    return dict(Counter(char for char in text.lower() if char.isalpha()))


text = "Programming is fun!"
print(letter_counting(text))

#____________________________________________________________________
#2. Группировка студентов по классам
#____________________________________________________________________
from collections import defaultdict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
result = defaultdict(list)
for class_name, student in students:
    result[class_name].append(student)
print(dict(result))