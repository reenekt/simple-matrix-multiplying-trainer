from random import randint
from prompts import *
from array_filling import *
from arrays_processing import *
from matrix import *


# Автор: Андрей Семенцов
# Author: Andrew Sementsov


def input_matrix():
    matrix_reversed = []
    i = 0
    matrix_reversed_row_size = None
    print('Ввод матрицы. Вводите значения элементов строк через пробел. '
          '\nЧтобы прекратить ввод строк оставьте поле ввода пустым и нажмите enter')
    while True:
        input_str = input('Строка #' + str(i + 1) + ': ')

        if len(input_str) == 0:
            print('Ввод массива завершен')
            break

        matrix_row = input_str.split(' ')
        if matrix_reversed_row_size is None:
            matrix_reversed_row_size = len(matrix_row)

        if len(matrix_row) != matrix_reversed_row_size:
            print('Неправильная длина строки. Попробуйте ввести снова')
        else:
            i += 1
            matrix_reversed.append(matrix_row)

    matrix = []
    for i in range(len(matrix_reversed)):
        for j in range(len(matrix_reversed[0])):
            if len(matrix) - 1 < j:
                matrix.append([])
            # matrix[j][i] = matrix_reversed[i][j]
            matrix[j].append(matrix_reversed[i][j])

    return matrix


def main():
    min_matrix_x_size = 2
    min_matrix_y_size = 2
    max_matrix_x_size = 5
    max_matrix_y_size = 5

    # Размеры матриц
    m = randint(2, 4)
    k = randint(3, 4)  # число столбцов для одной и число строк для другой матрицы
    n = randint(2, 4)
    first_matrix = get_matrix_filled_with_random_int(m, k)
    second_matrix = get_matrix_filled_with_random_int(k, n)

    second_matrix = [[
    # first_matrix = [[
        2,
        -1,
        3
    ], [
        0,
        -2,
        -5
    ]]
    first_matrix = [[
    # second_matrix = [[
        -2,
        4
    ], [
        3,
        -1
    ]]

    print('Даны две матрицы. Вычислите их произведение')
    print_matrix(first_matrix, second_matrix)
    print('')

    user_matrix = input_matrix()
    true_multiplied_matrix = multiply_matrices(first_matrix, second_matrix)
    print('Проверка ответа. Слева ответ пользователя, справа правильный ответ.')
    print_matrix(user_matrix, true_multiplied_matrix)
    # todo check equality


if __name__ == '__main__':
    main()
