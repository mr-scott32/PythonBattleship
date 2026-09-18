# Python Battleship

## A step-by-step programming tutorial

In this project, you will build a text-based version of **Battleship** in Python.

You will not learn every Python skill first and then try to remember how to use them later. Instead, you will build the game **one function at a time**.

Whenever the next part of the game requires a new programming skill, you will:

1. Learn the new skill.
2. See it used in a different example.
3. Complete a short practice task.
4. Apply the skill to Battleship.
5. Test your work before continuing.

The aim is not to copy a completed program. The aim is to understand **why each part of the program is needed and how the parts work together.**

---

# 1. Planning the Game

Before writing code, we need to decide what the program needs to do.

A large program is easier to develop when it is divided into smaller tasks. Each task can be placed inside its own **function**.

Our Battleship program will eventually contain functions for:

```text
CreateBoard
SetupPlayer
SetupCPU
PlayerTurn
CheckWin
CPUTurn
CheckLose
Main
```

Each function should have one main responsibility.

For example:

```text
CreateBoard
    Creates an empty game board.

SetupPlayer
    Allows the player to place their ships.

SetupCPU
    Places the CPU's ships randomly.

PlayerTurn
    Allows the player to attack.

CheckWin
    Checks whether the player has won.

CPUTurn
    Allows the CPU to attack.

CheckLose
    Checks whether the player has lost.

Main
    Controls the overall game.
```

## New skill: Functions

A function is a named section of code that performs a particular task.

For example:

```python
def say_hello():
    print('Hello!')
```

The function does not run just because we have created it.

We call it:

```python
say_hello()
```

## Different example

Imagine a program that needs to display a menu.

```python
def display_menu():
    print('1. Start')
    print('2. Instructions')
    print('3. Quit')

display_menu()
```

The function has one clear job: displaying the menu.

### Practice

Create a function called `display_rules()` that prints three rules for a game.

### Battleship

Before writing `CreateBoard`, write down:

* What does the function need to do?
* What information does it need?
* What should it produce?

---

# 2. Creating a List

Our board will eventually contain many pieces of information.

Python uses **lists** to store multiple values.

Create an empty list:

```python
items = []
```

Add something to a list using `.append()`:

```python
items.append('Apple')
items.append('Banana')
items.append('Orange')
```

The list now contains:

```text
Apple
Banana
Orange
```

## Different example

A shopping program could create a list of items:

```python
shopping_list = []

shopping_list.append('Milk')
shopping_list.append('Bread')
shopping_list.append('Eggs')
```

## New skill: `for` loops

A `for` loop can repeat instructions a specific number of times.

```python
for i in range(5):
    print('Hello')
```

This prints `Hello` five times.

The variable `i` changes each time the loop repeats.

### Practice

Create an empty list and use a `for` loop to add five `-` symbols to it.

Your list should represent:

```text
- - - - -
```

### Battleship

A Battleship row needs **10 empty positions**.

Create code that produces one row containing ten `-` symbols.

Do not worry about creating the entire board yet.

### Test

Print the row.

You should have ten positions.

---

# 3. Creating a 2D List

One row is not enough for Battleship.

A Battleship board has:

```text
10 rows
10 columns
```

This means we need a **list containing lists**.

This is called a **two-dimensional list**, or **2D list**.

For example:

```python
grid = []

row = ['-', '-', '-']
grid.append(row)
```

Now `grid` contains one row.

We can create many rows using a loop:

```python
grid = []

for i in range(3):
    row = []
    
    for j in range(3):
        row.append('-')
    
    grid.append(row)
```

This produces a 3 × 3 grid.

## Why are there two loops?

The outer loop creates the rows.

The inner loop creates the positions inside each row.

Think about it as:

```text
Create row
    Create position
    Create position
    Create position

Create row
    Create position
    Create position
    Create position

Create row
    Create position
    Create position
    Create position
```

### Practice

Create a 4 × 4 grid containing `-` symbols.

Print the resulting list.

### Battleship

Now create your `create_board()` function.

It should:

* create an empty list for the board
* create 10 rows
* put 10 `-` symbols into each row
* add each row to the board
* return the completed board

You should now have your first completed Battleship function.

---

# 4. Accessing Positions in a Grid

We need to be able to find individual positions on our board.

Python uses indexes to access list positions.

For example:

```python
items = ['A', 'B', 'C']
```

The positions are:

```text
Index:    0    1    2
          A    B    C
```

So:

```python
items[0]
```

gives:

```text
A
```

A 2D list uses two indexes:

```python
grid[row][column]
```

For example:

```python
grid[2][4]
```

means:

> Row 2, column 4.

Remember that Python starts counting at **0**.

---

## Different example

Imagine a cinema seating plan:

```text
A B C
D E F
G H I
```

The value in row 1, column 2 is:

```python
seats[1][2]
```

### Practice

Create a 3 × 3 grid containing letters.

Print one specific position using two indexes.

Then change that position to `X`.

### Battleship

Use your board and access individual positions.

For example, experiment with:

```python
grid[2][5]
```

Change a position to `S`.

Print the board and confirm that the correct position changed.

---

# 5. Displaying a Grid

Our board is stored correctly, but printing the entire list is not very easy to read.

We can use nested loops to display every position.

For example:

```python
for i in range(3):
    for j in range(3):
        print(grid[i][j], end=' ')
    print()
```

The inner loop prints each position in the row.

The outer loop moves to the next row.

The `end=' '` means that the next value is printed on the same line.

The `print()` after the inner loop moves to the next line.

### Practice

Create a 5 × 5 grid and display it as a square.

### Battleship

Add code to display your Battleship board.

You should now be able to:

1. Create a board.
2. Store it in a variable.
3. Change an individual position.
4. Display the entire board.

---

# 6. Getting Coordinates from the Player

A player needs to tell the program where they want to place a ship.

We can use `input()`.

```python
name = input('Enter your name: ')
```

`input()` produces text.

If we need a number, we can convert the input using `int()`:

```python
age = int(input('Enter your age: '))
```

## Different example

A game might ask:

```python
x = int(input('Enter the X coordinate: '))
y = int(input('Enter the Y coordinate: '))
```

The player could enter:

```text
2
5
```

The variables now contain integers.

### Practice

Write a program that asks the user for:

* a row
* a column

Then print both values.

### Battleship

Add coordinate input to your ship-placement program.

You need:

```text
x_pos
y_pos
```

These will represent the starting position of a ship.

---

# 7. Repeating Across Multiple Positions

A ship is not stored in one position.

A ship with a length of 5 occupies five positions.

A `for` loop can process those positions.

For example:

```python
for i in range(5):
    print(i)
```

produces:

```text
0
1
2
3
4
```

If our starting column is `3`, we could use:

```python
y_pos + i
```

to represent:

```text
3
4
5
6
7
```

This allows a ship to extend across the board.

## Different example

Imagine a character moving five spaces to the right.

If the starting position is 2:

```python
for i in range(5):
    position = 2 + i
    print(position)
```

The positions are:

```text
2
3
4
5
6
```

### Practice

Ask the user for a starting position and a length.

Use a loop to print every position occupied by the object.

### Battleship

Use a loop to inspect the positions a ship would occupy.

For a horizontal ship, think carefully about which coordinate needs to change.

For a vertical ship, think carefully about which coordinate needs to change.

---

# 8. Making Decisions

We now need to determine whether a ship can be placed.

Python uses `if` statements to make decisions.

```python
if score >= 50:
    print('Pass')
```

We can also use `else`:

```python
if score >= 50:
    print('Pass')
else:
    print('Fail')
```

We can combine conditions using logical operators.

For example:

```python
if age >= 13 and age <= 17:
    print('Teenager')
```

We can use `or` when either condition can be true:

```python
if answer == 'Y' or answer == 'y':
    print('Yes')
```

## Different example

A game character can enter a door only if they have a key:

```python
if has_key == True:
    print('Door opens')
else:
    print('Door remains locked')
```

### Practice

Write a program that checks whether a number is between 1 and 10.

### Battleship

When placing a ship, check whether each position already contains a ship.

If it does, the placement is invalid.

If it does not, the ship can potentially be placed.

---

# 9. Stopping a Loop

Sometimes we need to stop a loop before it reaches the end.

Python provides `break`.

For example:

```python
for i in range(10):
    if i == 5:
        break
    
    print(i)
```

The loop stops when `i` reaches 5.

## Different example

Imagine searching for a particular name:

```python
for name in names:
    if name == 'Sam':
        print('Found!')
        break
```

Once the name is found, there is no reason to keep searching.

### Practice

Create a loop that checks five numbers.

If one of the numbers is negative, stop the loop.

### Battleship

When checking the positions a ship would occupy:

> If any position is already occupied, the placement should be rejected.

Use `break` to stop checking once an invalid position is found.

---

# 10. Repeating Until Something Works

Suppose a player enters an invalid ship placement.

We don't want the program to simply move on to the next ship.

We want it to ask again.

This is where a `while` loop is useful.

```python
valid = False

while valid == False:
    print('Try again')
```

The loop continues while the condition is true.

Eventually, something inside the loop must change the condition.

For example:

```python
valid = False

while valid == False:
    answer = input('Enter Y to continue: ')

    if answer == 'Y':
        valid = True
```

## Why use a Boolean?

A Boolean stores either:

```text
True
False
```

This makes it useful for controlling loops.

### Practice

Create a program that repeatedly asks the user to enter a number between 1 and 5.

Stop asking when they enter a valid number.

### Battleship

Use a Boolean variable such as:

```python
placement = False
```

Continue asking for coordinates while the placement is invalid.

Once a valid placement has been made, change the variable so the loop ends.

---

# 11. Placing Different Ships

We now have a problem.

Battleship has several ships:

```text
Carrier       5
Battleship    4
Cruiser       3
Submarine     3
Destroyer     2
```

We could write separate code for every ship, but that would create a lot of repetition.

Instead, we can store related information in a **dictionary**.

A dictionary stores values using keys.

For example:

```python
prices = {
    'Bread': 4,
    'Milk': 3,
    'Eggs': 6
}
```

The item is the key.

The number is the value.

---

## Looping through a dictionary

The `.items()` method lets us retrieve both the key and value:

```python
for item, price in prices.items():
    print(item, price)
```

This produces each item and its price.

### Different example

```python
players = {
    'Alex': 25,
    'Jordan': 31,
    'Taylor': 18
}
```

A loop can process every player and their score.

### Practice

Create a dictionary containing three games and their ages.

Use `.items()` to print each game and its age.

### Battleship

Create a dictionary containing all five ships and their lengths.

Then use `.items()` to process each ship.

Your program should now be able to use the **same placement code** for ships of different lengths.

---

# 12. Creating the Player Setup

We now have nearly all of the skills required to create the player's setup.

The function needs to:

```text
Create a board
Create a list/dictionary of ships
Process each ship
Ask whether it is horizontal or vertical
Ask for coordinates
Check whether the placement is valid
Place the ship
Repeat if necessary
Display the board
Return the board
```

## New skill: Parameters

A parameter allows information to be passed into a function.

For example:

```python
def display_score(score):
    print(score)
```

The value is supplied when the function is called:

```python
display_score(85)
```

### Different example

```python
def calculate_total(price, quantity):
    total = price * quantity
    print(total)
```

The function receives two pieces of information.

### Battleship

Your placement code needs to know the length of the current ship.

The dictionary already provides this value.

Use that value when determining how many positions the ship occupies.

Build your `setup_player()` function now.

### Test

Before continuing, test:

* a horizontal ship
* a vertical ship
* a ship of a different length
* two ships that do not overlap
* an attempted overlapping placement

---

# 13. Returning Information from a Function

Our setup function creates a board.

Another part of the program will need to use that board.

This is where `return` is important.

For example:

```python
def get_name():
    name = input('Enter your name: ')
    return name
```

We can store the returned value:

```python
player_name = get_name()
```

## Different example

```python
def calculate_area(length, width):
    area = length * width
    return area
```

Then:

```python
room_area = calculate_area(5, 4)
```

`room_area` now contains the returned value.

### Battleship

Your `setup_player()` function needs to return the completed player grid.

Think about the data flow:

```text
SetupPlayer
     ↓
PlayerGrid
```

The next part of the program can then store the returned grid.

---

# 14. Creating the CPU's Ships

The player chooses where their ships go.

The CPU should not.

Instead, the CPU should choose positions randomly.

Python's `random` module can generate random numbers.

```python
import random
```

Then:

```python
number = random.randint(1, 10)
```

generates a random integer between 1 and 10.

## Different example

A treasure could appear at a random position on a 10 × 10 map:

```python
x = random.randint(0, 9)
y = random.randint(0, 9)
```

Every time the program runs, a different position may be selected.

### Practice

Generate 10 random coordinates.

Print them.

---

# 15. Random Ships Must Still Fit

Randomly choosing a starting position is not enough.

Imagine a 5-space ship starts in column 8.

It would need:

```text
8 9 10 11 12
```

which does not fit.

We therefore need to restrict the possible starting position.

For a ship of length `v` on a 10-position row, the starting coordinate needs to account for the ship's length.

For example, a length of 5 can start at:

```text
0 1 2 3 4 5
```

but not 6, 7, 8 or 9.

### Practice

For a board of 10 positions, work out the largest possible starting position for:

```text
Length 2
Length 3
Length 4
Length 5
```

### Battleship

Use the ship length when generating the CPU's starting coordinate.

The CPU should:

1. Randomly choose horizontal or vertical.
2. Randomly choose a valid starting coordinate.
3. Check whether the positions are already occupied.
4. If they are occupied, try again.
5. Otherwise, place the ship.

---

# 16. Checking Every Position

When the CPU chooses a position, we need to check **every position occupied by the ship**.

We already know how to use:

```python
for i in range(v):
```

But there is a useful Python feature for this particular problem.

## `for...else`

Consider:

```python
for number in numbers:
    if number < 0:
        break
else:
    print('No negative numbers found')
```

The `else` belongs to the **for loop**.

It runs only if the loop finishes without using `break`.

This makes it useful for:

> Check every position. If any position is invalid, break. Otherwise, place the ship.

### Different example

A program searches a list for a missing value.

```python
for item in items:
    if item == 'Missing':
        break
else:
    print('Everything is present')
```

### Practice

Create a list of numbers.

Use `for...else` to determine whether the list contains a negative number.

### Battleship

Use `for...else` when the CPU checks whether every position required by a ship is available.

If a position contains `S`, use `break`.

If the loop finishes without `break`, the ship can be placed.

Build `setup_cpu()`.

### Test

Run the program several times.

Check that:

* all five ships appear
* ships fit on the board
* ships do not overlap
* the positions change between games

---

# 17. The Player Needs to Attack

The player now has a grid and the CPU has a hidden grid.

We need another grid to show the player what has happened during the battle.

For example:

```text
- - - - -
- - O - -
- - - X -
- - - - -
- - - - -
```

Here:

```text
X = hit
O = miss
- = not yet selected
```

The player's battle grid therefore stores the results of their attacks.

The CPU grid stores the CPU's ships.

---

# 18. Passing Multiple Grids to a Function

Our player-turn function needs two grids:

```text
BattleGrid
CPUGrid
```

A function can receive multiple parameters.

For example:

```python
def compare_scores(score1, score2):
    if score1 > score2:
        print('Score 1 wins')
    else:
        print('Score 2 wins')
```

The function receives two values.

### Battleship

Your player-turn function needs to receive:

```text
battle_grid
cpu_grid
```

Think carefully about what each grid is used for.

```text
CPUGrid
    What ships actually exist?

BattleGrid
    What attacks has the player already made?
```

Build the beginning of `player_turn()`.

---

# 19. Checking a Player's Attack

The player enters:

```text
x coordinate
y coordinate
```

The program uses those coordinates to look at the CPU grid.

If the CPU grid contains a ship:

```text
Hit
```

Otherwise:

```text
Miss
```

The program then changes the battle grid.

For example:

```text
X
```

for a hit and:

```text
O
```

for a miss.

## Combining conditions

We also need to prevent the player from attacking the same position twice.

A condition can contain several checks:

```python
if condition1 and condition2:
    ...
```

or:

```python
if condition1 or condition2:
    ...
```

### Practice

Create a small grid.

Ask the user for a coordinate.

Check whether the position contains `X`.

If it does, print that the position has already been selected.

### Battleship

Complete the logic for `player_turn()`.

It should:

1. Display the battle grid.
2. Ask for coordinates.
3. Check the CPU grid.
4. Determine hit or miss.
5. Update the battle grid.
6. Prevent the same position being selected again.
7. Finish the player's turn after a valid attack.

---

# 20. Checking for a Win

There are 17 ship positions in total:

```text
5 + 4 + 3 + 3 + 2 = 17
```

The player wins when all 17 have been hit.

We therefore need to count the number of `X` values in the battle grid.

## Counting

A counter can be used:

```python
count = 0
```

Each time the required item is found:

```python
count += 1
```

This means:

> Increase `count` by 1.

## Nested loops

Our board contains rows, and each row contains positions.

We can therefore use:

```python
for row in grid:
    for item in row:
        ...
```

The outer loop processes each row.

The inner loop processes each position within that row.

### Different example

Suppose a school has marks stored by class:

```text
Class 1 → marks
Class 2 → marks
Class 3 → marks
```

Nested loops could be used to count how many students received a particular result.

### Practice

Create a 2D list containing several `X` values.

Use nested loops to count the number of `X` values.

### Battleship

Create `check_win()`.

It should:

1. Start a counter at zero.
2. Inspect every row.
3. Inspect every position in every row.
4. Count every `X`.
5. Determine whether the total is 17.
6. Return `True` or `False`.

---

# 21. Boolean Return Values

We now need the function to tell the main program whether the player has won.

A function can return a Boolean.

For example:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

The function returns either:

```text
True
False
```

We can store the result:

```python
result = is_even(8)
```

### Battleship

Your `check_win()` function should return:

```text
True
```

when all 17 ship positions have been hit.

Otherwise it should return:

```text
False
```

This allows another function to decide what happens next.

---

# 22. Creating the CPU's Turn

The CPU now needs to attack the player's ship grid.

The basic process is similar to the player's turn:

```text
Choose coordinates
        ↓
Check the player's grid
        ↓
Hit or miss
        ↓
Change the grid
```

The major difference is that the CPU does not use `input()`.

Instead, it generates coordinates randomly.

### Battleship

Create `cpu_turn()`.

It should:

* generate a random row
* generate a random column
* check whether that position has already been attacked
* determine hit or miss
* update the player's grid
* finish the CPU turn

Use the skills you have already learned rather than creating a completely new approach.

---

# 23. Checking for a Loss

The CPU wins when all 17 of the player's ship positions have been hit.

This is essentially the same type of problem as `check_win()`.

Create:

```text
CheckLose
```

Use the player's grid and count the number of `X` values.

If the count reaches 17:

```text
True
```

Otherwise:

```text
False
```

You are deliberately reusing a skill you have already learned.

---

# 24. Handling Invalid Input

So far, we have assumed that the user enters numbers correctly.

What happens if they enter:

```text
hello
```

instead of:

```text
5
```

This can cause a Python error when using `int()`.

Python provides `try` and `except` for handling errors.

For example:

```python
try:
    number = int(input('Enter a number: '))
except:
    print('Please enter a number')
```

Python attempts the code inside `try`.

If an error occurs, the `except` code runs.

## Different example

```python
try:
    age = int(input('Enter your age: '))
    print(age)
except:
    print('That was not a valid number.')
```

### Practice

Create a program that asks for a number and handles a non-number input.

### Battleship

Use error handling where coordinate input could cause the program to fail.

Your program should respond with an appropriate message rather than crashing.

---

# 25. Bringing Everything Together

We now have the individual functions.

The final function is `main()`.

Its job is to control the game.

The main program needs to:

```text
Set up the CPU
Set up the player
Create the battle grid

Start the game

    Player takes a turn

    Check whether player has won

    CPU takes a turn

    Check whether player has lost

Repeat until somebody wins
```

This is called **program flow**.

The individual functions perform the jobs.

`main()` decides **when each job happens**.

---

# 26. Passing the Results Between Functions

Look at the information produced by the setup functions.

```text
SetupCPU
    ↓
CPUGrid

SetupPlayer
    ↓
PlayerGrid

CreateBoard
    ↓
BattleGrid
```

These values can be stored in variables.

For example:

```python
cpu_grid = setup_cpu()
```

The function creates the grid and returns it.

The returned grid is stored in:

```text
cpu_grid
```

The same principle applies to the player grid and battle grid.

This is one of the most important ideas in the project:

> **Functions can receive information through parameters and send information back using return values.**

---

# 27. The Main Game Loop

A game needs to repeat turns.

A Boolean variable can control whether the game is still running:

```python
game_running = True
```

Then:

```python
while game_running:
    ...
```

The game continues until somebody wins.

The overall flow should be:

```text
START

Set up CPU
Set up Player
Create battle grid

WHILE game is running

    Player turn

    Check win

    If player won
        announce winner
        stop game

    CPU turn

    Check lose

    If player lost
        announce loser
        stop game

END
```

Notice that the win and lose checks happen **inside the game loop**.

---

# 28. Building `main()`

Now create your `main()` function.

It should call the other functions in the correct order.

Your program should follow this structure:

```text
main
│
├── setup_cpu
│
├── setup_player
│
├── create_board
│
└── while game is running
    │
    ├── player_turn
    │
    ├── check_win
    │
    ├── cpu_turn
    │
    └── check_lose
```

Do not put all of the game logic inside `main()`.

The purpose of your functions is to keep the individual tasks separate.

---

# 29. Calling `main()`

Python programs commonly use:

```python
if __name__ == "__main__":
    main()
```

This tells Python to run `main()` when this file is run as the main program.

For this project, this should be at the bottom of your program.

---

# 30. Testing the Complete Game

Do not simply play one game and decide that the program works.

Test individual parts deliberately.

## Board testing

Check that:

* the board has 10 rows
* every row has 10 positions
* every position starts as `-`

## Player setup testing

Check that:

* each ship can be placed horizontally
* each ship can be placed vertically
* ships cannot overlap
* ships fit on the board
* all five ships are placed

## CPU setup testing

Run the program multiple times.

Check that:

* ships appear in different positions
* ships fit on the board
* ships do not overlap

## Player attack testing

Check:

* a hit
* a miss
* attacking the same position twice
* a valid coordinate
* an invalid coordinate

## Win testing

Create a test grid containing exactly 17 `X` values.

Check that:

```text
CheckWin → True
```

Then remove one `X`.

Check that:

```text
CheckWin → False
```

## Lose testing

Perform the same type of testing for `CheckLose`.

---

# 31. Debugging

When your program does not work, do not immediately rewrite it.

First identify **which function is causing the problem**.

For example:

```text
The board is wrong
    ↓
Check CreateBoard

Ships overlap
    ↓
Check SetupPlayer or SetupCPU

Player attacks the wrong position
    ↓
Check PlayerTurn

Winner is detected incorrectly
    ↓
Check CheckWin

CPU attacks incorrectly
    ↓
Check CPUTurn
```

You can also temporarily print variables.

For example:

```python
print(x_pos)
print(y_pos)
```

This lets you see what values the program is actually using.

---

# 32. Important Python Skills You Have Used

By completing the project, you have used all of these skills.

### Variables

```python
score = 0
```

### Input

```python
name = input('Enter name: ')
```

### Type conversion

```python
number = int(input('Enter number: '))
```

### Selection

```python
if condition:
```

```python
elif condition:
```

```python
else:
```

### Logical operators

```python
and
```

```python
or
```

### Comparison operators

```python
==
!=
>
<
>=
<=
```

### Boolean values

```python
True
False
```

### `for` loops

```python
for i in range(10):
```

### `while` loops

```python
while game_running:
```

### Nested loops

```python
for row in grid:
    for item in row:
```

### Lists

```python
grid = []
```

### `.append()`

```python
grid.append(row)
```

### 2D lists

```python
grid[row][column]
```

### Dictionaries

```python
ships = {
    'Carrier': 5
}
```

### Dictionary `.items()`

```python
for ship, length in ships.items():
```

### Functions

```python
def create_board():
```

### Parameters

```python
def player_turn(battle_grid, cpu_grid):
```

### Return values

```python
return grid
```

### Boolean return values

```python
return True
```

### `break`

```python
break
```

### `for...else`

```python
for ...
    ...
else:
    ...
```

### Random numbers

```python
random.randint()
```

### Error handling

```python
try:
    ...
except:
    ...
```

### Formatted strings

```python
print(f'Placing a {ship}.')
```

---

# 33. The Development Order

When building your own version, follow this order.

Do **not** try to write the entire program at once.

### Step 1

Create and test:

```text
CreateBoard
```

### Step 2

Learn how to access positions in a 2D list.

### Step 3

Build:

```text
SetupPlayer
```

Start with one ship before adding all five.

### Step 4

Add:

```text
horizontal
vertical
```

placement.

### Step 5

Add:

```text
overlap checking
```

### Step 6

Add:

```text
repeat until valid
```

### Step 7

Use the dictionary to add all five ships.

### Step 8

Build:

```text
SetupCPU
```

using random positions.

### Step 9

Build:

```text
PlayerTurn
```

### Step 10

Build:

```text
CheckWin
```

### Step 11

Build:

```text
CPUTurn
```

### Step 12

Build:

```text
CheckLose
```

### Step 13

Build:

```text
Main
```

### Step 14

Add error handling and test the complete game.

---

# 34. Final Challenge

Once the basic Battleship game works, improve it without changing the fundamental structure.

Choose improvements that require you to apply skills you already know.

Possible challenges include:

* display row and column numbers around the board
* improve the instructions shown to the player
* display a clearer hit/miss message
* keep track of the number of turns
* display the number of remaining ship positions
* allow the player to enter coordinates in a different format
* improve invalid-input messages
* add a replay option
* add a difficulty setting that changes how the CPU selects its attacks

For each improvement, first identify:

```text
What does the program need to do?

Which function should be responsible?

What new information does that function need?

What should the function return?

How will you test it?
```

---

# Final Checklist

Before calling your Battleship program complete, make sure you can explain:

* Why the board is a 2D list.
* Why two nested loops are needed to create the board.
* How `grid[row][column]` accesses a position.
* Why the player and CPU need different grids.
* Why a third battle grid is required.
* Why a dictionary is useful for storing ship names and lengths.
* Why `.items()` is used.
* Why a `while` loop is used when placing ships.
* Why a Boolean variable can control that loop.
* Why `break` is needed when an invalid position is discovered.
* How `for...else` works.
* Why the CPU uses random numbers.
* Why the CPU's random starting position depends on ship length.
* How functions pass information through parameters.
* How functions send information back using `return`.
* How nested loops count hits.
* Why there are 17 ship positions.
* How the program determines when the game has ended.
* Why `main()` is responsible for controlling the overall game.

Most importantly, you should be able to look at a new programming problem and ask:

> **What is the next problem I need to solve, and which programming skill can I use to solve it?**

That is the main skill this project is designed to develop.