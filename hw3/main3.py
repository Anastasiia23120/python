sentence = str(input("Введіть речення: "))

words = sentence.split()
longest_word = max(words, key=len)

if len(longest_word) > 10:
    print("Твердження вірне – найдовше слово має більше 10 символів.")
else:
    print("Твердження невірне – найдовше слово має не більше 10 символів.")

print("Найдовше слово:", longest_word, "(", len(longest_word), "символів )")