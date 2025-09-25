# Словник з даними про журнали
# Ключ – назва журналу, значення – список [ціна, тираж]
journals = {
    "FashionMag": [50.00, 8000],
    "TechToday": [60.50, 15000],
    "HealthLife": [40.75, 9000],
    "ScienceWorld": [70.00, 5000],
    "TravelTime": [55.25, 12000]
}

# Функція виведення всіх значень словника
def print_journals(journals):
    print("Список усіх журналів:")
    for name, info in journals.items():
        print(f"{name}: Ціна = {info[0]}, Тираж = {info[1]}")

# Функція додавання нового запису
def add_journal(journals):
    name = input("Введіть назву журналу: ")
    try:
        price = float(input("Введіть ціну журналу: "))
        circulation = int(input("Введіть тираж журналу: "))
        journals[name] = [price, circulation]
        print(f"Журнал '{name}' додано.")
    except ValueError:
        print("Помилка! Введено некоректні дані.")

# Функція видалення запису
def delete_journal(journals):
    name = input("Введіть назву журналу для видалення: ")
    if name in journals:
        del journals[name]
        print(f"Журнал '{name}' видалено.")
    else:
        print(f"Журнал '{name}' не знайдено у словнику.")

# Функція сортування за ключами
def print_sorted_journals(journals):
    print("Словник журналів за відсортованими назвами:")
    for name in sorted(journals.keys()):
        info = journals[name]
        print(f"{name}: Ціна = {info[0]}, Тираж = {info[1]}")

# Функція обчислення середньої ціни журналів з тиражем < 10000
def average_price_small_circulation(journals):
    small = [info[0] for info in journals.values() if info[1] < 10000]
    if small:
        avg = sum(small) / len(small)
        print(f"Середня ціна журналів з тиражем менше 10000 примірників: {avg:.2f}")
    else:
        print("Журнали з тиражем менше 10000 не знайдено.")

# Діалогове меню
while True:
    print("\nМеню:")
    print("1 - Показати всі журнали")
    print("2 - Додати новий журнал")
    print("3 - Видалити журнал")
    print("4 - Показати журнали за відсортованими ключами")
    print("5 - Середня ціна журналів з тиражем < 10000")
    print("0 - Вихід")
    
    choice = input("Введіть пункт меню: ")
    
    if choice == "1":
        print_journals(journals)
    elif choice == "2":
        add_journal(journals)
    elif choice == "3":
        delete_journal(journals)
    elif choice == "4":
        print_sorted_journals(journals)
    elif choice == "5":
        average_price_small_circulation(journals)
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний пункт меню, спробуйте ще раз.")
