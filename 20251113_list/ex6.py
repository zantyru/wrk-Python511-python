# Задвоить элементы в списке. То есть компьютер
# превращает список [4, print, "xyz", None]
#  в список [4, 4, print, print, "xyz", "xyz", None, None]

# Как вариант решения

things = ["dgfd", 0, -1.2, None]
doubled_things = []

for item in things:
    doubled_things.append(item)
    doubled_things.append(item)

print(things)
print(doubled_things)