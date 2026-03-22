#____________________________________________________________________
#1. Выбор заказов
#____________________________________________________________________
def process_orders(arg):
    filtered = filter(lambda x: x["price"] > 500, arg)
    return sorted(map(lambda x: x["product"], filtered))

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

print(*process_orders(orders), sep="\n")

#____________________________________________________________________
#2. Статистика продаж
#____________________________________________________________________
def sales_ord(arg):

    dict_summa = {product: qty * price for product, qty, price in sales}
    return dict(sorted(dict_summa.items(), key=lambda x: x[1], reverse=True))


sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

print(sales_ord(sales))