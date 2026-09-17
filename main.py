import random
def create_board():
    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append('-')

        grid.append(row)
    return grid


def setup_player():

    grid = create_board()

    print('Carrier: 5 ' \
    'Battleship: 4 ' \
    'Cruiser: 3 ' \
    'Submarine: 3 ' \
    'Destroyer: 2 ')

    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine':3, 'Destroyer':2 }
    


    for k, v in ships.items():
        placement = False
        print(f'Placing a {k}. This will take {v} spaces.')
        orient = int(input(f'Place your {k}. ' \
            'Enter "1" for Horizontal or "2" for Vertical: '))
        if orient == 1:
            while placement == False:
                y_pos = int(input('Enter which COLUMN from 0-9 your ship will be placed on. It will be placed rightward from here: '))
                x_pos = int(input('Enter which ROW from 0-9 your ship will be placed on: '))
                for i in range(v):
                    if grid[x_pos][y_pos+i] == 'S' or y_pos > 9:
                        print('Invalid placement!')
                        break
                    else:
                        for i in range(v):
                            grid[x_pos][y_pos+i] = 'S'
                            placement = True

        elif orient == 2:
            while placement == False:
                x_pos = int(input('Enter which ROW from 0-9 your ship will be placed on. It will be placed downward from here: '))
                y_pos = int(input('Enter which COLUMN from 0-9 your ship will be placed on: '))
                for i in range(v):
                    if grid[x_pos+i][y_pos] == 'S' or x_pos > 9:
                        print('Invalid placement!')
                        break
                    else:
                        for i in range(v):
                            grid[x_pos+i][y_pos] = 'S'
                            placement = True

        
        else:
            print('Please enter a valid value')


        for i in range(10):
            for j in range(10):
                print(grid[i][j], end =' ')
            print()
    return grid

def setup_cpu():
    grid = create_board()

    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine':3, 'Destroyer':2 }

    for k, v in ships.items():
        placement = False
        print(f'Placing a {k}. This will take {v} spaces.')
        orient = random.randint(1, 2)

        if orient == 1:
            while placement == False:
                y_pos = random.randint(0, 10-v)
                x_pos = random.randint(0, 9)
                for i in range(v):
                    if grid[x_pos][y_pos+i] == 'S':
                        break
                else:
                    for i in range(v):
                        grid[x_pos][y_pos+i] = 'S'
                    placement = True

        elif orient == 2:
            while placement == False:
                x_pos = random.randint(0, 10-v)
                y_pos = random.randint(0, 9)

                for i in range(v):
                    if grid[x_pos+i][y_pos] == 'S':
                        break
                else:
                    for i in range(v):
                        grid[x_pos+i][y_pos] = 'S'
                    placement = True

    return grid

def attack_grid(battle_grid, cpu_grid):
    turn = True
    while turn:
        for i in range(10):
            for j in range(10):
                print(battle_grid[i][j], end =' ')
            print()
        x_pos = int(input('Enter x coordinate from 0-9'))
        y_pos = int(input('Enter y coordinate from 0-9'))

        try:
            if cpu_grid[x_pos][y_pos] == 'S' and battle_grid[x_pos][y_pos] != 'X' and battle_grid[x_pos][y_pos] != 'O':
                print('Hit!')
                battle_grid[x_pos][y_pos] = 'X'
                turn = False
            elif battle_grid[x_pos][y_pos] != 'X' and battle_grid[x_pos][y_pos] != 'O':
                print('Miss!')
                battle_grid[x_pos][y_pos] = 'O'
                turn = False
            else:
                print('Not even on the board ay chap?')
        except:
            print('Please land it on the board at least')
    return battle_grid

def check_win(battle_grid):
    count = 0
    for row in battle_grid:
        for item in row:
            if item == 'X':
                count += 1

    if count == 17:
        return True
    else:
        return False

    

def main():
    cpu_grid = setup_cpu()
    battle_grid = create_board()
    game_running = True
    while game_running:
        attack_grid(battle_grid, cpu_grid)
        win = check_win(battle_grid)
        if win == True:
            print('Win!')
            break
        

main()