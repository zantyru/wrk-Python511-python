# Компьютер запрашивает у пользователя
# 7 цветов радуги. Помещает их в список
# и выводит эти цвета из списка построчно
# (то есть одно название цвета на одной
# строке) [На 10 баллов]
# 
# [+1 балл] Перед названием цвета стоит его
# индекс, под которым он числится в списке
# 
# [+1 балл] Далее вывести список этих же
# названий цветов в обратном порядке, так
# же построчно.

INITIAL_COLOR_COUNT = 7

rainbow_colors = []

for i in range(INITIAL_COLOR_COUNT):
    color_name = input("Запрос #%i. Введите один из цветов радуги: " % (i + 1))
    rainbow_colors.append(color_name)

print("\nИтак, вы ввели следующие цвета:")
color_index = 0

for color_name in rainbow_colors:
    print(color_index, color_name)
    color_index += 1

print("\nВ обратном порядке:")

for color_index in range(len(rainbow_colors) - 1, -1, -1):
    color_name = rainbow_colors[color_index]
    print(color_index, color_name)