a = int(input("Введіть a: "))
while (a<1 or a>100 ):
    a = int(input("Введіть a: "))

b = int(input("Введіть b: "))
while (b<1 or b>100):
    b = int(input("Введіть b: "))

if a>b:
    x = 2*a+b
elif a==b:
    x=-2
else:
    x=(a-5)/b

print ("Результат обчислення виразу:", x)
