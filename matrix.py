from typing import List
from random import randint


def get_matrix_filled_with_random_int(x_size: int, y_size: int, random_min: int = -20, random_max: int = 80):
    """
    Создает матрицу заданного размера заполненную случайными целыми числами
    :param x_size: int
    :param y_size: int
    :param random_min: int
    :param random_max: int
    :return: Новая заполненная матрица
    """
    matrix = []
    for i in range(x_size):
        matrix_column = []
        for j in range(y_size):
            matrix_item = randint(random_min, random_max)
            matrix_column.append(matrix_item)
        matrix.append(matrix_column)
    return matrix


def print_matrix(*matrices: List[List[int]], space_size: int = 5):
    """
    Вывод матриц на экран. Может выводить несколько матрицв одну "строку"
    :param matrices:
    :param space_size:
    :return:
    """
    matrices_output = []
    matrices_count = len(matrices)

    if matrices_count == 0:
        print('Не задана ни одна матрица для вывода!')
        return

    matrices_max_y_size = 0
    for i in range(matrices_count):
        matrices_max_y_size = max(matrices_max_y_size, len(matrices[i][0]))

    # Берем каждую матрицу
    for matrix in matrices:
        # Берем каждую ее колонку
        for matrix_column in matrix:
            matrices_output_column = []
            max_width_of_column = 1

            # Поиск самого длинного числа
            for matrix_item in matrix_column:
                max_width_of_column = max(max_width_of_column, len(str(matrix_item)))

            # Берем каждый элемент матрицы и добавляем в концчную матрицу для вывода
            for matrix_item in matrix_column:
                matrix_item_str = str(matrix_item)
                if len(matrix_item_str) < max_width_of_column:
                    matrix_item_str_len_diff = max_width_of_column - len(matrix_item_str)
                    for _ in range(matrix_item_str_len_diff):
                        matrix_item_str += ' '
                matrix_item_str += ' '  # дополнительный пробел
                matrices_output_column.append(matrix_item_str)

            # Заполняем колонку для матрицы для вывода до максимального размера
            if len(matrices_output_column) < matrices_max_y_size:
                size_diff = matrices_max_y_size - len(matrices_output_column)
                for i in range(size_diff):
                    # matrices_output_column.append(' ')
                    placeholder_str = ' '
                    for _ in range(max_width_of_column):
                        placeholder_str += ' '
                    matrices_output_column.append(placeholder_str)

            # Добавляем колонку к матрице для вывода
            matrices_output.append(matrices_output_column)

        # Колонки-разделители для матрицы для вывода вставляются между "матрицами"
        if matrices.index(matrix) < matrices_count:
            for i in range(space_size):
                matrices_output_space_column = []
                for j in range(matrices_max_y_size):
                    matrices_output_space_column.append(' ')
                matrices_output.append(matrices_output_space_column)

    if len(matrices_output) == 0 or len(matrices_output[0]) == 0:
        print('Нет данных для вывода!')
        return

    matrices_output_x_size = len(matrices_output)
    matrices_output_y_size = len(matrices_output[0])

    for y in range(matrices_output_y_size):
        for x in range(matrices_output_x_size):
            print(matrices_output[x][y], end='')
        print('')  # EOL


def create_empty_matrix(x_size, y_size, fill_value=None):
    matrix = []
    for i in range(x_size):
        matrix_column = []
        for j in range(y_size):
            matrix_column.append(fill_value)
        matrix.append(matrix_column)
    return matrix


def multiply_matrices(first_matrix, second_matrix):
    first_matrix_columns_count = len(first_matrix)
    first_matrix_rows_count = len(first_matrix[0])
    second_matrix_columns_count = len(second_matrix)
    second_matrix_rows_count = len(second_matrix[0])

    m = first_matrix_rows_count  # число строк первой матрицы
    k = first_matrix_columns_count  # число столбцов первой матрицы / строк второй
    n = second_matrix_columns_count  # число столбцов второй матрицы

    # todo оправить условие и починить после цикл (см https://vscode.ru/prog-lessons/algoritm-umnozheniya-matrits.html )
    if second_matrix_columns_count == first_matrix_rows_count:
        # Обновление значений
        m = second_matrix_rows_count  # число строк второй матрицы
        k = first_matrix_rows_count  # число столбцов второй матрицы / строк первой
        n = first_matrix_columns_count  # число столбцов первой матрицы

        # все ок, но для работы нужно поменять матрицы местами
        # temp_matrix = first_matrix
        # second_matrix = first_matrix
        # first_matrix = temp_matrix
        first_matrix, second_matrix = second_matrix, first_matrix
    elif first_matrix_columns_count != second_matrix_rows_count:
        # Невозможно перемножить матрицы
        raise ValueError

    multiplied_matrix = create_empty_matrix(n, m)

    # for i in range(m):
    #     for j in range(n):
    for i in range(n):
        for j in range(m):
            # for i in range(n):
            #     for j in range(m):
            multiplied_matrix[i][j] = 0
            for f in range(k):
                # сложение произведений каждого элемента столбца первой матрицы на соответствующий элемент строки второй
                # multiplied_matrix[i][j] += first_matrix[i][f] * second_matrix[f][j]

                # multiplied_matrix[i][j] += \
                #     first_matrix[f][j] * \
                #     second_matrix[i][f]

                # first_matrix_item = first_matrix[i][f]
                # second_matrix_item = second_matrix[f][j]
                first_matrix_item = first_matrix[f][i]
                second_matrix_item = second_matrix[j][f]

                multiplied_matrix[i][j] += first_matrix_item * second_matrix_item
    return multiplied_matrix


