#____________________________________________________________________
#1. Банковский счёт
#____________________________________________________________________
class BankAccount:


    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__validate_amount(amount)
        self.__balance += amount

    def withdrawal(self, amount):
        self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= amount

    def __validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")


account = BankAccount("Alice", 0)
try:
    account.deposit(150)
    print(f"Current balance: {account.balance}")
    account.withdrawal(-150)
except ValueError as e:
    print(f"Error: {e}")
print(f"Current balance: {account.balance}")


try:
    account.withdrawal(151)
except ValueError as e:
    print(f"Error: {e}")
print(f"Current balance: {account.balance}")

#____________________________________________________________________
#2. История операций
#____________________________________________________________________
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return self.__history

    def deposit(self, amount):
        self.__validate_amount(amount)
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdrawal(self, amount):
        self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Not enough funds.")
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def __validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")


account = BankAccount("Alice", 0)

try:
    account.deposit(150)
    account.withdrawal(100)

except ValueError as e:
    print(f"Error: {e}")

print(f"Current balance: {account.balance}")
print("Operation history:")
print("\n".join(f"\t\t{operation}" for operation in account.history))