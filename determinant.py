import prettytable
nl = '\n'

def return_matrix(matrix):
    pretty_matrix = prettytable.PrettyTable()
    for row in matrix:
        pretty_matrix.add_row(row)
    return f'Матрица введенная вами:\n{pretty_matrix.get_string(header=False, border=True, hrules=prettytable.NONE)}'


def determinant(matrix):
    if len(matrix[0]) == 4:
        deter = determinant_order_4(matrix)
    elif len(matrix[0]) == 3:
        deter = determinant_order_3(matrix)
    elif len(matrix[0]) == 2:
        deter = determinant_order_2(matrix)
    else:
        deter = matrix[0][0]
    return f'Определитель равен: {nl if deter > 10**10 else "" }{int(deter) if deter.is_integer() else deter}'


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
