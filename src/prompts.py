from typing import Dict, Any

# Автор: Андрей Семенцов
# Author: Andrew Sementsov


def question_with_options(
        message: str = 'Выберите опцию',
        options: Dict[str, Any] = None,
        try_again_message: str = 'Такой опции нет. Попробуйте еще раз',
        required: bool = True,
        quit_str: str = 'quit'
):
    """
    Выбор опции
    :param message: str Сообщение, выводимое на экран
    :param options: Dict[str, Any] Словарь опций
    :param try_again_message: str Сообщение, выводимое на экран если выбранной опции не существует
    :param required: bool Должно ли значение обязательно быть выбрано
    :param quit_str: str Пропуск выбора опции (только если required == False)
    :return: Any Значение выбранной опции
    """
    if options is None:
        options = {}

    while True:
        print(message)

        for key in options:
            print(key, '-', options[key])

        input_value = input('Выбор: ')

        if not required and not (quit_str is None) and input_value == quit_str:
            return None

        if input_value in options:
            return options[input_value]
        else:
            print(try_again_message)


def prompt_float(message="Введите число", error_message="Ошибка при вводе числа, попробуйте еще раз"):
    """
    Запрос на ввод числа типа float.
    Пока не будет введено число, ввод не прекратится
    :param message: str Сообщение, выводимое на экран
    :param error_message: str Сообщение, выводимое на экран в случае ошибки
    :return: float Число
    """
    while True:
        try:
            input_string = input(message)
            number = float(input_string)
            return number
        except ValueError:
            print(error_message)


def prompt_int(message="Введите число", error_message="Ошибка при вводе числа, попробуйте еще раз"):
    """
    Запрос на ввод числа типа int.
    Пока не будет введено число, ввод не прекратится
    :param message: str Сообщение, выводимое на экран
    :param error_message: str Сообщение, выводимое на экран в случае ошибки
    :return: int Число
    """
    while True:
        try:
            input_string = input(message)
            number = int(input_string)
            return number
        except ValueError:
            print(error_message)
