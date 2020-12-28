from typing import List
from random import randint
from src.arrays import *


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
    for i in range(y_size):
        matrix_row = []
        for j in range(x_size):
            matrix_item = randint(random_min, random_max)
            matrix_row.append(matrix_item)
        matrix.append(matrix_row)
    return matrix


def get_matrix_column(matrix: List[List[int]], column_index):
    """
    Возвращаем массив содержащий элементы колонки матрицы
    :param matrix: Матрица
    :param column_index: Индекс колонки
    :return: Колонка матрицы
    """
    column = []
    for row in matrix:
        column.append(row[column_index])
    return column


def print_matrix(*matrices: List[List[int]], space_size: int = 5):
    """
    Вывод матриц на экран. Может выводить несколько матрицв одну "строку"
    :param matrices: матрицы для вывода
    :param space_size: размер отступа между матрицами (количество пробелов)
    :return: None
    """
    matrices_output = []
    matrices_count = len(matrices)

    if matrices_count == 0:
        print('Не задана ни одна матрица для вывода!')
        return

    matrices_max_y_size = 0
    for i in range(matrices_count):
        matrices_max_y_size = max(matrices_max_y_size, len(matrices[i]))

    def matrix_column_items_comparison_function(a, b):
        if a is None:
            return len(str(b))
        return max(a, len(str(b)))

    for y in range(matrices_max_y_size):
        matrices_output_row = []

        # Берем каждую матрицу
        for matrix in matrices:
            matrix_rows_count = len(matrix)
            matrix_columns_count = len(matrix[0])

            # Получение ширины каждого столбца
            columns_width_values = create_empty_array(matrix_columns_count)
            for i in range(matrix_columns_count):
                column = get_matrix_column(matrix, i)
                columns_width_values[i] = get_max_in_array(column, matrix_column_items_comparison_function)

            # Данные для вывода
            if y > matrix_rows_count - 1:
                # заглушки
                for i in range(matrix_columns_count):
                    matrix_item_str = ''
                    # Заполнение столбца мастрицы (точнее - элемента этого ряда) до нужной ширины
                    max_width_of_column = columns_width_values[i]
                    if len(matrix_item_str) < max_width_of_column:
                        matrix_item_str_len_diff = max_width_of_column - len(matrix_item_str)
                        for _ in range(matrix_item_str_len_diff):
                            matrix_item_str += ' '

                    matrix_item_str += ' '  # дополнительный пробел
                    matrices_output_row.append(matrix_item_str)
            else:
                # Берем каждый элемент матрицы и добавляем в концчную матрицу для вывода
                matrix_row = matrix[y]
                for matrix_item in matrix_row:
                    matrix_item_str = str(matrix_item)

                    # Заполнение столбца мастрицы (точнее - элемента этого ряда) до нужной ширины
                    matrix_column_index = matrix_row.index(matrix_item)
                    max_width_of_column = columns_width_values[matrix_column_index]
                    if len(matrix_item_str) < max_width_of_column:
                        matrix_item_str_len_diff = max_width_of_column - len(matrix_item_str)
                        for _ in range(matrix_item_str_len_diff):
                            matrix_item_str += ' '

                    matrix_item_str += ' '  # дополнительный пробел
                    matrices_output_row.append(matrix_item_str)

            # после того, как были получены все элементы матрицы и если матрица
            # не последняя - добавляется отступ перед рядом следующей матрицей
            matrix_index = matrices.index(matrix)
            if matrix_index < matrices_count - 1:
                matrices_output_space_item = ''
                for _ in range(space_size):
                    matrices_output_space_item += ' '
                matrices_output_row.append(matrices_output_space_item)

        # Добавляем колонку к матрице для вывода
        matrices_output.append(matrices_output_row)

    # Отображение на экране
    if len(matrices_output) == 0 or len(matrices_output[0]) == 0:
        print('Нет данных для вывода!')
        return

    matrices_output_y_size = len(matrices_output)
    matrices_output_x_size = len(matrices_output[0])

    for y in range(matrices_output_y_size):
        for x in range(matrices_output_x_size):
            print(matrices_output[y][x], end='')
        print('')  # EOL


def create_empty_matrix(x_size, y_size, fill_value=None):
    """
    Создание новой пустой матрицы
    :param x_size: Количество столбцов
    :param y_size: Количество рядов
    :param fill_value: Значение для заполнения матрицы
    :return: Новая матрица
    """
    matrix = []
    for i in range(x_size):
        matrix_column = []
        for j in range(y_size):
            matrix_column.append(fill_value)
        matrix.append(matrix_column)
    return matrix


def multiply_matrices(first_matrix: List[List], second_matrix: List[List]):
    """
    Умножает две матрицы и возвращает их произведение.
    Если матрицы невозможно умножить (они не совместимы),
    то выбросится исключение ValueError
    :param first_matrix: Первая матрицы
    :param second_matrix: Вторая матрица
    :return: Произведение матриц (новая матрица)
    """
    first_matrix_rows_count = len(first_matrix)
    first_matrix_columns_count = len(first_matrix[0])
    second_matrix_rows_count = len(second_matrix)
    second_matrix_columns_count = len(second_matrix[0])

    m = 0  # число строк первой матрицы
    k = 0  # число столбцов первой матрицы / строк второй
    n = 0  # число столбцов второй матрицы

    if first_matrix_columns_count == second_matrix_rows_count:
        m = first_matrix_rows_count  # число строк первой матрицы
        k = first_matrix_columns_count  # число столбцов первой матрицы / строк второй
        n = second_matrix_columns_count  # число столбцов второй матрицы
    elif first_matrix_rows_count == second_matrix_columns_count:
        # матрицы совместимы. Для умножения они будут переставлены так,
        # чтобы количество столбцов первой матрицы было равно числу строк второй
        first_matrix, second_matrix = second_matrix, first_matrix

        # пересчет значений после перестановки матриц местами
        first_matrix_rows_count = len(first_matrix)
        first_matrix_columns_count = len(first_matrix[0])
        second_matrix_rows_count = len(second_matrix)
        second_matrix_columns_count = len(second_matrix[0])

        m = first_matrix_rows_count  # число строк первой матрицы
        k = first_matrix_columns_count  # число столбцов первой матрицы / строк второй
        n = second_matrix_columns_count  # число столбцов второй матрицы
    else:
        # Невозможно перемножить матрицы
        raise ValueError

    # Матрица-произведение нужного размера
    multiplied_matrix = create_empty_matrix(m, n)

    for i in range(m):
        for j in range(n):
            multiplied_matrix[i][j] = 0
            for f in range(k):
                # сложение произведений каждого элемента столбца первой матрицы на соответствующий элемент строки второй
                first_matrix_item = first_matrix[i][f]
                second_matrix_item = second_matrix[f][j]
                multiplied_matrix[i][j] += first_matrix_item * second_matrix_item
    return multiplied_matrix


def check_matrices_equality(first_matrix: List[List], second_matrix: List[List]):
    """
    Сравнивает матрицы и возвращает результат равны они или нет.
    :param first_matrix: Первая матрица
    :param second_matrix: Вторая матрица
    :return: Равны ли матрицы
    """
    first_matrix_rows_count = len(first_matrix)
    first_matrix_columns_count = len(first_matrix[0])
    second_matrix_rows_count = len(second_matrix)
    second_matrix_columns_count = len(second_matrix[0])

    # Если отличается размер матриц
    if first_matrix_rows_count != second_matrix_rows_count or first_matrix_columns_count != second_matrix_columns_count:
        return False

    # Если хоть один элемент первой матрицы отличается от соответствующего элемента второй, то матрицы не равны
    for y in range(first_matrix_rows_count):
        for x in range(first_matrix_columns_count):
            if first_matrix[y][x] != second_matrix[y][x]:
                return False

    # Все проверки пройдены, матрицы равны
    return True
