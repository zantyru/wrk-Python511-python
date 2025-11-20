CELL_EMPTY_FLOOR = "."
CELL_VOID = " "
CELL_WALL = "#"
CELL_PLAYER = "@"

x = CELL_VOID
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
del _
del W
del x
maze_height = len(maze_cells)
maze_width = len(maze_cells[0])

player_y = 2  # Положение по высоте
player_x = 3  # Положение по ширине
player_dy = 0  # Намерения о смещении по вертикали
player_dx = 0  # Намерения о смещении по горизонтали

is_game_play = True

while is_game_play:
    ## Отрисовка ##
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
    
    ## Ввод ##
    
    ## Основная логика ##
    pass
    is_game_play = False