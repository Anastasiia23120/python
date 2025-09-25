def sum_list():
    A = list(map(int, input("Введіть список чисел через пробіл: ").split()))
    print("Список:", A)

    total = sum(A)
    print("Сума елементів списку =", total)

    return total

sum_list()