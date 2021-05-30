from random import randint
from prompts import *
from array_filling import *
from arrays_processing import *
from matrix import *


# Автор: Андрей Семенцов
# Author: Andrew Sementsov


def input_matrix():
    """
    Запрашивает ввод митрицы
    :return: Матрица с введенными значениями
    """
    matrix = []
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


def run_question():
    """
    Задает пользователю задачу (вопрос) на умножение матриц.
    :return: Является ли ответ пользователя верным
    """

    # Размеры матриц
    m = randint(2, 4)
    k = randint(3, 4)  # число столбцов для одной и число строк для другой матрицы
    n = randint(2, 4)
    m = 2
    k = 3
    n = 2
    first_matrix = get_matrix_filled_with_random_int(m, k)
    second_matrix = get_matrix_filled_with_random_int(k, n)

    # только для тестов
    # first_matrix = [
    #     [2, 0],
    #     [-1, -2],
    #     [3, -5]
    # ]
    # second_matrix = [
    #     [-2, 3],
    #     [4, -1]
    # ]
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

    return is_matrices_equal


def main():
    """
    Основная функция программы
    """
    questions_count = 0
    questions_with_true_answers_count = 0

    while True:
        # Подсчет результатов
        result = run_question()
        questions_count += 1
        if result:
            questions_with_true_answers_count += 1

        # список слов для завершения
        exit_words = 'q', 'Q', 'quit', 'Quit', 'Выход', 'Выйти', 'выход', 'выйти'

        print('\nЧтобы решить еще одну задачу умножения матриц нажмите Enter.'
              '\nЧтобы выйти из программы введите '
              '\n' + '/'.join(map(lambda s: '"' + s + '"', exit_words)) +
              '\nи затем нажмите Enter')
        user_input = input()

        if user_input in exit_words:
            questions_with_wrong_answers_count = questions_count - questions_with_true_answers_count
            questions_with_true_answers_percent = str(questions_with_true_answers_count / questions_count * 100)
            questions_with_true_answers_percent_str_dot_index = questions_with_true_answers_percent.index('.')
            questions_with_true_answers_percent = \
                questions_with_true_answers_percent[:questions_with_true_answers_percent_str_dot_index + 3]
            print('Завершение работы программы')
            print('Общий результат:')
            print('\tВсего вопросов: ', questions_count)
            print('\tПравильных ответов: ', questions_with_true_answers_count)
            print('\tНеправильных ответов: ', questions_with_wrong_answers_count)
            print('\t% правильных ответов: ', questions_with_true_answers_percent)
            print('')

            # пауза перед закрытием окна дял возможности просмотра результатов
            print('Нажмите любую клавишу для закрытия окна')
            input()
            break


if __name__ == '__main__':
    main()
