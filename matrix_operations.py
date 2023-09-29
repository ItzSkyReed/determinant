def determinant(matrix):
    if len(matrix[0]) == 4:
        deter = determinant_order_4(matrix)
    elif len(matrix[0]) == 3:
        deter = determinant_order_3(matrix)
    elif len(matrix[0]) == 2:
        deter = determinant_order_2(matrix)
    else:
        deter = matrix[0][0]
    return deter


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
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = []
    for i in range(m):
        line = []
        for j in range(n):
            if matrix[j][i].is_integer():
                line.append(int(matrix[j][i]))
            else:
                line.append(matrix[j][i])
        new_matrix.append(line)
    return new_matrix


def matrix_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def minor_to_matrix_3(matrix, separate_deter, deter):
    inversed_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(1, 4):
        for j in range(1, 4):
            if separate_deter:
                inversed_matrix[i - 1][j - 1] = (
                        (-1) ** (i + j) * determinant_order_2(matrix_minor(matrix, i - 1, j - 1)))
            else:
                inversed_matrix[i - 1][j - 1] = (
                        (-1) ** (i + j) * determinant_order_2(matrix_minor(matrix, i - 1, j - 1)) * (1 / deter))
    return inversed_matrix


def minor_to_matrix_4(matrix, separate_deter, deter):
    inversed_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(1, 5):
        for j in range(1, 5):
            if separate_deter:
                inversed_matrix[i - 1][j - 1] = (
                        (-1) ** (i + j) * determinant_order_3(matrix_minor(matrix, i - 1, j - 1)))
            else:
                inversed_matrix[i - 1][j - 1] = (
                        (-1) ** (i + j) * determinant_order_3(matrix_minor(matrix, i - 1, j - 1)) * (1 / deter))
    return inversed_matrix


def inverse_matrix(matrix, separate_deter):
    deter = 0
    if len(matrix) == 4:
        deter = determinant_order_4(matrix)
        if deter == 0:
            return 0
        matrix = minor_to_matrix_4(matrix, separate_deter, deter)
        matrix = transposition(matrix)
    elif len(matrix) == 3:
        deter = determinant_order_3(matrix)
        if deter == 0:
            return 0
        matrix = minor_to_matrix_3(matrix, separate_deter, deter)
        matrix = transposition(matrix)
    elif len(matrix) == 2:
        deter = determinant_order_2(matrix)
        if deter == 0:
            return 0
        matrix = [[matrix[1][1], -(matrix[0][1])], [-matrix[1][0], (matrix[0][0])]]
    else:
        matrix[0][0] = 1 / matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] % 1 == 0:
                matrix[i][j] = int(matrix[i][j])
            if abs(matrix[i][j]) > 100_000_000:
                matrix[i][j] = "{:.4e}".format(matrix[i][j])
            elif abs(matrix[i][j]) < 0.000001 and matrix[i][j] != 0:
                matrix[i][j] = "{:.3e}".format(matrix[i][j])
            else:
                matrix[i][j] = round(matrix[i][j], 5)
    answer = [matrix, len(matrix), len(matrix)]
    if deter != 1 and separate_deter:
        answer.append(deter)
    return answer


def transposition_event(matrix):
    matrix = transposition(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j], 5)
            if matrix[i][j] % 1 == 0:
                matrix[i][j] = int(matrix[i][j])
            if abs(matrix[i][j]) > 100_000_000:
                matrix[i][j] = "{:.4e}".format(matrix[i][j])
            elif abs(matrix[i][j]) < 0.000001 and matrix[i][j] != 0:
                matrix[i][j] = "{:.3e}".format(matrix[i][j])
    return matrix
