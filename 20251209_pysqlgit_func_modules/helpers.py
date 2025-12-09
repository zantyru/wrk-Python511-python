print(f"{__name__ = }")


def print_title(header_text):
    print(f"-=[ {header_text} ]=-")
    print("Автор: Имя Отчество Фамилия")
    print()


if __name__ == "__main__":
    print_title("Электронный кошелёк")
    print_title  # Это не запуск функции
    print_title("Чат-бот \"ПушКинг\"")
