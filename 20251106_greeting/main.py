is_program_work = True
temperature_celsius = 20

while is_program_work:
    # Секция кода: отрисовка данных и приглашения к вводу
    print("[ПУЛЬТ ТЕМПЕРАТУРЫ]")
    print("")
    print("Текущая температура: %i" % temperature_celsius)
    print("")
    print("1 - +1 градус")
    print("2 - -1 градус")
    print("0 - выход")
    print("")
    print(">>> ")

    # Секция кода: получение данных от пользователя (ввод)
    choice = input().strip()  # Метод стрип пораждает новую строку без внешних пробельных символов

    # Секция кода: обработка данных, обновление состояния
    if choice == "0":
        is_program_work = False
    elif choice == "1":
        temperature_celsius += 1
    elif choice == "2":
        temperature_celsius -= 1
