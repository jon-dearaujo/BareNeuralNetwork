import random

class Matrix:
  def __init__(self, inner=None, rows=1, cols=1):
    if inner is None:
      self.rows = rows
      self.cols = cols
      self.matrix = []

      self.matrix = [[0.0 for y in range(self.cols)] 
      for x in range(self.rows)]
    else:
      self.rows = len(inner)
      self.cols = len(inner[0])
      self.matrix = inner

  def randomize(self):
    self.matrix = [[random.uniform(0, 100) for y in range(self.cols)] 
    for x in range(self.rows)]
  
  def __scalar_multiply(self, scalar):
    self.__perform_for_each(lambda x: x * scalar)
    
  def __scalar_add(self, val):
    self.__perform_for_each(lambda x: x + val)
  
  def add(self, other):
    if type(other) is list:
      if not (len(self.matrix) == len(other) \
        and len(self.matrix[0]) == len(other[0])):
        raise Exception('Invalid matrix dimensions')

      self.__perform_for_each_with_indexes(lambda val, row, col: val + other[row][col])
    else:
      self.__scalar_add(other)

  def multiply(self, other):
    print(type(other))
    if isinstance(other, Matrix):
      '''Matrix product'''
      if not (len(self.matrix[0]) == len(other.matrix)):
        raise Exception('Matrix A\'s column size must match Matrix B\'s row size')
      
      result_row = len(self.matrix)
      result_col = len(other.matrix[0])
      result = self.__gen_new_zeroed_inner(result_row, result_col)

      for i in range(result_row):
        for j in range(result_col):
          total = 0.0
          for move in range(len(other.matrix)):
            total += self.matrix[i][move] * other.matrix[move][j]
          result[i][j] = total
      return Matrix(result)

    else:
      '''Scalar product'''
      self.__scalar_multiply(other)

  def transpose(self):
    ''' [1, 2, 3] - [1, 4]
        [4, 5, 6] - [2, 5]
                    [3, 6]'''

    result = self.__gen_new_zeroed_inner(self.cols, self.rows)
    for i in range(self.rows):
      for j in range(self.cols):
        result[j][i] = self.matrix[i][j]
    self.matrix = result

  def __dot_product(self, vector_a, vector_b):
    sum = 0.0
    for move in range(len(vector_a)):
      sum += vector_a[move] * vector_b[move]
    return sum

  def __perform_for_each_with_indexes(self, func):
    self.matrix = [[func(val, row, col) for col, val in enumerate(self.matrix[row])] 
      for row in range(len(self.matrix))]

  def __perform_for_each(self, func):
    self.matrix = [
      [func(val) for val in row] 
      for row in self.matrix]

  def __gen_new_zeroed_inner(self, rows, cols):
    return [[0.0 for y in range(cols)] for x in range(rows)]

  def __repr__(self):
    return self.matrix.__repr__()
#End Matrix