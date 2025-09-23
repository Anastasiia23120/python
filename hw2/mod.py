def first_fib_greater_than(p):
    a, b = 1, 1
    while b <= p:
        a, b = b, a + b
    return b