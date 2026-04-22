#____________________________________________________________________
#1. План по дням недели
#____________________________________________________________________
import itertools

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}
days = itertools.cycle(weekly_schedule.items())
while True:
    user_input = input("Press 'Enter' for the schedule or 'quit' for exit: ")
    if user_input.lower() == "quit":
        break
    day, tasks = next(days)
    print(f"{day}: {', '.join(tasks)}")

#____________________________________________________________________
#2. Объединение списков продуктов
#____________________________________________________________________
import itertools

def join_products(*lst):
    return (item.lower() for item in itertools.chain(*lst))


fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

products = join_products(fruits, vegetables, dairy)

for product in products:
    print(product)

#____________________________________________________________________
#3. Комбинации одежды
#____________________________________________________________________
import itertools

def generate_attr(stuff, color, size):
    return (f"{stf} - {col} - {s}" for stf, col, s in itertools.product(stuff, color, size))


clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

attributes  = generate_attr(clothes, colors, sizes)

for attribute in attributes:
    print(attribute)