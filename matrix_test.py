import unittest

from matrix import multiply_matrices

class MatrixMultiplicationTestCase(unittest.TestCase):

    def test_multiply_matrices(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        result = multiply_matrices(matrix1, matrix2)
        self.assertEqual(result, expected_result)

    def test_multiply_matrices_3x3(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        result = multiply_matrices(matrix1, matrix2)
        self.assertEqual(result, expected_result)

    def test_multiply_matrices_2x3(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        expected_result = [[58, 64], [139, 154]]
        result = multiply_matrices(matrix1, matrix2)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()
