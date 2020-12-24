from prompts import prompt_int
from random import randint, uniform

# Автор: Андрей Семенцов
# Author: Andrew Sementsov


def array_fill_manual(arr_length: int = 0):
    arr = []
    for i in range(arr_length):
        input_message = 'Введите значение элемента № ' + \
                        str(i) + ' массива [' + str(i + 1) + '/' + str(arr_length) + ']: '
        arr.append(prompt_int(input_message))
    return arr


def array_fill_random(arr_length: int = 0, min_value: int = -10, max_value: int = 100):
    arr = []
    for i in range(arr_length):
        arr.append(randint(min_value, max_value))
    return arr


def array_fill_from_file(arr_length: int = 0, file_path: str = None):
    if file_path is None:
        file_path = input('Введите название файла в папке программы или абсолютный путь до файла: ')

    arr = []

    # Открытие файла для чтения
    try:
        f = open(file_path)
    except FileNotFoundError as fnf_error:
        print('Файл не найден')
        raise fnf_error

    # Счетчик добавленных в массив элементов
    added_items = 0

    for line in f:
        try:
            # Считывание строки, приведение значения строки к типу int и добавление к массиву
            arr.append(float(line))
            added_items += 1

            # Прекращение заполнения массива когда массив заполнен до нужной длины
            if added_items >= arr_length:
                break
        except ValueError as error:
            # line[:-1] убирает символ переноса строки
            print('Значение', '"' + line[:-1] + '"', 'не является целым числом!')
            f.close()  # Закрытие потока в случае ошибки
            raise error

    # Закрытие потока после завершения считывания значений
    f.close()

    # Зполнение нулями незаполненный остаток массива
    left_empty_items_count = arr_length - added_items
    if left_empty_items_count > 0:
        for i in range(left_empty_items_count):
            arr.append(0)

    return arr
