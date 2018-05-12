import random

class Matrix:
  def __init__(self, inner=None, rows=1, cols=1):
    if inner is None:
      self.rows = rows
      self.cols = cols
      self.data = []

      self.data = [[0.0 for y in range(self.cols)] 
      for x in range(self.rows)]
    else:
      self.rows = len(inner)
      self.cols = len(inner[0])
      self.data = inner

  @staticmethod
  def fromList(lst):
    return Matrix([[val] for val in lst])

  def toList(self):
    return [row[0] for row in self.data]

  def randomize(self):
    self.data = [[random.uniform(-1, 1) for y in range(self.cols)] 
    for x in range(self.rows)]
  
  def __scalar_multiply(self, scalar):
    self.__perform_for_each(lambda x: x * scalar)
    
  def __scalar_add(self, val):
    self.__perform_for_each(lambda x: x + val)
  
  def add(self, other):
    if isinstance(other, Matrix):
      if not (len(self.data) == len(other.data) \
        and len(self.data[0]) == len(other.data[0])):
        raise Exception('Invalid matrix dimensions')

      self.__perform_for_each_with_indexes(lambda val, row, col: val + other.data[row][col])
    else:
      self.__scalar_add(other)

  def multiply(self, other):
    if isinstance(other, Matrix):
      '''Matrix product'''
      if not (len(self.data[0]) == len(other.data)):
        raise Exception('Matrix A\'s column size must match Matrix B\'s row size')
      
      result_row = len(self.data)
      result_col = len(other.data[0])
      result = self.__gen_new_zeroed_inner(result_row, result_col)

      for i in range(result_row):
        for j in range(result_col):
          total = 0.0
          for move in range(len(other.data)):
            total += self.data[i][move] * other.data[move][j]
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
        result[j][i] = self.data[i][j]
    return Matrix(result)

  def map(self, function):
    self.data = [[function(value) for value in row] for row in self.data]

  def __dot_product(self, vector_a, vector_b):
    sum = 0.0
    for move in range(len(vector_a)):
      sum += vector_a[move] * vector_b[move]
    return sum

  def __perform_for_each_with_indexes(self, func):
    self.data = [[func(val, row, col) for col, val in enumerate(self.data[row])] 
      for row in range(len(self.data))]

  def __perform_for_each(self, func):
    self.data = [
      [func(val) for val in row] 
      for row in self.data]

  def __gen_new_zeroed_inner(self, rows, cols):
    return [[0.0 for y in range(cols)] for x in range(rows)]

  def __repr__(self):
    return self.data.__repr__()
#End Matrix