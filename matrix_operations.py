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


def inverse_matrix(matrix):
    deter = 0
    if len(matrix[0]) == 4:
        deter = determinant_order_4(matrix)
        if deter == 0:
            return 0
    elif len(matrix[0]) == 3:
        deter = determinant_order_3(matrix)
        if deter == 0:
            return 0
        inverse_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
        for i in range(1,4):
            for j in range(1,4):
                inverse_matrix[i-1][j-1] = ((-1) ** (i + j + 1) * determinant_order_2(matrix_minor(matrix, i-1, j-1)))
        matrix = transposition(inverse_matrix)
    elif len(matrix[0]) == 2:
        deter = determinant_order_2(matrix)

        if deter == 0:
            return 0
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
    if deter != 1:
        answer.append(deter)
    return answer
