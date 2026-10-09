def is_valid(m, r, c, v):
    for i in range(4):
        if m[r][i] == v or m[i][c] == v:
            return False
    br, bc = (r // 2) * 2, (c // 2) * 2
    for i in range(br, br + 2):
        for j in range(bc, bc + 2):
            if m[i][j] == v:
                return False
    return True


def solve_sudoku(matrix):
    # базовый случай — нет пустых клеток
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                for v in range(1, 5):
                    if is_valid(matrix, i, j, v):
                        matrix[i][j] = v
                        # рекурсивный случай
                        if solve_sudoku(matrix):
                            return True
                        matrix[i][j] = 0
                return False
    return True


puzzle = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4],
]
for row in puzzle:
    print(row)
print()
solve_sudoku(puzzle)
for row in puzzle:
    print(row)