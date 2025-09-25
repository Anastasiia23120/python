n = int(input("Введіть кількість елементів масиву: "))
arr = [int(input(f"arr[{i}] = ")) for i in range(n)]

print("Масив:", arr)

suma = sum(x for x in arr if x > 0 and x % 2 == 0)
print("Сума додатніх парних елементів =", suma)