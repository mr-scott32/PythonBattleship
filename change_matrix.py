# Matrix Creation
matrix = []                         # Create an empty list to store the rows

for i in range(5):                  # Repeat 5 times to create 5 rows
    row = []                        # Create an empty list for the current row

    for j in range(5):              # Repeat 5 times to create 5 columns
        row.append('-')             # Add a '-' to the current row

    matrix.append(row)              # Add the completed row to the matrix


# Get Coordinates
x_pos = int(input('Enter x coordinate from 0 to 4: '))  # Get the row position from the user
y_pos = int(input('Enter y coordinate from 0 to 4: '))  # Get the column position from the user

for i in range(5):                                      # Check each position needed for the placement
    if matrix[x_pos][y_pos+i] == 'X' or y_pos > 9:     # Check if the position is already occupied or outside the board
        print('Invalid placement!')                     # Tell the user that the placement is invalid
        break                                           # Stop checking the placement
    else:
        for i in range(v):                              # Repeat for the length of the ship
            matrix[x_pos][y_pos+i] = 'X'               # Place an 'X' at each position occupied by the ship
            placement = True                            # Record that the ship has been placed successfully


# Matrix Print
for i in range(5):                  # Repeat for each row
    for j in range(5):              # Repeat for each column in the current row
        print(matrix[i][j], end=' ') # Access and print the current matrix element
    print()                         # Move to the next line after each row