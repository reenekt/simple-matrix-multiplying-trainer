from typing import List, Callable, Optional


def create_empty_array(length, fill_value=None):
    array = []
    for i in range(length):
        array.append(fill_value)
    return array


def get_max_in_array(array: List, comparison_function: Optional[Callable] = None):
    max_value = None
    for item in array:
        if not (comparison_function is None):
            max_value = comparison_function(max_value, item)
        else:
            if max_value is None:
                max_value = item
            else:
                max_value = max(max_value, item)
    return max_value
