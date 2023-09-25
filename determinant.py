
def determinant_order_3(matrix, n):
    mat = []
    line = []
    for i in range(1, 4):
        for j in range(0, 4):
            if j != n:
                line.append(matrix[i][j])
        if line:
            mat.append(line)
        line = []
    return (mat[0][0] * mat[1][1] * mat[2][2]) + (mat[0][1] * mat[1][2] * mat[2][0]) + (
        mat[0][2] * mat[1][0] * mat[2][1]) - (mat[0][2] * mat[1][1] * mat[2][0]) - (
        mat[0][1] * mat[1][0] * mat[2][2]) - (mat[0][0] * mat[1][2] * mat[2][1])


def determinant_order_4(matrix):
    determinant = 0.0
    for i in range(4):
        determinant += ((-1) ** i) * matrix[0][i] * determinant_order_3(matrix, i)
    return f'Определитель равен: {int(determinant) if determinant.is_integer() else determinant}'