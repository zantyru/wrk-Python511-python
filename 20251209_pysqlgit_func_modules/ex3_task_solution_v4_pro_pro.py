# Напишите функцию, которая
# принимает два числа и
# печатает их произведение


from typing import TypeAlias


Number: TypeAlias = int | float


def print_multiplication(a: Number, b: Number) -> None:
    print(a * b)


print_multiplication(2, 3)
print_multiplication(5.5, 4)
print_multiplication(17.39, 0.023)
print_multiplication("****Хакер****", 3)  # Использование не по смыслу
