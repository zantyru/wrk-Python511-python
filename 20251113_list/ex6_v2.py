# Задвоить элементы в списке. То есть компьютер
# превращает список [4, print, "xyz", None]
#  в список [4, 4, print, print, "xyz", "xyz", None, None]

# Ещё вариант решения

things = ["dgfd", 0, -1.2, None]

for index, item in enumerate(things[:]):  # взятие полной копии списка [:]
    things.insert(index * 2, item)

print(things)