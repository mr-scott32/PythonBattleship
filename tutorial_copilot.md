 # Building Battleship in Python

## A project tutorial for students

In this project you will build a text-based Battleship game. You will learn
Python by making a real game in small, testable pieces.

This is a guide, not a typing exercise. There are several good ways to build
the game. The examples below give you a working direction, but you should
make choices about the interface, symbols, rules, and computer strategy.

By the end, your program should be able to:

* create a 10 by 10 board
* place five ships without overlapping them
* let a human player attack
* let the computer attack
* show hits and misses
* detect when one side has lost all 17 ship spaces

The file `main.py` is the reference version for this tutorial. You can build
your own version in the same file, or create a new file such as `student_game.py`
while you experiment.

---

## 1. Start with the rules

Before writing code, describe the game in ordinary language.

The standard fleet in this project is:

| Ship | Length |
| --- | ---: |
| Carrier | 5 |
| Battleship | 4 |
| Cruiser | 3 |
| Submarine | 3 |
| Destroyer | 2 |

The total number of ship spaces is 17. Each player has a 10 by 10 board.
Players take turns choosing a row and column. A hit is marked with `X` and a
miss with `O`.

### Design decisions

Write down your answers before coding:

1. Will coordinates start at 0 or 1?
2. Will rows be entered before columns?
3. What will an empty space look like?
4. Will a hit give the player another turn?
5. Should ships be visible after they are placed?
6. What should happen when the player types letters instead of numbers?

The reference program uses coordinates from 0 through 9, stores a board as
`grid[row][column]`, and uses these symbols:

```text
-  empty water
S  ship
X  hit
O  miss
```

There is no single correct interface. You could use emojis, letters for rows,
colored terminal output, or a numbered menu. Make the rules clear to the
person playing your game.

### Small planning exercise

Draw a 5 by 5 board on paper. Pick a starting square and a direction for a
ship of length 3. List every coordinate that the ship would occupy.

For example, starting at row 1, column 2 and moving horizontally gives:

```text
(1, 2), (1, 3), (1, 4)
```

This is the pattern your Python loops will eventually create.

---

## 2. Make a tiny Python program first

Create a file and begin with something you can run immediately:

```python
print('Welcome to Battleship!')
```

Run it from the project folder:

```text
python main.py
```

If your computer uses a different command, try `python3 main.py`.

### Concepts introduced

* `print()` displays information.
* A string is text inside quotes.
* Python runs instructions from top to bottom.

### Try it

Add a title, a short rules message, and your name as the game designer. Run
the program after each change. Frequent small tests make mistakes easier to
find.

---

## 3. Put repeated work in functions

A function is a named block of code with one job. Define a function with
`def`, then call it by writing its name followed by parentheses.

```python
def show_title():
	print('=== BATTLESHIP ===')


show_title()
```

The function does not run when Python reads the `def` line. It runs when you
call `show_title()`.

### Why functions help

The finished game has separate jobs:

```text
create_board  make an empty board
setup_player  let the player place ships
setup_cpu     place CPU ships randomly
player_turn   process one player attack
cpu_turn      process one CPU attack
check_win     decide whether the player won
check_lose    decide whether the player lost
main          control the order of the game
```

This is modular programming. Each function is easier to understand and test
when it has one clear responsibility.

### Try it

Create `show_rules()` and make it print three rules. Call both
`show_title()` and `show_rules()` from the bottom of the file.

---

## 4. Build one row with a list

Lists store multiple values in order.

```python
row = ['-', '-', '-', '-', '-']
print(row)
```

Instead of typing every value, use a loop:

```python
row = []

for column in range(5):
	row.append('-')

print(row)
```

`range(5)` produces five loop values: 0, 1, 2, 3, and 4. The loop variable
`column` is a name for the current repeat; Python does not require you to use
the name `i`.

### Concepts introduced

* `[]` creates an empty list.
* `.append(value)` adds one value to the end.
* A `for` loop repeats a block.
* Indentation tells Python which statements belong to the loop.

### Try it

Change the program to create a row with 10 positions. Print the length using
`len(row)`. What does `len(row)` tell you?

---

## 5. Turn a row into a board

A Battleship board is a list containing rows. This is often called a 2D list
or matrix.

```python
def create_board():
	grid = []

	for row_number in range(10):
		row = []

		for column_number in range(10):
			row.append('-')

		grid.append(row)

	return grid
```

There are two loops because there are two dimensions:

* the outer loop creates 10 rows
* the inner loop creates 10 columns in each row

`return grid` sends the finished board back to the caller.

Test the function:

```python
board = create_board()
print(len(board))
print(len(board[0]))
```

Both values should be 10.

### Indexing a board

Python starts counting at zero. `board[0]` is the first row, and
`board[0][0]` is the first cell. The general pattern is:

```python
board[row][column]
```

Try changing one cell:

```python
board[2][4] = 'S'
print(board[2][4])
```

### A common mistake

Do not create every row by reusing the same list object. Build a new `row = []`
inside the outer loop. Otherwise changing one row can unexpectedly change all
rows.

---

## 6. Display the board

A nested loop can visit every cell and print it:

```python
def display_board(grid):
	for row in grid:
		for cell in row:
			print(cell, end=' ')
		print()
```

The inner `print()` uses `end=' '` so cells stay on the same line. The final
`print()` moves to the next row.

You can also display coordinate labels:

```python
def display_board(grid):
	print('  ' + ' '.join(str(number) for number in range(10)))

	for row_number, row in enumerate(grid):
		print(str(row_number) + ' ' + ' '.join(row))
```

This version is more useful during a game because players can see which row
and column to enter.

### Creative choices

Experiment with:

* borders around the board
* `~` for water instead of `-`
* separate display functions for your own board and the hidden enemy board
* color, if your terminal supports it

Keep the data in the board simple even if the display is fancy. That makes
the game rules easier to reason about.

---

## 7. Store the fleet in a dictionary

A dictionary connects keys to values. It is a good fit for ship names and
lengths:

```python
ships = {
	'Carrier': 5,
	'Battleship': 4,
	'Cruiser': 3,
	'Submarine': 3,
	'Destroyer': 2,
}
```

Loop through both pieces of information with `.items()`:

```python
for ship_name, ship_length in ships.items():
	print(ship_name, ship_length)
```

This is better than writing nearly identical placement code five times. If
you add a new ship to the dictionary, the loop can use it automatically.

### Concepts introduced

* dictionary keys identify values
* `.items()` gives a key and value together
* descriptive variable names make loops easier to read

### Try it

Add a custom ship. Decide whether the win condition should now be calculated
from the dictionary instead of staying fixed at 17.

---

## 8. Place a ship on a board

For a horizontal ship, the row stays the same while the column changes:

```python
row = 3
start_column = 4
ship_length = 3

for offset in range(ship_length):
	grid[row][start_column + offset] = 'S'
```

The cells are `(3, 4)`, `(3, 5)`, and `(3, 6)`.

For a vertical ship, the column stays the same while the row changes:

```python
start_row = 3
column = 4
ship_length = 3

for offset in range(ship_length):
	grid[start_row + offset][column] = 'S'
```

The cells are `(3, 4)`, `(4, 4)`, and `(5, 4)`.

Notice the shared idea: `offset` counts from zero through one less than the
ship length. The direction decides whether the offset is added to the row or
the column.

### Draw before you code

For a ship of length 4 starting at row 2, column 1, list the horizontal and
vertical coordinates on paper. Then ask: which coordinate changes?

---

## 9. Validate placement before changing the board

A good game checks a proposed move before it writes any `S` values. The move
is valid only when:

1. every coordinate is inside the board
2. every destination cell is empty

One clear approach is to calculate the proposed coordinates first:

```python
def get_ship_cells(row, column, length, orientation):
	cells = []

	for offset in range(length):
		if orientation == 'H':
			cells.append((row, column + offset))
		else:
			cells.append((row + offset, column))

	return cells


def can_place_ship(grid, cells):
	for row, column in cells:
		if row < 0 or row >= 10 or column < 0 or column >= 10:
			return False
		if grid[row][column] != '-':
			return False

	return True
```

Only after validation should you place the ship:

```python
def place_ship(grid, cells):
	for row, column in cells:
		grid[row][column] = 'S'
```

This separates two questions:

* Is the move allowed?
* How do we apply an allowed move?

That separation prevents half a ship from being placed before discovering
that the rest would go off the board.

### Important debugging lesson

The original student version checks `y_pos > 9` or `x_pos > 9`, but that does
not fully prove that every cell fits. A ship can start at 8 and still extend
past the edge. It can also index the board before the boundary check is useful.
The `can_place_ship()` approach checks each proposed destination first.

### Try it

Write tests using a small 5 by 5 board:

* a ship entirely inside the board should be accepted
* a ship extending past the right edge should be rejected
* a ship extending past the bottom edge should be rejected
* a ship overlapping `S` should be rejected

---

## 10. Let the player place ships

Now combine input, dictionaries, loops, and placement validation.

The overall shape is:

```python
def setup_player():
	grid = create_board()

	for ship_name, ship_length in ships.items():
		placed = False

		while not placed:
			print(f'Placing {ship_name}, length {ship_length}.')
			row = int(input('Starting row: '))
			column = int(input('Starting column: '))
			orientation = input('Horizontal or vertical? H/V: ').upper()

			cells = get_ship_cells(row, column, ship_length, orientation)

			if can_place_ship(grid, cells):
				place_ship(grid, cells)
				placed = True
			else:
				print('That placement is not valid. Try again.')

		display_board(grid)

	return grid
```

This uses a Boolean flag. `placed` begins as `False`; the loop continues until
a valid placement changes it to `True`.

### Make input safer

`int(input(...))` works for numbers, but crashes when the player types `hello`.
Use a `try` block while you are learning:

```python
try:
	row = int(input('Starting row: '))
except ValueError:
	print('Please enter a whole number.')
```

For a polished version, put input conversion in a reusable function that
keeps asking until the value is valid.

### Creative choices

You could allow:

* `H` and `V`, or words such as `horizontal`
* players to choose whether ships can touch
* random placement after a player chooses a difficulty
* a preview of the proposed ship before accepting it

---

## 11. Place the CPU fleet randomly

The `random` module can choose numbers for the computer:

```python
import random

row = random.randint(0, 9)
column = random.randint(0, 9)
orientation = random.choice(['H', 'V'])
```

The CPU can reuse the same validation functions as the player. The only
difference is where its proposed move comes from:

```python
def setup_cpu():
	grid = create_board()

	for ship_name, ship_length in ships.items():
		placed = False

		while not placed:
			row = random.randint(0, 9)
			column = random.randint(0, 9)
			orientation = random.choice(['H', 'V'])
			cells = get_ship_cells(row, column, ship_length, orientation)

			if can_place_ship(grid, cells):
				place_ship(grid, cells)
				placed = True

	return grid
```

The loop may need several attempts. That is normal: a random proposal is not
always legal.

### Think like a tester

Run `setup_cpu()` several times. Check that every board has exactly 17 `S`
cells and that no ship leaves the board. A random program should still obey
the rules every time.

---

## 12. Represent the two sides clearly

The game needs more than one board:

```text
cpu_grid       where the CPU ships are
player_grid    where the player ships are
battle_grid    what the player has discovered about the CPU board
```

Keeping `battle_grid` separate hides the CPU ships. The player sees `X` or
`O`, but not the undiscovered `S` positions in `cpu_grid`.

This is a useful programming idea: one piece of data can be the complete
truth, while another is a view designed for a particular user.

### Try it

Add a `display_hidden_board()` function that shows `X` and `O` but replaces
unknown cells with `-`, even if the underlying CPU board contains `S`.

---

## 13. Implement a player turn

A player turn follows a repeatable sequence:

1. display the known enemy board
2. ask for a row and column
3. reject coordinates outside the board
4. reject a cell already targeted
5. check the CPU board for a ship
6. mark a hit or miss
7. finish the turn

A simplified version looks like this:

```python
def player_turn(battle_grid, cpu_grid):
	while True:
		display_board(battle_grid)
		row = int(input('Attack row: '))
		column = int(input('Attack column: '))

		if row < 0 or row >= 10 or column < 0 or column >= 10:
			print('That coordinate is outside the board.')
			continue

		if battle_grid[row][column] in ['X', 'O']:
			print('You already attacked there.')
			continue

		if cpu_grid[row][column] == 'S':
			print('Hit!')
			battle_grid[row][column] = 'X'
		else:
			print('Miss!')
			battle_grid[row][column] = 'O'

		return battle_grid
```

The `continue` statement skips to the next loop attempt. `return` ends the
function after a valid attack.

### Notice the separation

The code reads the result from `cpu_grid`, but writes the mark to
`battle_grid`. That prevents the player from accidentally seeing or changing
the CPU's hidden board.

---

## 14. Implement a CPU turn

The first CPU can choose random coordinates:

```python
def cpu_turn(player_grid):
	while True:
		row = random.randint(0, 9)
		column = random.randint(0, 9)

		if player_grid[row][column] in ['X', 'O']:
			continue

		if player_grid[row][column] == 'S':
			print('The CPU hit your ship!')
			player_grid[row][column] = 'X'
		else:
			print('The CPU missed.')
			player_grid[row][column] = 'O'

		return player_grid
```

The CPU must not attack a cell it already attacked. The `while True` loop
keeps choosing until it finds a new cell.

### Upgrade the strategy

After the random version works, choose one improvement:

* remember a hit and target neighboring cells
* keep a list of untried coordinates
* add easy, medium, and hard difficulty levels
* let the CPU take another turn after a hit

Build one small change at a time and test after each change.

---

## 15. Check for a winner

One way to count hits is to inspect every cell:

```python
def count_hits(grid):
	count = 0

	for row in grid:
		for cell in row:
			if cell == 'X':
				count += 1

	return count


def check_win(battle_grid):
	return count_hits(battle_grid) == 17
```

The original program has both `check_win()` and `check_lose()`. They perform
the same counting operation on different boards, so you could reuse
`count_hits()` and make the two checks more readable.

A stronger design calculates the target from the fleet:

```python
fleet_size = sum(ships.values())
```

Then adding a ship does not require remembering to change `17` elsewhere.

### Try it

Test `count_hits()` with a handmade board containing zero, one, and several
`X` values. Testing small functions with simple data is faster than testing
only through the full game.

---

## 16. Connect everything in `main()`

The `main()` function controls the story of the game:

```python
def main():
	cpu_grid = setup_cpu()
	player_grid = setup_player()
	battle_grid = create_board()

	while True:
		player_turn(battle_grid, cpu_grid)

		if check_win(battle_grid):
			print('You win!')
			break

		cpu_turn(player_grid)

		if check_lose(player_grid):
			print('You lose!')
			break
```

The order matters:

1. create both ship boards
2. create a blank hidden-information board
3. let the player attack
4. check whether the player won
5. let the CPU attack
6. check whether the player lost
7. repeat until `break`

The final guard makes sure the game starts only when the file is run directly:

```python
if __name__ == '__main__':
	main()
```

This lets you import functions into a test file without automatically
starting an interactive game.

---

## 17. Test in layers

Do not wait until the whole game is finished to test it.

### Board tests

* Does `create_board()` return 10 rows?
* Does every row contain 10 cells?
* Are all cells initially `-`?

### Placement tests

* Can a horizontal ship fit at the left edge?
* Can a vertical ship fit at the bottom edge?
* Are overlapping ships rejected?
* Does every accepted fleet contain 17 ship cells?

### Attack tests

* Does a ship cell become `X`?
* Does an empty cell become `O`?
* Is a repeated attack rejected?
* Are negative and out-of-range coordinates rejected?

### Game tests

* Does the player win after all CPU ship spaces are hit?
* Does the player lose after all their ship spaces are hit?
* Does the game stop immediately after either result?

You can use a small board while debugging. A 5 by 5 board makes it easier to
see every cell and quickly create edge cases.

---

## 18. Debugging habits

When something goes wrong, do not guess. Reduce the problem.

1. Read the error message and note the line number.
2. Print the values immediately before the failing line.
3. Check whether the row and column mean what you think they mean.
4. Test the smallest function involved.
5. Remove temporary debug prints when the problem is solved.

Useful temporary checks include:

```python
print('DEBUG:', row, column, orientation)
print('DEBUG board size:', len(grid), len(grid[0]))
```

### Current-version challenges

The reference `main.py` is a learning project, so it deliberately leaves
some improvements for you:

* invalid text input can raise `ValueError`
* placement should check every destination before writing
* invalid orientation input should ask again instead of moving on
* `check_win()` and `check_lose()` can share a helper
* the CPU can avoid repeated guesses with a dedicated list or set
* a variable named `stored_hit` is created but not used

Treat these as programming challenges. Fix one, write down what changed, and
test the behavior again.

---

## 19. Make the game yours

Once the basic version works, choose features that interest you. Here are
some possible paths:

### Interface

* add row and column labels
* add a menu for new game, rules, and quit
* show ship names and sunk messages
* add color or sound

### Rules

* allow diagonal ships
* prevent ships from touching
* give another turn after a hit
* support a two-player mode
* add a turn limit

### Data and design

* store each ship as a dictionary with a name, length, cells, and hits
* use constants for board size and symbols
* create a reusable `Board` class
* load and save a game
* add a replay or statistics screen

### Computer opponent

* add difficulty levels
* target cells next to a successful hit
* record the CPU's previous guesses in a set
* make the CPU choose between safe and aggressive moves

For each feature, describe the rule in plain English first. Then identify
which function owns that rule. Finally, make the smallest code change that
implements it and test the old behavior as well as the new behavior.

---

## 20. Suggested project checklist

Use this as a progress tracker:

- [ ] I can run a Python file from the terminal.
- [ ] I can define and call a function.
- [ ] I can create and update a list.
- [ ] I understand `grid[row][column]`.
- [ ] I can create and display a 10 by 10 board.
- [ ] I can loop through a dictionary of ships.
- [ ] I can calculate horizontal and vertical ship cells.
- [ ] I reject invalid and overlapping placement.
- [ ] The player can place every ship.
- [ ] The CPU can place every ship randomly.
- [ ] The player can make a valid attack.
- [ ] The CPU can make a valid attack.
- [ ] The game detects both win and lose conditions.
- [ ] I tested edge cases deliberately.
- [ ] I added at least one feature of my own.

The most important lesson is not the final number of lines. It is learning to
turn a large idea into small functions, test each function, and make your own
decisions about how the finished game should feel.
