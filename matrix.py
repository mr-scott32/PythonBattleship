# Matrix Creation
matrix = []     # Create an empty list to store the rows

for i in range(5):  # Repeat 5 times to create 5 rows
    row = []        # Create an empty list for the current row

    for j in range(5):  # Repeat 5 times to create 5 columns
        row.append('-') # Add a '-' to the current row

    matrix.append(row)  # Add the completed row to the matrix


# Matrix Print
for i in range(5):                      # Repeat for each row
    for j in range(5):                  # Repeat for each column in the current row
        print(matrix[i][j], end=' ')    # Access and print the current matrix element
    print()                             # Move to the next line after each row