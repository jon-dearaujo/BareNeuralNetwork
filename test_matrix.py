import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
  def setUp(self):
    self.matrix = Matrix(rows=2, cols=3)
    self.matrix.matrix = [[1.0, 1.0, 1.0],[1.0, 1.0, 1.0]]

  def test_it_has_defined_size(self):
    self.assertEqual(self.matrix.rows, 2)
    self.assertEqual(self.matrix.cols, 3)

    self.assertEqual(len(self.matrix.matrix), 2)
    self.assertEqual(len(self.matrix.matrix[0]), 3)

  def test_new_with_given_matrix_should_work(self):
    new_inner = [[2.0,2.0,2.0], [2.0,2.0,2.0]]
    matrix = Matrix(inner=new_inner)

    self.assertEqual(len(new_inner), matrix.rows)
    self.assertEqual(len(new_inner[0]), matrix.cols)
    self.assertEqual(new_inner, matrix.matrix)

  def test_scalar_multiplication_works(self):
    expected_matrix = [[2.0,2.0,2.0], [2.0,2.0,2.0]]
    self.matrix.multiply(2)
    self.assertEqual(self.matrix.matrix, expected_matrix)
  
  def test_scalar_add_works(self):
    expected_matrix = [[5.0,5.0,5.0], [5.0,5.0,5.0]]
    self.matrix.add(4)
    self.assertEqual(self.matrix.matrix, expected_matrix)

  def test_add_only_accepts_same_size(self):
    other_matrix = [[5.0, 2.0]] #One row, two columns
    with self.assertRaises(Exception) as error:
      self.matrix.add(other_matrix)
    self.assertEqual("Invalid matrix dimensions", str(error.exception))

  def test_add_works(self):
    other_matrix = [[1.0, 2.0, 1.0],[1.0, 2.0, 1.0]]
    expected_matrix = [[2.0, 3.0, 2.0],[2.0, 3.0, 2.0]]
    self.matrix.add(other_matrix)
    self.assertEqual(self.matrix.matrix, expected_matrix)

  def test_multiply_only_accepts_col_number_matching_row_number(self):
    other = Matrix([[2.0,2.0,2.0], [2.0,2.0,2.0]])

    with self.assertRaises(Exception) as error:
      self.matrix.multiply(other)
    self.assertEqual('Matrix A\'s column size must match Matrix B\'s row size', \
      str(error.exception))

  def test_multiply_must_work(self):
    other = Matrix([[2.0,5.0], [2.0,2.0], [4.0, 2.0]])
    expected = [[8.0, 9.0], [8.0, 9.0]]

    new_matrix = self.matrix.multiply(other)
    self.assertEqual(new_matrix.matrix, expected)
  
  def test_randomize_should_generate_new_values(self):
    original = self.matrix.matrix

    self.matrix.randomize()

    self.assertNotEqual(original, self.matrix.matrix)

  def test_transpose_should_work(self):
    original = Matrix([[2.0,5.0], [2.0,2.0], [4.0, 2.0]])
    expected_inner = [[2.0,2.0, 4.0], [5.0, 2.0, 2.0]]

    original.transpose()
    self.assertEqual(original.matrix, expected_inner)

if __name__ == '__main__':
  unittest.main()