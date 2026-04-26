#____________________________________________________________________
#1. Генератор Фибоначчи
#____________________________________________________________________
def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


limit = int(input("Введите кол-во: "))
fib_gen = fibonacci()
for _ in range(limit):
    print(next(fib_gen))
#____________________________________________________________________
#2. Генератор уникальных элементов
#____________________________________________________________________
def unique_gen(n):
    wo_repeat = set()

    for i in n:
        if i not in wo_repeat:
            wo_repeat.add(i)
            yield i


data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
print(list(unique_gen(data)))

#for num in unique_gen(data):
#    print(num)