# Пока так, но потом сам класс будет всё делать сам

def create_non_empty_chest():  # Создали свою функцию  

    class Chest:
        pass

    chest = Chest()
    chest.width = 1000
    chest.length = 900
    chest.depth = 500
    chest.items = ["ложка", "меч", "просроченное молоко"]
    chest.is_lid_open = True
    chest.is_lid_exists = True
    chest.is_lock_locked = False

    return chest  # Ох! return. Надо будет разобраться


my_chest = create_non_empty_chest()
print(f"{my_chest.width = }")

other_chest = create_non_empty_chest()
other_chest.width = 200
print(f"{other_chest.width = }")
