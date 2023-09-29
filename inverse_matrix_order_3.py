
def transposition(matrix):
    new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            if matrix[j][i].is_integer():
                new_matrix[i][j] = (int(matrix[j][i]))
            else:
                new_matrix[i][j] = matrix[j][i]
    return new_matrix


def determinant_order_3(matrix):
    mat = []
    line = []
    for i in range(3):
        for j in range(3):
            line.append(matrix[i][j])
        if line:
            mat.append(line)
        line = []
    return (mat[0][0] * mat[1][1] * mat[2][2]) + (mat[0][1] * mat[1][2] * mat[2][0]) + (
        mat[0][2] * mat[1][0] * mat[2][1]) - (mat[0][2] * mat[1][1] * mat[2][0]) - (
        mat[0][1] * mat[1][0] * mat[2][2]) - (mat[0][0] * mat[1][2] * mat[2][1])


def determinant_order_2(matrix, m, n):
    mat = []
    line = []
    for i in range(0, 3):
        for j in range(0, 3):
            if j != n and i != m:
                line.append(matrix[i][j])
        if line:
            mat.append(line)
        line = []
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


def matrix_calc(matrix):
    determinant = determinant_order_3(matrix)
    if determinant == 0:
        print(f'Обратная матрица не существует т.к определитель равен 0')
        exit()
    else:
        inverse_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
        for i in range(1, 4):
            for j in range(1, 4):
                inverse_matrix[i - 1][j - 1] = (
                    determinant_order_2(matrix, i - 1, j - 1) * ((-1) ** (i + j)) * (1 / determinant))
        transpositioned_matrix = transposition(inverse_matrix)
        print('Обратная матрица третьего порядка:')
    for i in range(3):
        print(f'| {" | ".join(map(str, transpositioned_matrix[i]))} | ')