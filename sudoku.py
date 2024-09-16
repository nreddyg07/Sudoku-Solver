M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ") # to print the sudoku grid
        print()

def solve(grid, row, col, num):
    for x in range(M): # to check for empty spaces in the row
        if grid[row][x] == num:
            return False          
    for x in range(M):
        if grid[x][col] == num: # to check for empty spaces in the column
            return False
# defining the starting point of the 3x3 box
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num: # to check for the numbers in the 3x3 box
                return False
    return True
 
def Suduko(grid, row, col):
   if (row == M - 1 and col == M): # to exit form whole sudoku puzzle
        return True
   if col == M: # to go to next row
        row += 1
        col = 0
   if grid[row][col] > 0: # to check wheather the box has to be solved or not
        return Suduko(grid, row, col + 1)
   for num in range(1, M + 1): 
       if solve(grid, row, col, num): # to solve the above function and if it returns true then the value of num is assigned to that box 
          grid[row][col] = num
          if Suduko(grid, row, col + 1): # to check for the column
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]
 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")

