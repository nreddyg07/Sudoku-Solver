Steps to solve the Sudoku Puzzle in Python:
 In this method for solving the sudoku puzzle, first, we assign the size of the 2D matrix to a variable M (M*M).
 Then we assign the utility function (puzzle) to print the grid.
 Later it will assign num to the row and col.
 If we find the same num in the same row or same column or in the specific 3*3 matrix, ‘false’ will be returned.
 Then we will check if we have reached the 8th row and 9th column and return true for stopping further backtracking.
 Next, we will check if the column value becomes 9 then we move to the next row and column.
 Further now we see if the current position of the grid has a value greater than 0, then we iterate for the next column.
 After checking if it is a safe place, we move to the next column and then assign the num in the current (row, col) position of the grid. Later we check for the next possibility with the next column.
 As our assumption was wrong, we discard the assigned num and then we go for the next assumption with a different num value# Sudoku-Solver
