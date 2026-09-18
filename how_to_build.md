# Building a Text-Based Battleship Game in Python

## Introduction

In this project, we will build a text-based version of the game **Battleship** using Python.

The program will allow a player to:

* create a 10 × 10 game board
* place five ships on the board
* play against a computer opponent
* attack the computer's ships
* receive feedback about hits and misses
* have the computer attack the player's ships
* determine when all 17 ship spaces have been hit

The program is divided into several functions. Each function is responsible for a particular part of the game.

The main functions are:

```text
create_board()
setup_player()
setup_cpu()
player_turn()
check_win()
cpu_turn()
check_lose()
main()
```

This is an example of **modular programming**. Instead of putting the entire game into one enormous block of code, the program is separated into smaller functions.

---

# 1. Understanding the Game Board

Before creating the game, we need somewhere to store the ships and attacks.

A Battleship board is a **10 × 10 matrix**.

A matrix is a list containing other lists.

For example, a small 3 × 3 matrix could look like this:

```text
- - -
- - -
- - -
```

In Python, this could be represented as:

```python
[
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
```

Each inner list represents one **row**.

Each item inside a row represents a **column**.

Therefore:

```python
matrix[2][4]
```

means:

```text
row 2, column 4
```

Python starts counting from **0**, so a 10 × 10 board has positions from:

```text
0 to 9
```

---

# 2. Creating the Board

The first function we need is `create_board()`.

Its job is to create an empty 10 × 10 board.

```python
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
```

## Step 1 — Create an empty list

```python
grid = []
```

At this point, there are no rows in our board.

We will gradually add rows to this list.

---

## Step 2 — Create the rows

```python
for i in range(10):
```

This loop repeats 10 times.

Each repetition creates one row.

Therefore, after the loop has completed, the board will contain:

```text
10 rows
```

---

## Step 3 — Create an empty row

```python
row = []
```

Each time the outer loop runs, a new empty row is created.

We then need to put 10 positions into this row.

---

## Step 4 — Create the columns

```python
for j in range(10):
```

This is a second loop inside the first loop.

It repeats 10 times for every row.

The first loop controls the **rows**.

The second loop controls the **columns**.

This creates:

```text
10 rows × 10 columns
```

---

## Step 5 — Add an empty space

```python
row.append('-')
```

A `-` represents an empty position on the board.

For example, after one row has been completed:

```text
- - - - - - - - - -
```

---

## Step 6 — Add the row to the grid

```python
grid.append(row)
```

Once all 10 columns have been created, the completed row is added to the grid.

After all 10 rows have been created, the result is a 10 × 10 matrix.

---

## Step 7 — Return the board

```python
return grid
```

The function sends the completed board back to whatever part of the program called it.

This is important because other functions need to use the board.

For example:

```python
grid = create_board()
```

means:

> Create a board and store the returned board in `grid`.

---

# 3. Setting Up the Player

The next function is responsible for allowing the player to place their ships.

```python
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
    
```

The first thing the function does is create an empty board:

```python
grid = create_board()
```

Notice that we don't need to recreate the board code.

Instead, we **call the function** we already created.

This is one of the advantages of functions.

---

# 4. Using a Dictionary for the Ships

The ships are stored in a dictionary:

```python
ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine':3, 'Destroyer':2 }
```

A dictionary stores **key-value pairs**.

Here:

```text
Carrier     → 5
Battleship  → 4
Cruiser     → 3
Submarine   → 3
Destroyer   → 2
```

The ship name is the **key**.

The number of spaces occupied by the ship is the **value**.

This is useful because the program can work through all five ships using one loop.

---

# 5. Looping Through the Ships

```python
for k, v in ships.items():
```

`.items()` allows us to access both the key and value.

Therefore:

```text
k = ship name
v = ship length
```

For example, during one iteration:

```text
k = "Carrier"
v = 5
```

During another:

```text
k = "Destroyer"
v = 2
```

---

# 6. Tracking Whether a Ship Has Been Placed

```python
placement = False
```

The variable `placement` records whether the current ship has successfully been placed.

Initially:

```text
placement = False
```

because the ship hasn't been placed yet.

The program uses:

```python
while placement == False:
```

to keep asking the player for a position until the placement succeeds.

---

# 7. Asking for the Orientation

The program tells the player which ship they are placing:

```python
print(f'Placing a {k}. This will take {v} spaces.')
```

The `f` before the string allows variables to be inserted into the text.

For example:

```text
Placing a Carrier. This will take 5 spaces.
```

The program then asks whether the ship should be horizontal or vertical:

```python
orient = int(input(f'Place your {k}. ' \
    'Enter "1" for Horizontal or "2" for Vertical: '))
```

The input is converted to an integer using:

```python
int()
```

Therefore:

```text
1 = horizontal
2 = vertical
```

---

# 8. Horizontal Ship Placement

The program checks whether the player selected horizontal placement:

```python
if orient == 1:
```

If so, it repeatedly asks the player for coordinates:

```python
while placement == False:
```

The player enters the column:

```python
y_pos = int(input('Enter which COLUMN from 0-9 your ship will be placed on. It will be placed rightward from here: '))
```

and the row:

```python
x_pos = int(input('Enter which ROW from 0-9 your ship will be placed on: '))
```

The two variables represent the position where the ship begins.

---

# 9. Checking Horizontal Positions

The program then examines each position that the ship would occupy:

```python
for i in range(v):
```

Remember that `v` is the length of the current ship.

For example, for a Cruiser:

```text
v = 3
```

Therefore:

```python
range(v)
```

produces three iterations.

The program checks:

```python
if grid[x_pos][y_pos+i] == 'S' or y_pos > 9:
```

The expression:

```python
grid[x_pos][y_pos+i]
```

accesses a particular position on the board.

The `x_pos` remains the same because the ship is horizontal.

The `y_pos` increases because the ship extends across columns.

For example, if:

```text
x_pos = 4
y_pos = 2
v = 3
```

the positions being examined are:

```text
grid[4][2]
grid[4][3]
grid[4][4]
```

---

# 10. Placing the Horizontal Ship

If the position is available, the program enters the `else` section:

```python
else:
    for i in range(v):
        grid[x_pos][y_pos+i] = 'S'
        placement = True
```

The program places an `S` into each position occupied by the ship.

The `S` represents a **ship**.

For example:

```text
- - S S S - - - - -
```

The value of `placement` is then changed:

```python
placement = True
```

This tells the `while` loop that the ship has been placed.

---

# 11. Vertical Ship Placement

The next section handles vertical ships:

```python
elif orient == 2:
```

The process is similar, but the coordinates change differently.

The player enters the row first:

```python
x_pos = int(input('Enter which ROW from 0-9 your ship will be placed on. It will be placed downward from here: '))
```

Then the column:

```python
y_pos = int(input('Enter which COLUMN from 0-9 your ship will be placed on: '))
```

The program checks:

```python
for i in range(v):
```

and accesses:

```python
grid[x_pos+i][y_pos]
```

This time, the column stays the same while the row increases.

For example:

```text
grid[2][5]
grid[3][5]
grid[4][5]
```

This creates a vertical ship.

---

# 12. Displaying the Player's Board

After each ship is placed, the board is displayed:

```python
for i in range(10):
    for j in range(10):
        print(grid[i][j], end =' ')
    print()
```

The outer loop moves through the rows.

The inner loop moves through the columns.

The expression:

```python
grid[i][j]
```

gets the current position.

The argument:

```python
end=' '
```

means that the next value is printed on the same line.

The final:

```python
print()
```

moves to the next line.

---

# 13. Returning the Player's Board

At the end of the function:

```python
return grid
```

The completed player board is returned.

This allows another part of the program to store it:

```python
player_grid = setup_player()
```

The `player_grid` variable now contains the player's board.

---

# 14. Setting Up the CPU

The CPU needs its own board.

This is the purpose of:

```python
def setup_cpu():
```

The CPU uses the same five ships:

```python
ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine':3, 'Destroyer':2 }
```

However, instead of asking the player where to put each ship, the computer uses random numbers.

---

# 15. Randomising the CPU's Orientation

The CPU chooses horizontal or vertical using:

```python
orient = random.randint(1, 2)
```

The `random` module was imported at the beginning:

```python
import random
```

`random.randint(1, 2)` randomly produces either:

```text
1
```

or:

```text
2
```

Therefore, the CPU randomly chooses its orientation.

---

# 16. Randomising the CPU's Position

For a horizontal ship:

```python
y_pos = random.randint(0, 10-v)
x_pos = random.randint(0, 9)
```

The computer randomly chooses a starting position.

The same concept is used for vertical ships:

```python
x_pos = random.randint(0, 10-v)
y_pos = random.randint(0, 9)
```

The ship length is considered when choosing the starting position.

This helps keep the randomly generated ship within the board.

---

# 17. Checking for Overlapping CPU Ships

Before placing a CPU ship, the program checks each position:

```python
for i in range(v):
    if grid[x_pos][y_pos+i] == 'S':
        break
```

If an existing ship is found, the placement is stopped.

If no existing ship is found, the `else` belonging to the `for` loop is executed:

```python
else:
    for i in range(v):
        grid[x_pos][y_pos+i] = 'S'
    placement = True
```

This places the ship.

The same process occurs for vertical ships.

The CPU therefore continues generating random positions until it successfully places each ship.

---

# 18. Player Attacks

Once both boards have been created, the player needs to attack the CPU.

This is the purpose of:

```python
def player_turn(battle_grid, cpu_grid):
```

Notice that the function receives two pieces of information:

```text
battle_grid
cpu_grid
```

The `cpu_grid` contains the CPU's actual ships.

The `battle_grid` is the board the player sees while attacking.

---

# 19. Continuing Until a Valid Turn

The function begins with:

```python
turn = True
```

and:

```python
while turn:
```

The program continues asking for a shot until the player makes a valid attack.

---

# 20. Displaying the Battle Grid

The program displays the player's attack board:

```python
for i in range(10):
    for j in range(10):
        print(battle_grid[i][j], end =' ')
    print()
```

Initially, this board contains `-` symbols.

After attacks, it can contain:

```text
X
```

for a hit and:

```text
O
```

for a miss.

---

# 21. Getting the Player's Attack

The player enters:

```python
x_pos = int(input('Enter x coordinate from 0-9'))
y_pos = int(input('Enter y coordinate from 0-9'))
```

These values identify the position being attacked.

The program then uses:

```python
cpu_grid[x_pos][y_pos]
```

to determine what is actually located at that position on the CPU's board.

---

# 22. Detecting a Hit

The program checks:

```python
if cpu_grid[x_pos][y_pos] == 'S' and battle_grid[x_pos][y_pos] != 'X' and battle_grid[x_pos][y_pos] != 'O':
```

There are three conditions.

First:

```python
cpu_grid[x_pos][y_pos] == 'S'
```

checks whether there is a ship at that location.

Second:

```python
battle_grid[x_pos][y_pos] != 'X'
```

checks that the position hasn't already been recorded as a hit.

Third:

```python
battle_grid[x_pos][y_pos] != 'O'
```

checks that the position hasn't already been recorded as a miss.

If all conditions are true:

```python
print('Hit!')
battle_grid[x_pos][y_pos] = 'X'
turn = False
```

The attack is recorded as an `X`.

---

# 23. Detecting a Miss

If the location isn't an existing ship and hasn't already been attacked:

```python
elif battle_grid[x_pos][y_pos] != 'X' and battle_grid[x_pos][y_pos] != 'O':
```

the program records a miss:

```python
print('Miss!')
battle_grid[x_pos][y_pos] = 'O'
turn = False
```

An `O` therefore represents a missed attack.

---

# 24. Handling Invalid Input

The attack is surrounded by:

```python
try:
```

and:

```python
except:
```

This allows the program to deal with an invalid coordinate that causes an error.

If an error occurs, the program displays:

```python
print('Please land it on the board at least')
```

The program then returns to the loop and allows another attempt.

---

# 25. Checking Whether the Player Has Won

The `check_win()` function determines whether all of the CPU's ships have been hit.

```python
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
```

The program starts a counter:

```python
count = 0
```

It then examines every row:

```python
for row in battle_grid:
```

and every item in each row:

```python
for item in row:
```

Whenever it finds an `X`:

```python
if item == 'X':
    count += 1
```

the counter increases.

The five ships occupy:

```text
5 + 4 + 3 + 3 + 2 = 17
```

spaces.

Therefore, 17 hits means all ship spaces have been hit.

The function returns:

```python
True
```

if the count reaches 17.

Otherwise it returns:

```python
False
```

---

# 26. The CPU's Turn

The CPU uses:

```python
def cpu_turn(battle_grid):
```

This function is similar to the player's turn.

The major difference is that the CPU does not ask the player for coordinates.

Instead, it generates them randomly:

```python
x_pos = random.randint(0, 9)
y_pos = random.randint(0, 9)
```

This means the computer randomly chooses a row and column.

---

# 27. CPU Hits and Misses

The CPU checks the board in the same way:

```python
if battle_grid[x_pos][y_pos] == 'S' and battle_grid[x_pos][y_pos] != 'X' and battle_grid[x_pos][y_pos] != 'O':
```

If a ship is found, it prints:

```python
print('Hit!')
```

and records:

```python
battle_grid[x_pos][y_pos] = 'X'
```

If there is no ship, it records:

```python
battle_grid[x_pos][y_pos] = 'O'
```

The CPU continues selecting random coordinates until it makes a valid attack.

---

# 28. Checking Whether the Player Has Lost

The `check_lose()` function works in the same way as `check_win()`:

```python
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
```

It counts the number of `X` values on the player's board.

When 17 ship spaces have been hit, the function returns:

```python
True
```

This means the player has lost.

---

# 29. Bringing Everything Together

The final function is `main()`.

This function controls the overall sequence of the game.

```python
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
```

The first step is to create the CPU's board:

```python
cpu_grid = setup_cpu()
```

The second step is to create the player's board:

```python
player_grid = setup_player()
```

The third board is:

```python
battle_grid = create_board()
```

This starts as an empty board and records the player's attacks against the CPU.

---

# 30. Starting the Game Loop

```python
game_running = True
```

This indicates that the game is currently running.

The program then enters:

```python
while game_running:
```

Everything inside this loop represents one cycle of the game.

The sequence is:

```text
PLAYER TURN
     ↓
CHECK WIN
     ↓
CPU TURN
     ↓
CHECK LOSE
     ↓
REPEAT
```

---

# 31. Player Turn

The player attacks first:

```python
player_turn(battle_grid, cpu_grid)
```

The function receives:

```text
battle_grid
cpu_grid
```

The player chooses a coordinate and the result is recorded on `battle_grid`.

---

# 32. Check for a Win

After the player's attack:

```python
win = check_win(battle_grid)
```

The function counts the number of `X` values.

If there are 17:

```python
win = True
```

The program then displays:

```python
print('You win!')
```

and:

```python
break
```

ends the game loop.

---

# 33. CPU Turn

If the player hasn't won, the CPU takes its turn:

```python
cpu_turn(player_grid)
```

The CPU attacks the player's board.

A hit is recorded as:

```text
X
```

and a miss as:

```text
O
```

---

# 34. Check for a Loss

After the CPU attacks:

```python
lose = check_lose(player_grid)
```

The program checks whether 17 ship spaces have been hit.

If so:

```python
lose = True
```

and:

```python
print('You lose :(')
```

is displayed.

The `break` then ends the game loop.

---

# 35. The Program Entry Point

At the very bottom is:

```python
if __name__ == "__main__":
    main()
```

This determines what happens when the Python file is run.

When the file is run directly, Python calls:

```python
main()
```

This starts the entire game.

The important point is that `main()` doesn't contain all of the game logic.

Instead, it **controls the order in which the functions are called**.

---

# 36. Complete Program Flow

The overall structure of the program can be represented as:

```text
main()
│
├── setup_cpu()
│   └── create_board()
│
├── setup_player()
│   └── create_board()
│
├── create_board()
│
└── WHILE game is running
    │
    ├── player_turn()
    │
    ├── check_win()
    │
    ├── cpu_turn()
    │
    └── check_lose()
```

The program therefore follows a clear sequence.

---

# 37. How the Boards Are Used

There are three important boards in `main()`:

```python
cpu_grid = setup_cpu()
player_grid = setup_player()
battle_grid = create_board()
```

They have different purposes.

### `cpu_grid`

Contains the CPU's ships.

For example:

```text
- - S S S - - -
```

The player does not directly see this board.

---

### `player_grid`

Contains the player's ships.

For example:

```text
S S S - - - - -
```

The CPU attacks this board.

---

### `battle_grid`

Records the player's attacks.

For example:

```text
- O - X - - - -
```

Here:

```text
X = hit
O = miss
- = not attacked yet
```

This separation allows the program to keep the CPU's ship positions separate from the player's attack information.

---

# 38. Why Functions Are Used

This project demonstrates an important programming concept: **functional decomposition**.

Instead of having one large section of code, the problem is broken into smaller tasks.

For example:

```text
create_board()
```

has one main responsibility:

> Create a board.

```text
setup_player()
```

has the responsibility of:

> Allowing the player to place their ships.

```text
setup_cpu()
```

has the responsibility of:

> Randomly placing the CPU's ships.

```text
player_turn()
```

has the responsibility of:

> Allowing the player to attack.

```text
cpu_turn()
```

has the responsibility of:

> Allowing the CPU to attack.

```text
check_win()
```

has the responsibility of:

> Checking whether the player has hit all 17 ship spaces.

```text
check_lose()
```

has the responsibility of:

> Checking whether the CPU has hit all 17 player ship spaces.

```text
main()
```

has the responsibility of:

> Controlling the overall flow of the game.

---

# 39. Important Python Concepts Used

This program brings together several Python concepts.

## Lists

Used to create the rows and boards:

```python
grid = []
row = []
```

## Nested lists

Used to represent the 10 × 10 board:

```python
grid[x_pos][y_pos]
```

## Loops

Used to repeat actions:

```python
for
```

and:

```python
while
```

## Dictionaries

Used to store ship names and lengths:

```python
ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine':3, 'Destroyer':2 }
```

## Functions

Used to divide the program into manageable sections:

```python
def create_board():
```

## Parameters

Used to send information into functions:

```python
def player_turn(battle_grid, cpu_grid):
```

## Return values

Used to send information back from functions:

```python
return grid
```

and:

```python
return True
```

or:

```python
return False
```

## Random numbers

Used to create the CPU's behaviour:

```python
random.randint()
```

## Exception handling

Used to deal with errors:

```python
try:
```

and:

```python
except:
```

---

# 40. Challenge: Trace the Data

One of the most important things to understand in this program is **how data moves between functions**.

For example:

```python
player_grid = setup_player()
```

The function:

```text
setup_player()
```

creates a board and eventually returns it:

```python
return grid
```

That returned value is then stored in:

```text
player_grid
```

The same concept occurs with:

```python
cpu_grid = setup_cpu()
```

and:

```python
battle_grid = create_board()
```

This allows the different functions to work with the same game data.

---

# 41. Challenge: Understanding the Nested Loops

Consider:

```python
for i in range(10):
    for j in range(10):
        print(grid[i][j], end =' ')
    print()
```

The outer loop runs once for every row.

For each row, the inner loop runs 10 times.

Therefore:

```text
10 × 10 = 100
```

positions are accessed.

The board contains 100 individual positions.

---

# 42. Challenge: Understanding Coordinates

Suppose:

```python
x_pos = 4
y_pos = 7
```

Then:

```python
grid[x_pos][y_pos]
```

becomes:

```python
grid[4][7]
```

This accesses one specific position on the board.

When placing a horizontal ship, the row stays the same:

```python
grid[x_pos][y_pos+i]
```

When placing a vertical ship, the column stays the same:

```python
grid[x_pos+i][y_pos]
```

This is the key difference between horizontal and vertical placement.

---

# 43. Challenge: Why Does the Win Check Count 17?

The ships have the following lengths:

```text
Carrier       5
Battleship    4
Cruiser       3
Submarine     3
Destroyer     2
```

Adding them together:

```text
5 + 4 + 3 + 3 + 2 = 17
```

Therefore, there are 17 ship positions.

Every successful hit changes one position to:

```text
X
```

Once all 17 positions contain `X`, the game is won or lost depending on whose board is being checked.

---

# 44. Final Program

The complete program brings all of these functions together:

```python
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
```

# Summary

The complete Battleship program is built by developing one problem at a time.

The development sequence is:

```text
1. Create a board
        ↓
2. Set up the player's ships
        ↓
3. Set up the CPU's ships
        ↓
4. Allow the player to attack
        ↓
5. Check whether the player has won
        ↓
6. Allow the CPU to attack
        ↓
7. Check whether the player has lost
        ↓
8. Use main() to control the entire game
```

The most important idea is that **each function has a particular responsibility**.

The `main()` function then acts as the controller, calling each function in the correct order to create the complete game.
