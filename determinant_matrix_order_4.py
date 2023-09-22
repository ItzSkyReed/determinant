print('Введите матрицу четвертого порядка, обязательно вводите по одной строке через пробел.')
any_matrix_order_4 = []
for m in range(0, 4):
    try:
        any_matrix_order_4.append(list(map(float, input().split(" "))))
        if len(any_matrix_order_4[m]) != 4:
            print("Количество введенных чисел не 4")
            exit()
    except ValueError:
        print("Неправильный ввод, возможно вы не ввели число или же ввели буквы.")
        exit()
    except Exception as ex:
        print(f'Случилась ошибка о которой я не подумал. {ex}')
        exit()


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
    return int(determinant) if determinant.is_integer() else determinant


print(f'Определитель данной матрицы равен: {determinant_order_4(any_matrix_order_4)}')