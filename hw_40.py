#____________________________________________________________________
#1. Электронное письмо
#____________________________________________________________________
from datetime import datetime


class Email:


    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __gt__(self, other):
        if not isinstance(other, Email):
            return NotImplemented
        return self.date > other.date


e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(f"{e1} \n")
print(f"{e2} \n")

print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)

#____________________________________________________________________
#2. Класс для работы с деньгами
#____________________________________________________________________
class Money:


    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"${self.amount}"

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount + other.amount)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(max(self.amount - other.amount, 0))


money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)
