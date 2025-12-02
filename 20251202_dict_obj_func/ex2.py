# Сотрудник
employee = {
    "фамилия": "Такойтов",
    "имя": "Онсам",
    "отчество": "Какойтович",
    "доступные отделы": [
        "пищеблок",
        "бухгалтерия",
        "бассейн",
    ],
    "параметры" : {
        "должник ли": False,
        "примерный семьянин ли": True,
        "оптимист": True,
    }
}

# Список сотрудников
employees = []

# Заполнение списка
employees.append(employee)

# employee_2 = employee  # Это неправильно, так будет копия ссылки

from copy import deepcopy
employee_2 = deepcopy(employee)  # Полная копия создаётся
employee_2["фамилия"] = "Касаткин"
employee_2["имя"] = "Джон"
employee_2["отчество"] = "Доевич"
employees.append(employee_2)

# Распечатка
for e in employees:
    print()
    for key, value in e.items():
        print(key, " - ", value)


# Но это не удобно! Код копирования каждый раз что ли пичсать?