from flask import Flask, render_template, request

app = Flask(__name__)

M = 9

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        grid = [[int(request.form[f'cell_{i}{j}']) if request.form[f'cell_{i}{j}'] else 0 for j in range(M)] for i in range(M)]
        
        if Suduko(grid, 0, 0):
            return render_template('index.html', grid=grid, solved=True)
        else:
            return render_template('index.html', grid=grid, solved=False)

    grid = [[0 for _ in range(M)] for _ in range(M)]
    return render_template('index.html', grid=grid, solved=None)

if __name__ == '__main__':
    app.run(debug=True)
