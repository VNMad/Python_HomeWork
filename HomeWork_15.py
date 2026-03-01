#____________________________________________________________________
#1. Одно слово
#____________________________________________________________________
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

for i in range(len(text_list)-1, -1, -1):
    if ' ' in text_list[i]:
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()

print("Обработанный список:", text_list)
#____________________________________________________________________
#2. Обновление цен товаров
#____________________________________________________________________
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = int(input("Введите скидку (в процентах): "))

for i, product in enumerate(products):
    products[i].append(round(product[1] * (1-discount/100), 2))

print(f'{'Товар':10} {'Старая цена':12} {'Новая цена':12}')
for product in products:
    print(f"{product[0]:<10} {product[1]:>10.2f}$ {product[2]:>10.2f}$")
