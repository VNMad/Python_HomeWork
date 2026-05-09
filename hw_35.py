#____________________________________________________________________
#1. Счётчик экземпляров
#____________________________________________________________________
class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users


user1 = User("user_1", "123")
user2 = User("user_2", "456")

print(f"Total users: {User.get_total()}")

#____________________________________________________________________
#2. Проверка данных пользователя
#____________________________________________________________________

class User:
    def __init__(self, username, password):
        if not isinstance(username, str) or len(username) == 0:
            raise ValueError(f"Invalid username: '{username}'")

        if not isinstance(password, str) or len(password) < 5:
            raise ValueError(f"Invalid password: '{password}' must be string, equal or more than 5 symbols")

        self.username = username
        self.password = password

    def __str__(self):
        return f"User: {self.username}"


users = [
    ("alice", "secret"),
    ("bob", "qwe")
]

for username, password in users:
    try:
        user = User(username, password)

    except ValueError as error:
        print(f"User: {username}")
        print(f"ValueError: {error}")

    else:
        print(user)
        print("Password: Ok")