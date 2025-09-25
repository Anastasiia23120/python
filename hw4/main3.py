def delete_odd_indexes():
    A = list(map(int, input("Введіть список чисел через пробіл: ").split()))
    print("Початковий список:", A)

    result = [A[i] for i in range(len(A)) if i % 2 == 0]
    print("Результат (без непарних індексів):", result)

    return result

delete_odd_indexes()