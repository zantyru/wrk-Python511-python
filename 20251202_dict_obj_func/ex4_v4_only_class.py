# Теперь всё делает класс (ну, почти всё), но есть проблема
# со списком (и любыми другими изменяющимися контейнерами),
# он общий для всех сундуков.
# 
# В предыдущей версии с функцией такой проблемы нет.


class Chest:    
    width = 1000
    length = 900
    depth = 500
    items = ["ложка", "меч", "просроченное молоко"]  # С этим будет проблема (пока); список получается общим для всех
    is_lid_open = True
    is_lid_exists = True
    is_lock_locked = False


my_chest = Chest()
my_chest.items.append("промокашка")
print(f"{my_chest.width = }")
print(f"{my_chest.items = }")

other_chest = Chest()
other_chest.width = 200
other_chest.items.append("долото")
print(f"{other_chest.width = }")
print(f"{other_chest.items = }")


# Потом научимся классы писать правильно