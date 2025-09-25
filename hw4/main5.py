def analyze_digits():
    digits = list(map(int, input("Введіть набір цифр через пробіл: ").split()))
    print("Введені цифри:", digits)

    even = {x for x in digits if x % 2 == 0}
    odd = {x for x in digits if x % 2 != 0}

    print("Парні цифри:", even)
    print("Непарні цифри:", odd)

    if len(even) > len(odd):
        print("Більше парних цифр")
    elif len(odd) > len(even):
        print("Більше непарних цифр")
    else:
        print("Парних і непарних цифр однаково")

analyze_digits()