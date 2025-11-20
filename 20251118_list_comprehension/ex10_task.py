# Используя list comprehension, создать список
# нечётных целых чисел из диапазона от 5 до 20
# включительно. Потом вывести этот список в консоль.

odd_numbers = [number for number in range(5, 20 + 1) if number % 2 == 1]
print(odd_numbers)
