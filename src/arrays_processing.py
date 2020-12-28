from typing import List, Optional
from math import fabs, floor, sqrt

# Автор: Андрей Семенцов
# Author: Andrew Sementsov


def get_average_in_array(array: List[float]):
    """
    Возвращает среднее арифметическое значений массива
    :param array: List[float]
    :return: float
    """
    return sum(array) / len(array)


def get_index_of_number_with_minimal_diff_from_average_in_array(array: List[float]):
    """
    Получение индекса элемента, у которого наименьшее отклонение от среднего арифметического значений массива
    :param array: List[float]
    :return: int
    """
    average_number = get_average_in_array(array)
    minimal_diff_from_average_value: Optional[float] = None
    minimal_diff_from_average_index = 0

    for index, value in enumerate(array):
        # Значение для сравнения. Разница между элементом массива и средним арифметическим значений массива.
        comparing_minimal_diff_from_average_value = fabs(value - average_number)

        if minimal_diff_from_average_value is None \
                or minimal_diff_from_average_value > comparing_minimal_diff_from_average_value:
            minimal_diff_from_average_value = comparing_minimal_diff_from_average_value  # Новая минимальная разница
            minimal_diff_from_average_index = index  # Индекс элемента с новой минимальной разницей

    return minimal_diff_from_average_index


def get_count_of_positive_items_in_array(array: List[float]):
    """
    Возвращает количество положительных элементов массива
    :param array: List[float]
    :return: int
    """
    positive_items_count = 0

    for item in array:
        if item > 0:
            positive_items_count += 1

    return positive_items_count


def get_positive_number_in_array(array: List[float], start: int = 0):
    """
    Возвращает первый положительный элемент массива начиная с индекса start
    :param array: List[float]
    :param start: int
    :return: float
    """
    array_length = len(array)

    # Начало поиска больше чем длина массива
    if start > array_length:
        raise ValueError

    for i in range(array_length - start):
        if array[start + i] > 0:
            return array[start + i]

    # В массиве нет положительных элементов, начиная с индекса start
    raise ValueError


def get_sum_between_first_and_second_positive_numbers_in_array(array: List[float]):
    """
    Возвращает сумму элементов массива между первым и вторым положительным числом
    :param array: List[float]
    :return: float
    """
    first_positive = get_positive_number_in_array(array, start=0)
    first_positive_index = array.index(first_positive)
    second_positive = get_positive_number_in_array(array, start=first_positive_index + 1)
    second_positive_index = array.index(second_positive)

    # Самый простой способ - использовать встроенные средства языка программирования
    # Но мы не пойдем этим путем
    # return sum(array[first_positive_index+1:second_positive_index])

    # Сумма нужных элементов
    sum_between_first_and_second_positive_numbers = 0.0

    # Сколько элементов между первым и вторым положительным числом
    items_length = second_positive_index - first_positive_index - 1
    for i in range(items_length):
        sum_between_first_and_second_positive_numbers += array[first_positive_index + i + 1]

    return sum_between_first_and_second_positive_numbers


def get_integer_part_of_float_number(number: float):
    """
    Возвращает целую часть числа с плавающей точкой
    :param number: float
    :return: int
    """
    return int(floor(number))


def is_integer_part_of_float_number_full_square(number: float):
    """
    Проверка является ли чосло полным квадратом
    Из целой части числа вычисляется корень,
    затем находится ближайшее целое число к этому корню, затем оно возводится в квадрат
    и сверяется с исходной целой частью числа. Если эта значения равны - число является полным корнем.
    :param number: float
    :return: bool
    """
    integer_part = get_integer_part_of_float_number(number)
    integer_part_sqrt = sqrt(integer_part)
    integer_part_sqrt_nearest_int = round(integer_part_sqrt)
    integer_part_sqrt_nearest_int_square = integer_part_sqrt_nearest_int * integer_part_sqrt_nearest_int
    return integer_part_sqrt_nearest_int_square == integer_part


def get_index_of_number_with_its_int_part_is_full_square_in_array(array: List[float], start: int = 0):
    """
    Возвращает индекс первого найденного элемента, целая часть которого является полным квадратом
    :param array: List[float]
    :param start: int
    :return: int
    """
    array_length = len(array)

    # Начало поиска больше чем длина массива
    if start > array_length:
        raise ValueError

    for i in range(array_length - start):
        if is_integer_part_of_float_number_full_square(array[start + i]) > 0:
            return start + i

    # В массиве нет элементов, у которых целая часть является полным квадратом, начиная с индекса start
    raise ValueError


def sort_only_numbers_with_their_int_part_is_full_square(array: List[float]):
    """
    Сортирует только те элементы массива, у которых целая часть является полным квадратом.
    Остальные элементы остаются на своих местах
    :param array: List[float]
    :return: None
    """
    # Не использовать дополнительные массивы ни для каких целей!

    try:
        last_full_square_of_int_part_index = get_index_of_number_with_its_int_part_is_full_square_in_array(array, start=0)
    except ValueError:
        # Нет ни одного подходящего элемента, сортировка не требуется
        return

    current_full_square_of_int_part_index = 0

    while True:
        try:
            # Поиск следующего элемента, у которого целая часть является полным квадратом,
            # начиная с индекса последнего найденного такого элемента
            current_full_square_of_int_part_index = \
                get_index_of_number_with_its_int_part_is_full_square_in_array(array, last_full_square_of_int_part_index + 1)

            # Если значение с бОльшим индексом меньше чем значение с меньшим индексом - нужно поменять значения
            # местами и повторить проверку всего массива с начала и делать так до тех пор, пока не будет отсортирован
            # весь массив
            if array[current_full_square_of_int_part_index] < array[last_full_square_of_int_part_index]:
                # Перестановка значений местами
                full_square_of_int_part_lesser_value = array[current_full_square_of_int_part_index]
                array[current_full_square_of_int_part_index] = array[last_full_square_of_int_part_index]
                array[last_full_square_of_int_part_index] = full_square_of_int_part_lesser_value

                # Сброс индексов для повторной проверки массива
                last_full_square_of_int_part_index = \
                    get_index_of_number_with_its_int_part_is_full_square_in_array(array, start=0)
                current_full_square_of_int_part_index = 0
            else:
                # Если значение с бОльшим индексом больше чем значение с меньшим индексом - нужно продолжить
                # проверку массива дальше
                last_full_square_of_int_part_index = current_full_square_of_int_part_index
        except ValueError:
            # Больше нет подходящих элементов, все нужные элементы уже отсортированы
            break


# НЕ ДЛЯ ЗАДАНИЯ ВАРИАНТА 7, ЭТО ДЛЯ ВАРИАНТА 8. ДОБАВЛЕНО ПО ОШИБКЕ
def get_max_element_modulo(array: List[float]):
    """
    Возвращает элемент с максимальным значением по модулю
    :param array: List[float]
    :return: float
    """
    max_item_modulo: Optional[float] = None

    for item in array:
        item_modulo = fabs(item)
        if max_item_modulo is None or max_item_modulo < item_modulo:
            max_item_modulo = item_modulo

    return max_item_modulo


# НЕ ДЛЯ ЗАДАНИЯ ВАРИАНТА 7, ЭТО ДЛЯ ВАРИАНТА 8. ДОБАВЛЕНО ПО ОШИБКЕ
def get_min_element_modulo(array: List[float]):
    """
    Возвращает элемент с минимальным значением по модулю
    :param array: List[float]
    :return: float
    """
    min_item_modulo: Optional[float] = None

    for item in array:
        item_modulo = fabs(item)
        if min_item_modulo is None or min_item_modulo > item_modulo:
            min_item_modulo = item_modulo

    return min_item_modulo


# НЕ ДЛЯ ЗАДАНИЯ ВАРИАНТА 7, ЭТО ДЛЯ ВАРИАНТА 8. ДОБАВЛЕНО ПО ОШИБКЕ
def get_product_of_numbers_between_min_and_max_by_modulo_in_array(array: List[float]):
    # Максимальный и минимальный по модулю элементы и их индексы
    max_element_modulo = get_max_element_modulo(array)
    min_element_modulo = get_min_element_modulo(array)
    index_of_max_element_modulo = array.index(max_element_modulo)
    index_of_min_element_modulo = array.index(min_element_modulo)

    # Определения "положения" максимального и минимального по модулю элементов в массиве
    start_index = min(index_of_max_element_modulo, index_of_min_element_modulo)
    end_index = max(index_of_max_element_modulo, index_of_min_element_modulo)

    # Количество элементов, которые нужно перемножить начиная со start_index
    needle_items_length = end_index - start_index

    product_of_needle_items = 1  # Произведение нужных элементов массива

    for i in range(needle_items_length):
        product_of_needle_items *= array[start_index + i]

    return product_of_needle_items


