# Построить новый список из элементов
# списка numbers, где чётным значениям
# соответствует символ "*", а нечётным -
# "#"

numbers = [4, 5, 22, -2, 1, 7]

result_list = [
    "*" if number % 2 == 0 else "#"
    for number in numbers
]

# Вариант с обычной записью цикла и условия
# for number in numbers:
#     if number % 2 == 0:
#         result_list.append("*")
#     else:
#         result_list.append("#")

print(result_list)