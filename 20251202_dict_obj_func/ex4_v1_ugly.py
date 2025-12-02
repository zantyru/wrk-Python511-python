chest = type(str(), tuple(), dict())  # Что?! Какая-то алхимия. Далее так делать не будем

# С этого момента у этого chest будет
# атрибут width; его "внутренняя"
# переменная; и так далее с другими
# атрибутами
chest.width = 1000
chest.length = 900
chest.depth = 500
chest.items = ["ложка", "меч", "просроченное молоко"]
chest.is_lid_open = True
chest.is_lid_exists = True
chest.is_lock_locked = False

print(f"{chest.width = }")