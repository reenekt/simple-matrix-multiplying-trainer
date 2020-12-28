import unittest
from src.matrix import multiply_matrices


class MyTestCase(unittest.TestCase):
    def test_multiply_small_matrices(self):
        first_matrix = [
            [2, 0],
            [-1, -2],
            [3, -5]
        ]
        second_matrix = [
            [-2, 3],
            [4, -1]
        ]

        multiplied_matrices_expected_result = [
            [-4, 6],
            [-6, -1],
            [-26, 14],
        ]

        multiplied_matrices_actual_result = multiply_matrices(first_matrix, second_matrix)

        self.assertEqual(multiplied_matrices_expected_result, multiplied_matrices_actual_result)

    def test_multiply_small_matrices_swapped(self):
        first_matrix = [
            [2, 0],
            [-1, -2],
            [3, -5]
        ]
        second_matrix = [
            [-2, 3],
            [4, -1]
        ]

        multiplied_matrices_expected_result = [
            [-4, 6],
            [-6, -1],
            [-26, 14],
        ]

        # Swap matrices
        first_matrix, second_matrix = second_matrix, first_matrix

        multiplied_matrices_actual_result = multiply_matrices(first_matrix, second_matrix)

        self.assertEqual(multiplied_matrices_expected_result, multiplied_matrices_actual_result)

    def test_multiply_middle_matrices(self):
        first_matrix = [
            [37, 10, 53, -13],
            [-6, 11, -8, 10],
            [12, 66, 33, 19]
        ]
        second_matrix = [
            [60, 23, 33],
            [71, -8, -8],
            [30, 75, 14]
        ]

        multiplied_matrices_expected_result = [
            [2478, 3031, 4085, 77],
            [2579, 94, 3563, -1155],
            [828, 2049, 1452, 626],
        ]

        multiplied_matrices_actual_result = multiply_matrices(first_matrix, second_matrix)

        self.assertEqual(multiplied_matrices_expected_result, multiplied_matrices_actual_result)

    def test_multiply_middle_matrices_swapped(self):
        first_matrix = [
            [37, 10, 53, -13],
            [-6, 11, -8, 10],
            [12, 66, 33, 19]
        ]
        second_matrix = [
            [60, 23, 33],
            [71, -8, -8],
            [30, 75, 14]
        ]

        multiplied_matrices_expected_result = [
            [2478, 3031, 4085, 77],
            [2579, 94, 3563, -1155],
            [828, 2049, 1452, 626],
        ]

        # Swap matrices
        first_matrix, second_matrix = second_matrix, first_matrix

        multiplied_matrices_actual_result = multiply_matrices(first_matrix, second_matrix)

        self.assertEqual(multiplied_matrices_expected_result, multiplied_matrices_actual_result)


if __name__ == '__main__':
    unittest.main()
