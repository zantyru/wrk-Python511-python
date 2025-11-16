pet_names = []  # список имён животных (пустой)

for i in range(3):
    name = input("Введите имя питомца, вариант %i: " % (i + 1))
    pet_names.append(name)

print("Ваш список имён для питомца:", pet_names)

print("Ещё раз ваш список имён для питомца: ")

for name in pet_names:  # Перебираем элементы списка
    print(name, end=", ")

print()

# Интересный приём, но пока не используем
print("И ещё раз ваш список имён для питомца:", *pet_names)




