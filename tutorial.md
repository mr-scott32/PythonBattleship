# Python Programming Tutorial

## Building a Text-Based Battleship Game

### What you will learn

In this project, you will use a range of Python programming skills to build a text-based Battleship game.

You will learn how to:

* create and call functions
* use parameters
* return values from functions
* create and manipulate lists
* create 2D lists (matrices)
* use nested `for` loops
* use `while` loops
* use Boolean variables
* use `if`, `elif` and `else`
* use dictionaries
* use `.items()`
* use `range()`
* use user input
* convert input using `int()`
* use formatted strings
* use random numbers
* use `try` and `except`
* use `break`
* use `for...else`
* access individual elements of a matrix
* pass the same data between functions
* break a large problem into smaller functions
* create a main program that controls the flow of a program

You will **not** be given the Battleship code for each function. Instead, each section teaches you the skill using a different example before you apply it to Battleship.

---

# Part 1 — Functions

## Why use functions?

Imagine you are making a program for a school café.

You might need to:

1. display the menu
2. calculate a bill
3. check whether a customer has enough money
4. print a receipt

Instead of putting everything into one enormous program, each task can be placed inside its own function.

For example:

```python
def say_hello():
    print("Welcome to the café!")
```

The function does not run just because we have defined it.

We need to call it:

```python
say_hello()
```

### Try it

Create a function called `show_menu()` that displays:

```text
1. Sandwich
2. Pizza
3. Pasta
```

Then call the function.

---

# Part 2 — Functions with Parameters

Sometimes a function needs information from the program.

For example, a program might need to display a student's name.

```python
def greet_student(name):
    print(f"Welcome {name}!")
```

We can then call:

```python
greet_student("Alex")
```

The value `"Alex"` is passed into the parameter `name`.

The output is:

```text
Welcome Alex!
```

### Parameters

A parameter is information that a function receives.

```python
def greet_student(name):
```

Here:

```text
name = parameter
```

When we call:

```python
greet_student("Alex")
```

the value `"Alex"` is passed into `name`.

### Try it

Create:

```python
def show_score(score):
```

The function should display:

```text
Your score is 25
```

when called with:

```python
show_score(25)
```

---

# Part 3 — Returning Values

A function can also send information back to the part of the program that called it.

For example:

```python
def calculate_area(length, width):
    area = length * width
    return area
```

We can store the returned value:

```python
room_area = calculate_area(5, 4)
```

Now:

```text
room_area = 20
```

### `print()` vs `return`

These are different.

```python
print(area)
```

displays something to the user.

```python
return area
```

sends something back to the program.

### Try it

Create:

```python
def calculate_total(price, quantity):
```

Return the total cost.

For example:

```python
total = calculate_total(5, 3)
```

should result in:

```text
total = 15
```

---

# Part 4 — Boolean Values

A Boolean variable can have one of two values:

```python
True
False
```

For example:

```python
logged_in = False
```

Later:

```python
logged_in = True
```

Boolean variables are particularly useful when a program needs to keep track of whether something has happened.

For example:

```python
finished = False

while finished == False:
    # do something
```

When the task is completed:

```python
finished = True
```

The loop can then stop.

### Try it

Create a variable:

```python
door_open = False
```

Write an `if` statement that prints:

```text
The door is open
```

when `door_open` is `True`.

---

# Part 5 — `while` Loops

A `while` loop repeats while a condition is true.

For example:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

This produces:

```text
0
1
2
3
4
```

The important part is that something eventually changes the condition.

---

## Using a Boolean with a `while` loop

Consider a password system:

```python
correct = False

while correct == False:
    password = input("Enter password: ")

    if password == "hello":
        correct = True
```

The loop continues until the correct password is entered.

This technique is useful when a program needs to keep asking for something until valid information is entered.

### Try it

Create a program that repeatedly asks:

```text
Enter a number:
```

until the user enters `10`.

Use a Boolean variable to control the loop.

---

# Part 6 — Lists

A list stores multiple values.

For example:

```python
scores = [12, 18, 15, 20]
```

Individual items can be accessed using their position.

```python
scores[0]
```

gives:

```text
12
```

and:

```python
scores[2]
```

gives:

```text
15
```

Remember that Python starts counting at **0**.

---

# Part 7 — Adding to a List

An empty list can be created:

```python
items = []
```

We can add something using `.append()`:

```python
items.append("Pizza")
```

Now:

```text
["Pizza"]
```

We can add another:

```python
items.append("Pasta")
```

Now:

```text
["Pizza", "Pasta"]
```

### Try it

Create an empty list called `players`.

Ask the user for three player names and append each name to the list.

---

# Part 8 — `for` Loops

A `for` loop is useful when we know how many times something needs to happen.

```python
for i in range(5):
    print(i)
```

This produces:

```text
0
1
2
3
4
```

The value of `i` changes each time the loop runs.

---

# Part 9 — Nested Loops

A loop can be placed inside another loop.

For example, imagine a 3 × 3 seating plan.

```python
for row in range(3):
    for column in range(3):
        print("Seat", row, column)
```

The outer loop controls the rows.

The inner loop controls the columns.

This is called a **nested loop**.

The pattern is:

```text
FOR each row
    FOR each column
        do something
```

This concept is extremely important for the Battleship board.

---

# Part 10 — Two-Dimensional Lists

A two-dimensional list is a list containing other lists.

For example:

```python
seats = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
```

This represents:

```text
- - -
- - -
- - -
```

We can access a particular position using two indexes:

```python
seats[1][2]
```

The first number identifies the row.

The second identifies the column.

Therefore:

```text
seats[row][column]
```

---

# Part 11 — Building a Matrix

Suppose a program needs a 4 × 4 map.

Start with:

```python
map_grid = []
```

Create a row:

```python
row = []
```

Add four positions:

```python
for column in range(4):
    row.append("-")
```

Then add the row to the matrix:

```python
map_grid.append(row)
```

To create all four rows, another loop is required around this process.

### Your task

Create a function called:

```python
create_map()
```

that returns a 4 × 4 matrix containing `-`.

Do not copy the Battleship board code. Work out the structure yourself.

---

# Part 12 — Accessing a Matrix

Once you have a matrix, you can change an individual position.

For example:

```python
map_grid[2][1] = "X"
```

This changes one position.

You can think of it as:

```text
        column
          ↓
      0 1 2 3
    0 - - - -
row 1 - - - -
    2 - X - -
    3 - - - -
```

### Try it

Create a 5 × 5 matrix.

Ask the user for:

```text
row
column
```

Then place an `X` at that position.

---

# Part 13 — Displaying a Matrix

A matrix can be displayed using nested loops:

```python
for row in range(5):
    for column in range(5):
        print(grid[row][column], end=" ")
    print()
```

The inner loop prints all the columns.

The outer loop then moves to the next row.

The `end=" "` keeps the values on the same line.

The final `print()` moves down to the next line.

### Your task

Modify your 5 × 5 matrix program so that it displays the matrix after placing the `X`.

---

# Part 14 — Dictionaries

A dictionary stores information as key-value pairs.

For example:

```python
prices = {
    "Pizza": 12,
    "Burger": 10,
    "Pasta": 15
}
```

The keys are:

```text
Pizza
Burger
Pasta
```

The values are:

```text
12
10
15
```

We can access a value using its key:

```python
prices["Pizza"]
```

which gives:

```text
12
```

---

# Part 15 — Looping Through a Dictionary

The `.items()` method allows us to access both the key and value:

```python
for item, price in prices.items():
    print(item, price)
```

This produces:

```text
Pizza 12
Burger 10
Pasta 15
```

The important pattern is:

```python
for key, value in dictionary.items():
```

This becomes useful when several objects have the same type of information.

### Your task

Create a dictionary containing five school subjects and their test marks.

Use `.items()` to display each subject and mark.

---

# Part 16 — User Input

The `input()` function allows the user to enter information.

```python
name = input("Enter your name: ")
```

The value entered is stored in `name`.

By default, input is stored as a string.

---

# Part 17 — Converting Input to an Integer

If the user enters:

```text
5
```

Python initially treats it as text.

We can convert it to an integer:

```python
number = int(input("Enter a number: "))
```

Now `number` can be used in mathematical operations.

### Try it

Ask the user for:

* their age
* their score

Convert both to integers and display their total.

---

# Part 18 — Conditional Statements

Programs often need to make decisions.

```python
if score >= 50:
    print("Pass")
else:
    print("Fail")
```

There can also be multiple possibilities:

```python
if score >= 80:
    print("A")
elif score >= 50:
    print("B")
else:
    print("C")
```

---

# Part 19 — Combining Conditions

Conditions can be combined using:

```python
and
or
```

For example:

```python
if age >= 13 and age <= 18:
    print("Teenager")
```

Both conditions must be true.

With `or`, only one needs to be true:

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

# Part 20 — Checking Whether a Position Is Available

Imagine a cinema booking program.

A seat contains either:

```text
-
```

for available, or:

```text
X
```

for booked.

The program could check:

```python
if seats[row][column] == "X":
    print("Seat already booked")
else:
    seats[row][column] = "X"
```

This same idea can be used when checking whether a position on a game board is already occupied.

### Your task

Create a 5 × 5 seating plan.

Ask the user for a seat.

If it contains `X`, display:

```text
Seat unavailable
```

Otherwise place an `X` there.

---

# Part 21 — Random Numbers

The Battleship CPU needs to make decisions without the player telling it what to do.

Python's `random` module can generate random numbers.

First:

```python
import random
```

Then:

```python
number = random.randint(1, 10)
```

generates a random integer from 1 to 10.

For example, it might generate:

```text
4
```

or:

```text
9
```

or:

```text
1
```

---

# Part 22 — Random Coordinates

A computer could randomly choose a position on a 10 × 10 board:

```python
row = random.randint(0, 9)
column = random.randint(0, 9)
```

It can then access:

```python
grid[row][column]
```

### Your task

Create a 5 × 5 grid and have the computer randomly select one position.

Change that position to `X`.

Display the result.

---

# Part 23 — Keeping Random Objects on the Board

Suppose an object is five spaces long.

If the starting position is too close to the right edge, the object won't fit.

For a board containing positions 0–9, a five-space object could start at:

```text
0
1
2
3
4
5
```

but not:

```text
6
7
8
9
```

The maximum starting position depends on the object's length.

This means random starting positions can be calculated rather than simply using:

```python
random.randint(0, 9)
```

### Think about it

If an object has length `3` and the board has 10 positions, what should the maximum starting position be?

Work this out before continuing.

---

# Part 24 — `break`

`break` immediately stops a loop.

For example:

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

The output is:

```text
0
1
2
3
4
```

When `number` reaches 5, the loop stops.

### Try it

Create a loop that searches through a list of numbers.

Stop searching when the number `7` is found.

---

# Part 25 — `try` and `except`

Sometimes user input can cause an error.

For example:

```python
number = int(input("Enter a number: "))
```

If the user enters:

```text
hello
```

Python cannot convert `"hello"` into an integer.

A `try` block allows us to attempt an operation:

```python
try:
    number = int(input("Enter a number: "))
```

An `except` block handles an error:

```python
except:
    print("Invalid input")
```

Together:

```python
try:
    number = int(input("Enter a number: "))
except:
    print("Invalid input")
```

### Why is this useful in a game?

A player might enter a coordinate that doesn't exist.

For example:

```text
12
```

on a board that only contains positions 0–9.

The program needs to deal with unexpected input rather than crashing.

---

# Part 26 — `for...else`

Python has a less commonly used structure:

```python
for number in numbers:
    if number == 5:
        break
else:
    print("5 was not found")
```

The `else` runs when the `for` loop finishes **without using `break`**.

For example, if the list contains:

```python
[1, 2, 3]
```

the loop finishes normally and the `else` runs.

If the list contains:

```python
[1, 2, 5, 3]
```

the loop uses `break`, so the `else` does not run.

This is useful when checking whether **any** position in a proposed object is unavailable.

---

# Part 27 — Planning a Function

Before writing a function, identify:

### Input

What information does the function need?

### Process

What does the function do?

### Output

What information does the function need to return?

For example, consider a function that calculates a student's average.

```text
Input:
Two marks

Process:
Add marks
Divide by 2

Output:
Average
```

This can become:

```python
def calculate_average(mark1, mark2):
```

The parameters are the inputs.

The returned average is the output.

---

# Part 28 — Applying This to Battleship

Before writing each Battleship function, identify its responsibility.

You should be able to answer:

```text
What does this function need?
What does it do?
What does it return?
```

Use the following development order.

---

# Function 1 — `create_board()`

## Goal

Create and return a 10 × 10 matrix.

## Skills required

You need to use:

* lists
* nested lists
* nested `for` loops
* `.append()`
* `return`

## Planning

```text
Input:
None

Process:
Create an empty list
Create 10 rows
Create 10 columns in each row
Place "-" in each position
Add each row to the board

Output:
10 × 10 matrix
```

### Your task

Write:

```python
def create_board():
```

Do not look at the finished Battleship program.

Use your 4 × 4 map example as a starting point.

---

# Function 2 — `setup_player()`

## Goal

Create the player's board and allow them to place:

```text
Carrier       5
Battleship    4
Cruiser       3
Submarine     3
Destroyer     2
```

## Skills required

You will need:

* function calls
* dictionaries
* `.items()`
* `for` loops
* `while` loops
* Boolean variables
* `input()`
* `int()`
* `if`
* `elif`
* `else`
* matrix indexing
* nested loops

---

## Step 1 — Create the board

Call your `create_board()` function.

You now have a blank board.

---

## Step 2 — Store the ships

Think back to the dictionary example.

Create a dictionary where:

```text
key = ship name
value = ship length
```

---

## Step 3 — Loop through the ships

Use `.items()` to retrieve:

```text
ship name
ship length
```

You need this because the same placement process happens for every ship.

---

## Step 4 — Ask for orientation

The player needs to choose:

```text
1 = Horizontal
2 = Vertical
```

Use an `if` statement to determine which placement process should occur.

---

## Step 5 — Ask for coordinates

For a horizontal ship, think carefully about:

```text
row stays the same
column changes
```

For a vertical ship:

```text
column stays the same
row changes
```

---

## Step 6 — Check every position

Before placing a ship, examine every position it will occupy.

Ask:

> Is this position already occupied?

If any position contains `S`, the placement is invalid.

---

## Step 7 — Place the ship

Only once the required positions have been checked should the ship be placed.

Use:

```text
S
```

to represent a ship.

---

## Step 8 — Repeat until successful

Use a Boolean variable and a `while` loop.

The basic idea is:

```text
placement = False

WHILE placement is False
    ask for placement
    check placement
    if successful
        placement = True
```

---

# Function 3 — `setup_cpu()`

## Goal

Create the CPU's board and randomly place the same five ships.

## Skills required

You will use:

* everything from `setup_player()`
* `random.randint()`
* random orientations
* random coordinates
* `for...else`

---

## What changes?

The player chooses:

```text
orientation
row
column
```

The CPU needs to generate these values.

For example:

```python
orient = random.randint(1, 2)
```

The CPU can randomly choose its orientation.

You then need to generate an appropriate starting coordinate.

---

## Important problem

The CPU cannot simply choose any starting coordinate.

If the ship is five spaces long, it cannot start too close to an edge.

Calculate the maximum possible starting position using the ship length.

---

## Avoiding overlaps

The CPU must also check whether a proposed position already contains `S`.

The process should be:

```text
Choose random position
        ↓
Check every required position
        ↓
Was an occupied position found?
        ↓
YES → reject placement
NO  → place ship
```

Use the `for...else` technique from earlier.

---

# Function 4 — `player_turn()`

## Goal

Allow the player to attack the CPU's board.

## Skills required

You will use:

* parameters
* matrix indexing
* `input()`
* `int()`
* `if`
* `elif`
* `else`
* `while`
* `try`
* `except`
* Boolean variables

---

## Inputs

The function needs two boards:

```text
battle board
CPU board
```

Think carefully about why it needs both.

The CPU board tells the program whether the selected position contains a ship.

The battle board records what the player has discovered.

---

## Attack process

The basic algorithm is:

```text
Display the battle board

Ask for row
Ask for column

Check the CPU board

If there is a ship:
    record a hit

Otherwise:
    record a miss
```

Use:

```text
X = hit
O = miss
```

---

## Preventing repeated attacks

The player shouldn't be able to attack the same position repeatedly.

Before accepting an attack, check whether the battle board already contains:

```text
X
```

or:

```text
O
```

If it does, the player needs to try again.

---

# Function 5 — `check_win()`

## Goal

Determine whether the player has destroyed every CPU ship.

## Skills required

You will use:

* nested loops
* counters
* conditionals
* Boolean return values

---

## Think about the problem

The board contains 100 positions.

You need to search every position.

Whenever you find:

```text
X
```

increase a counter.

The total number of ship spaces is:

```text
5 + 4 + 3 + 3 + 2
```

Calculate this before writing the function.

---

## Return value

The function should return a Boolean.

Therefore:

```text
True
```

means the player has won.

```text
False
```

means the player has not won yet.

---

# Function 6 — `cpu_turn()`

## Goal

Allow the CPU to randomly attack the player's board.

## Skills required

You will use:

* `random.randint()`
* matrix indexing
* `while`
* Boolean variables
* conditionals
* `try`
* `except`

---

## Algorithm

Think of the CPU turn as:

```text
Choose random row
Choose random column
        ↓
Has this position already been attacked?
        ↓
YES → choose another position
NO  → record hit or miss
```

The CPU does not need to ask the player for coordinates.

---

# Function 7 — `check_lose()`

## Goal

Determine whether the CPU has destroyed all of the player's ship spaces.

This function uses the same fundamental counting technique as `check_win()`.

The important programming concept is that **the same algorithm can be used for different purposes**.

You should be able to build this function yourself after completing `check_win()`.

---

# Function 8 — `main()`

## Goal

Control the overall game.

This function should not contain all the game logic.

Instead, it should call the functions you have already created.

Think about the order.

First:

```text
Create CPU board
```

Then:

```text
Create player board
```

Then:

```text
Create attack board
```

Then the game begins.

---

## The game loop

Each cycle of the game follows:

```text
Player turn
     ↓
Check win
     ↓
CPU turn
     ↓
Check lose
     ↓
Repeat
```

Use a Boolean variable to control the loop.

---

# Part 29 — Passing Data Between Functions

This is one of the most important concepts in the project.

Consider:

```python
def display_board(board):
```

The function receives a board.

Another function might create that board:

```python
board = create_board()
```

The board can then be passed into another function:

```python
display_board(board)
```

The same piece of data can therefore be used by several functions.

In Battleship, this is essential.

The boards need to move between functions.

---

# Part 30 — Parameters vs Return Values

These two concepts are easy to confuse.

### Parameter

Information going **into** a function.

```python
def display_score(score):
```

`score` is a parameter.

### Return value

Information coming **out** of a function.

```python
def calculate_score():
    return score
```

You can remember:

```text
PARAMETER
     ↓
  FUNCTION
     ↓
RETURN VALUE
```

---

# Part 31 — Building the Program in the Correct Order

Do not try to write the entire Battleship program at once.

Build it incrementally.

### Stage 1

Create:

```text
create_board()
```

Test that it produces a 10 × 10 board.

---

### Stage 2

Create:

```text
setup_player()
```

Test that all five ships can be placed.

---

### Stage 3

Create:

```text
setup_cpu()
```

Test that the CPU can randomly place all five ships.

---

### Stage 4

Create:

```text
player_turn()
```

Test hits, misses and repeated attacks.

---

### Stage 5

Create:

```text
check_win()
```

Test whether 17 hits are correctly detected.

---

### Stage 6

Create:

```text
cpu_turn()
```

Test that the CPU can randomly attack the player's board.

---

### Stage 7

Create:

```text
check_lose()
```

Test whether 17 CPU hits are detected.

---

### Stage 8

Create:

```text
main()
```

Connect all the functions together.

---

# Part 32 — Testing Each Function

Do not wait until the entire game is finished before testing.

For each function, create a small test.

For example:

### `create_board()`

Check:

```text
Does it have 10 rows?
Does every row have 10 positions?
Does every position contain "-"?
```

### `setup_player()`

Check:

```text
Can all five ships be placed?
Can horizontal ships be placed?
Can vertical ships be placed?
Are overlapping ships rejected?
```

### `setup_cpu()`

Check:

```text
Are five ships created?
Are ships within the board?
Do ships overlap?
```

### `player_turn()`

Check:

```text
Does a ship produce a hit?
Does an empty position produce a miss?
Are previous attacks rejected?
```

### `check_win()`

Check:

```text
0 hits → False
16 hits → False
17 hits → True
```

### `cpu_turn()`

Check:

```text
Does the CPU select a position?
Does it record hits?
Does it record misses?
Does it avoid previous attacks?
```

### `check_lose()`

Check:

```text
0 hits → False
16 hits → False
17 hits → True
```

---

# Part 33 — Debugging Strategy

When something goes wrong, don't immediately rewrite the whole program.

Identify:

### 1. What did I expect?

For example:

```text
The ship should occupy three spaces.
```

### 2. What actually happened?

```text
Only two spaces were occupied.
```

### 3. Which function is responsible?

Probably the ship placement function.

### 4. Which variable is involved?

Perhaps:

```text
v
x_pos
y_pos
i
```

### 5. What are their values?

Use temporary `print()` statements to investigate.

For example:

```python
print(v)
print(x_pos)
print(y_pos)
```

This lets you see what the program is actually doing.

---

# Part 34 — Common Errors to Look For

## Index errors

This happens when you try to access a position that doesn't exist.

For a 10 × 10 board:

```text
Valid:
0–9

Invalid:
10+
```

Remember that a ship occupies multiple positions, so you need to consider **every position**, not just the starting position.

---

## Infinite loops

If you have:

```python
while placement == False:
```

something inside the loop must eventually change `placement`.

Otherwise the loop may never finish.

---

## Incorrect indentation

Python uses indentation to determine which statements belong to a loop or conditional.

For example:

```python
if score > 50:
    print("Pass")
```

The indentation is part of the syntax.

---

## Incorrect matrix indexing

Remember:

```python
grid[row][column]
```

The first index selects the inner list.

The second selects an item within that list.

---

# Part 35 — Final Skills Checklist

Before submitting your Battleship program, make sure you can explain each of these.

### Functions

* [ ] Define a function
* [ ] Call a function
* [ ] Pass parameters
* [ ] Return values
* [ ] Explain why functions are useful

### Selection

* [ ] Use `if`
* [ ] Use `elif`
* [ ] Use `else`
* [ ] Combine conditions with `and` and `or`

### Iteration

* [ ] Use `for`
* [ ] Use `while`
* [ ] Use nested loops
* [ ] Use `break`
* [ ] Understand `for...else`

### Data structures

* [ ] Create lists
* [ ] Add items using `.append()`
* [ ] Access list elements
* [ ] Create two-dimensional lists
* [ ] Access matrix elements
* [ ] Create dictionaries
* [ ] Use `.items()`

### Input and output

* [ ] Use `input()`
* [ ] Convert input using `int()`
* [ ] Use f-strings
* [ ] Use `print()`

### Randomisation

* [ ] Import `random`
* [ ] Use `random.randint()`
* [ ] Generate random coordinates
* [ ] Generate random choices

### Error handling

* [ ] Understand `try`
* [ ] Understand `except`
* [ ] Handle invalid input

### Program design

* [ ] Break a large problem into functions
* [ ] Identify inputs, processes and outputs
* [ ] Pass data between functions
* [ ] Use return values
* [ ] Test functions individually
* [ ] Build the program incrementally
* [ ] Use a main function to control program flow

---

# Final Challenge

You should now build the Battleship program **function by function**.

Do not begin by writing `main()`.

Start with:

```python
create_board()
```

Once it works, move to:

```python
setup_player()
```

Then:

```python
setup_cpu()
```

Then:

```python
player_turn()
```

Then:

```python
check_win()
```

Then:

```python
cpu_turn()
```

Then:

```python
check_lose()
```

Finally:

```python
main()
```

The goal is not to copy a completed program.

The goal is to be able to look at a problem such as:

> "Create a function that randomly places a five-space object on a 10 × 10 grid without overlapping an existing object."

and identify the programming skills required to solve it:

```text
Function
    ↓
2D list
    ↓
Random numbers
    ↓
Loops
    ↓
Matrix indexing
    ↓
Conditionals
    ↓
Boolean / loop control
```

That is the skill you are developing throughout this project.
