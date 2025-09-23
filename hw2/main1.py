import math


def expression(x):
    if x > 45:
        return -math.sqrt(x)
    else:
        return math.sin(math.radians(2 * x))  


def first_fib_greater_than(p):
    a, b = 1, 1
    while b <= p:
        a, b = b, a + b
    return b


x = float(input("Введіть число x: "))
print("Результат виразу z =", expression(x))

p = int(input("Введіть число p: "))
print("Перше число Фібоначчі більше за", p, "це", first_fib_greater_than(p))