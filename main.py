import random


def create_board():
    """Start here - need to create matrix to house the grid. How do we do so? 
    How many lines do we need? What symbol to use to represent?"""

    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append('-')

        grid.append(row)
    return grid


def setup_player():
    """We need to setup the player - add each ship, (5, 4, 3, 3, 2). Horizontal or vertical?
    How do we stop position moving off the board?
    How to avoid several IFs - use dictionaries (ship(str): spaces(int))? """
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
    """After player - what do we need to change about CPU?
    Need to obscure certain data? How?
    How to create a sense of 'AI' player? How to randomise?"""
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

def player_turn(battle_grid, cpu_grid):
    """Next, how do we allow player to attack without changing their or CPU grid? Third grid?
    How to make sure it checks accurately for ships? What symbols? How to change? How to make sure it's a valid move?"""
    turn = True
    while turn:
        print('' \
        '___________________________________________' \
        '')
        input('Press enter to continue.')
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

    for i in range(10):
        for j in range(10):
            print(battle_grid[i][j], end =' ')
        print()
    return battle_grid

def check_win(battle_grid):
    """How to check for win? Need to check each row. How many hits is a win? Limited - 17."""
    count = 0
    for row in battle_grid:
        for item in row:
            if item == 'X':
                count += 1

    if count == 17:
        return True
    else:
        return False

def cpu_turn(battle_grid):
    """Is this the same as the player_turn? Do we need another grid - the CPU cannot really see, so likely not."""
    turn = True
    while turn:
        stored_hit = False
        print('' \
        '___________________________________________' \
        '')
        input('Press enter to continue.')
        
        x_pos = random.randint(0, 9)
        y_pos = random.randint(0, 9)

        try:
            if battle_grid[x_pos][y_pos] == 'S' and battle_grid[x_pos][y_pos] != 'X' and battle_grid[x_pos][y_pos] != 'O':
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
    for i in range(10):
        for j in range(10):
            print(battle_grid[i][j], end =' ')
        print()
    return battle_grid

def check_lose(battle_grid):
    """How to check for lose? Need to check each row. How many hits is a win? Limited - 17."""
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
    """Main line - how must it flow?"""
    cpu_grid = setup_cpu()
    player_grid = setup_player()
    battle_grid = create_board()
    game_running = True
    while game_running:
        player_turn(battle_grid, cpu_grid)
        win = check_win(battle_grid)
        if win == True:
            print('You win!')
            break
        cpu_turn(player_grid)
        lose = check_lose(player_grid)
        if lose == True:
            print('You lose :(')
            break
        
        
if __name__ == "__main__":
    main()