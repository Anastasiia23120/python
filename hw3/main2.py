word = str(input("Введіть слово: "))

if any(ch.isdigit() for ch in word):
    print("Твердження невірне – у слові є цифри.")
else:
    print("Твердження вірне – у слові немає цифр.")