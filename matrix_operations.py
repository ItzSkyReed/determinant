def determinant(matrix):
    try:
        if len(matrix[0]) == 4:
            deter = determinant_order_4(matrix)
        elif len(matrix[0]) == 3:
            deter = determinant_order_3(matrix)
        elif len(matrix[0]) == 2:
            deter = determinant_order_2(matrix)
        else:
            deter = matrix[0][0]
        return deter
    except:
        print(Exception)


def determinant_order_2(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])


def determinant_order_3(matrix):
    deter = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (
            matrix[0][2] * matrix[1][0] * matrix[2][1]) - (matrix[0][2] * matrix[1][1] * matrix[2][0]) - (
                    matrix[0][1] * matrix[1][0] * matrix[2][2]) - (matrix[0][0] * matrix[1][2] * matrix[2][1])
    return deter


def determinant_order_4(matrix):
    deter = 0.0
    for i in range(4):
        mat_3 = []
        line = []
        for b in range(1, 4):
            for j in range(0, 4):
                if j != i:
                    line.append(matrix[b][j])
            if line:
                mat_3.append(line)
            line = []
        deter += ((-1) ** i) * matrix[0][i] * determinant_order_3(mat_3)
    return deter


def transposition(matrix):
    new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            if matrix[j][i].is_integer():
                new_matrix[i][j] = (int(matrix[j][i]))
            else:
                new_matrix[i][j] = matrix[j][i]
    return new_matrix


def inverse_matrix(matrix):
    deter = determinant(matrix)
    if deter == 0:
        print(f'Обратная матрица не существует т.к определитель равен 0')
        exit()
    else:
        inverse_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
        for i in range(1, 4):
            for j in range(1, 4):
                inverse_matrix[i - 1][j - 1] = (determinant_order_2(matrix))
        transpositioned_matrix = transposition(inverse_matrix)
        print([transpositioned_matrix, len(transpositioned_matrix[0]), len(transpositioned_matrix[0])])
        return [transpositioned_matrix, len(transpositioned_matrix[0]), len(transpositioned_matrix)]
