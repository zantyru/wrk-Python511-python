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

for color_index, color_name in enumerate(rainbow_colors):
    print(color_index, color_name)

print("\nВ обратном порядке:")

for color_index, color_name in reversed(enumerate(rainbow_colors)):
    print(color_index, color_name)