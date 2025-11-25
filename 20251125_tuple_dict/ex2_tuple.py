# Нам знакомы списки - изменяемые коллеции
# упорядоченных данных

things = list()
things.append(3)
things.append(None)
things.append("xyz")
print(things)

numbers = [4, 5, 6]
print(numbers)


# А есть кортежи (tuple), тоже коллеции
# упорядоченных данных, но не изменяемые

things = tuple()
# У кортежа нет append, он же неизменяемый
print(things)

data = tuple([3, 4, 5, None, 7])
# У кортежа нет append, он же неизменяемый
print(data)

values = 8.9, 12, -2.1, 0
print(values)

more_values = ("x", "y", "z")  # Круглые скобки
print(more_values)

one_element_tuple = (1, )  # Запятая!!!
one_element_tuple = 1,  # Запятая!!!
print(one_element_tuple)

# Операции на чтение данных и работа
# с индексами такие же, как и в списках