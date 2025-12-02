INVALID_INPUT = 'invalid_input'
OUT_OF_BOUNDS = 'out_of_bounds'
HIT_OBSTACLE = 'hit_obstacle'
ERROR_FLAG = 'flag'
ERROR_MESSAGE = 'message'

# ## Проименованные символы, что есть что на карте
CELL_EMPTY_FLOOR = "."
CELL_VOID = " "
CELL_WALL = "#"
CELL_PLAYER = "@"

# ## "Тело" лабиринта, карта местности
x = CELL_VOID # Эти переменные-всевдонимы для удобства рисования карты
W = CELL_WALL
_ = CELL_EMPTY_FLOOR
maze_cells = [
    [_,_,_,_,_,_,_,x,x,_,_,_,],
    [_,W,W,_,W,W,_,_,_,_,_,_,],
    [_,W,_,_,_,W,_,_,_,_,_,x,],
    [_,W,_,_,_,W,_,_,_,_,x,x,],
    [_,W,W,W,W,W,_,_,x,_,_,x,],
    [_,_,_,_,_,_,_,x,x,_,_,_,],
    [_,_,_,_,x,x,x,x,x,x,_,_,],
]
del _ # Эти переменные-всевдонимы больше не нужны, удаляем
del W
del x
maze_height = len(maze_cells)
maze_width = len(maze_cells[0])

# ## Переменные, описывающие игрока (игрового персонажа)
player_y = 2  # Положение по высоте
player_x = 3  # Положение по ширине
player_dy = 0  # Намерения о смещении по вертикали
player_dx = 0  # Намерения о смещении по горизонтали

# ## Технические переменные
is_game_play = True
steps_count = 0  # Счетчик шагов
last_error_message = ""

# ## Словари для хранения сообщений и флагов ошибок (требование [+coin])
errors = {
    INVALID_INPUT : {
        ERROR_FLAG: False,
        ERROR_MESSAGE: '[!] Введены не те символы',
    },
    OUT_OF_BOUNDS : {
        ERROR_FLAG: False,
        ERROR_MESSAGE: '[!] Нельзя выйти за пределы карты', 
    },
    HIT_OBSTACLE : {
        ERROR_FLAG: False,
        ERROR_MESSAGE: '[!] Нельзя пройти сквозь препятствие',
    },
}

# ## Основной цикл приложения
while is_game_play:
    # Сброс флагов ошибок в начале каждой итерации
    for error_type in errors.values():
        error_type[ERROR_FLAG] = False
    
    #-- Отрисовка --#
    # "Очистка" экрана
    print("\n" * 100)

    # Отрисовка лабиринта
    for y, cells_line in enumerate(maze_cells):
        for x, cell in enumerate(cells_line):
            if x == player_x and y == player_y:
                print(CELL_PLAYER, end=" ")
            else:
                print(cell, end=" ")
        print()
    
    # Вывод счетчика шагов
    print(f"\nСделано шагов: {steps_count}")
    
    # Вывод сообщений об ошибках из ПРЕДЫДУЩЕЙ итерации
    # (используем переменную для хранения сообщения с прошлого хода)
    if last_error_message:
        print(f"\n{last_error_message}")
        last_error_message = ""  # Сбрасываем сообщение после вывода
    
    # Отрисовка текста меню и пояснений
    print("\n")
    print(
        "a - шаг влево   w - шаг вверх\n"
        "d - шаг вправо  s - шаг вниз\n"
        "   0 - выход из программы\n"
        "\n"
        ">>> ",
        end=""
    )

    #-- Ввод --#
    player_action = input().strip()  # strip для удаления внешних пробельных символов

    #-- Основная логика --#
    # Очистка намерения двигаться, оставшегося с прошлой итерации
    player_dx = 0
    player_dy = 0

    # Разбор пользовательского ввода
    if player_action == "0":
        is_game_play = False
        continue
    elif player_action == "a":
        player_dx = -1
    elif player_action == "d":
        player_dx = 1
    elif player_action == "w":
        player_dy = -1
    elif player_action == "s":
        player_dy = 1
    else:
        errors[INVALID_INPUT][ERROR_FLAG] = True
        last_error_message = errors[INVALID_INPUT][ERROR_MESSAGE]

    # Обработка намерения двигаться
    if not errors[INVALID_INPUT][ERROR_FLAG] and player_action != "0":
        # Желаемое новое положение игрока
        player_new_x = player_x + player_dx
        player_new_y = player_y + player_dy

        # Проверки на невозможность движения
        is_player_x_correct = 0 <= player_new_x < maze_width
        is_player_y_correct = 0 <= player_new_y < maze_height
        is_player_inside_maze = is_player_x_correct and is_player_y_correct

        # Проверка выхода за пределы
        if not is_player_inside_maze:
            errors[OUT_OF_BOUNDS][ERROR_FLAG] = True
            last_error_message = errors[OUT_OF_BOUNDS][ERROR_MESSAGE]
        # Проверка преград на пути
        elif maze_cells[player_new_y][player_new_x] != CELL_EMPTY_FLOOR:
            errors[HIT_OBSTACLE][ERROR_FLAG] = True
            last_error_message = errors[HIT_OBSTACLE][ERROR_MESSAGE]
        else:
            # Осуществление перемещения
            player_x = player_new_x
            player_y = player_new_y
            # Увеличиваем счетчик шагов только при успешном перемещении
            steps_count += 1