import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
  def setUp(self):
    self.matrix = Matrix(rows=2, cols=3)
    self.matrix.data = [[1.0, 1.0, 1.0],[1.0, 1.0, 1.0]]

  def test_it_has_defined_size(self):
    self.assertEqual(self.matrix.rows, 2)
    self.assertEqual(self.matrix.cols, 3)

    self.assertEqual(len(self.matrix.data), 2)
    self.assertEqual(len(self.matrix.data[0]), 3)

  def test_new_with_given_matrix_should_work(self):
    new_inner = [[2.0,2.0,2.0], [2.0,2.0,2.0]]
    matrix = Matrix(inner=new_inner)

    self.assertEqual(len(new_inner), matrix.rows)
    self.assertEqual(len(new_inner[0]), matrix.cols)
    self.assertEqual(new_inner, matrix.data)

  def test_scalar_multiplication_works(self):
    expected_matrix = [[2.0,2.0,2.0], [2.0,2.0,2.0]]
    self.matrix.multiply(2)
    self.assertEqual(self.matrix.data, expected_matrix)
  
  def test_scalar_add_works(self):
    expected_matrix = [[5.0,5.0,5.0], [5.0,5.0,5.0]]
    self.matrix.add(4)
    self.assertEqual(self.matrix.data, expected_matrix)

  def test_add_only_accepts_same_size(self):
    other_matrix = Matrix([[5.0, 2.0]]) #One row, two columns
    with self.assertRaises(Exception) as error:
      self.matrix.add(other_matrix)
    self.assertEqual("Invalid matrix dimensions", str(error.exception))

  def test_add_works(self):
    other_matrix = Matrix([[1.0, 2.0, 1.0],[1.0, 2.0, 1.0]])
    expected_matrix = [[2.0, 3.0, 2.0],[2.0, 3.0, 2.0]]
    self.matrix.add(other_matrix)
    self.assertEqual(self.matrix.data, expected_matrix)

  def test_product_only_accepts_col_number_matching_row_number(self):
    other = Matrix([[2.0,2.0,2.0], [2.0,2.0,2.0]])

    with self.assertRaises(Exception) as error:
      Matrix.product(self.matrix, other)
    self.assertEqual('Matrix A\'s column size must match Matrix B\'s row size', \
      str(error.exception))

  def test_product_must_work(self):
    other = Matrix([[2.0,5.0], [2.0,2.0], [4.0, 2.0]])
    expected = [[8.0, 9.0], [8.0, 9.0]]

    new_matrix = Matrix.product(self.matrix, other)
    self.assertEqual(new_matrix.data, expected)

  def test_multiply_must_work(self):
    other = Matrix([[2.0, 5.0, 10.0], [3.0, 1.0, 7.0]])
    expected = [[2.0, 5.0, 10.0], [3.0, 1.0, 7.0]]

    self.matrix.multiply(other)

    self.assertEqual(expected, self.matrix.data)
  
  def test_randomize_should_generate_new_values(self):
    original = self.matrix.data

    self.matrix.randomize()

    self.assertNotEqual(original, self.matrix.data)

  def test_transpose_should_work(self):
    original = Matrix([[2.0,5.0], [2.0,2.0], [4.0, 2.0]])
    expected_new = [[2.0,2.0, 4.0], [5.0, 2.0, 2.0]]

    new = Matrix.transpose(original)
    self.assertEqual(new.data, expected_new)

  def test_map_should_be_applied_to_all_elements(self):
    self.matrix.map(lambda x: 100.0)
    self.assertTrue([[self.assertEqual(100.0, val) for val in row] for row in self.matrix.data])

  def test_subtract_works(self):
    a = Matrix([[5, 15], [6, 10]])
    b = Matrix([[2, 5], [3, 1]])
    expected = Matrix([[3, 10], [3, 9]])

    self.assertEqual(Matrix.subtract(a, b).data, expected.data)

if __name__ == '__main__':
  unittest.main()