check_number = 1
items = []

def add_item(item_name, item_cost):
    global items
    items.append((item_name, item_cost))

def print_с():
    global check_number, items
    if not items:
        return

    print(f"Чек {check_number}. Всего предметов: {len(items)}")
    for item_name, item_cost in items:
        print(f"{item_name} - {item_cost}")

    total_cost = sum(item_cost for _, item_cost in items)
    print(f"Итого: {total_cost}")
    print("-----")

    check_number += 1
    items = []

add_item('Блокнот', 100)
print_с()

add_item('Ручка', 70)
print_с()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_с()

add_item('Булочка', 15)
add_item('Булочка', 15)
