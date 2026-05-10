#____________________________________________________________________
#1. Класс Person
#____________________________________________________________________
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, my name is {self.name}."


person = Person("Alice")
print(person.introduce())

#____________________________________________________________________
#2. Класс Student
#____________________________________________________________________
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, my name is {self.name}."

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        text = super().introduce()
        return f"{text}\nI'm on course {self.course}."


student = Student("Alice", 2)
print(student.introduce())

#____________________________________________________________________
#3. Класс Teacher и список людей
#____________________________________________________________________.
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, my name is {self.name}."


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        text = super().introduce()
        return f"{text}\nI'm on course {self.course}."


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        return (
            f"Hello, I am professor {self.name}.\n"
            f"My subject is {self.subject}"
        )


people = [
    Student("Alice", 2),
    Teacher("Bob", "Mathematics")
]
for ppl in people:
    print(ppl.introduce())