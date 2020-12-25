from random import randint
from prompts import *
from array_filling import *
from arrays_processing import *
from matrix import *


# Автор: Андрей Семенцов
# Author: Andrew Sementsov


def input_matrix():
    matrix= []
    i = 0
    matrix_reversed_row_size = None
    print('Ввод матрицы. Вводите значения элементов строк через пробел. '
          '\nЧтобы прекратить ввод строк оставьте поле ввода пустым и нажмите enter')
    while True:
        input_str = input('Строка #' + str(i + 1) + ': ')

        if len(input_str) == 0:
            print('Ввод массива завершен')
            break

        matrix_row_str = input_str.split(' ')
        if matrix_reversed_row_size is None:
            matrix_reversed_row_size = len(matrix_row_str)

        matrix_row = []
        for item_str in matrix_row_str:
            try:
                item_number = int(item_str)
            except ValueError:
                print('Нужно ввести только целые числа! Попробуйте ввести снова')
                continue
            matrix_row.append(item_number)

        if len(matrix_row) != matrix_reversed_row_size:
            print('Неправильная длина строки. Попробуйте ввести снова')
        else:
            i += 1
            matrix.append(matrix_row)

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

    first_matrix = [
        [2, 0],
        [-1, -2],
        [3, -5]
    ]
    second_matrix = [
        [-2, 3],
        [4, -1]
    ]
    # first_matrix, second_matrix = second_matrix, first_matrix

    print('Даны две матрицы. Вычислите их произведение')
    print_matrix(first_matrix, second_matrix)
    print('')

    user_matrix = input_matrix()
    true_multiplied_matrix = multiply_matrices(first_matrix, second_matrix)
    print('Проверка ответа. Слева ответ пользователя, справа правильный ответ.')
    print_matrix(user_matrix, true_multiplied_matrix)
    is_matrices_equal = check_matrices_equality(user_matrix, true_multiplied_matrix)
    if is_matrices_equal:
        print('Правильно. Ответ верный!')
    else:
        print('Ответ не верный!')


if __name__ == '__main__':
    main()