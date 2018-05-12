import math

from matrix import Matrix

class NeuralNetwork():
  def __init__(self, number_inputs, number_hiddens, number_outputs):
    self.number_inputs = number_inputs 
    self.number_hiddens = number_hiddens
    self.number_outputs = number_outputs

    # nn = NeuralNetwork(2, 2, 1) inputs, hiddens, outsputs
    self.weights_ih = Matrix(rows=self.number_hiddens, cols=self.number_inputs)
    self.weights_ho = Matrix(rows=self.number_outputs, cols=self.number_hiddens)

    self.bias_h = Matrix(rows=self.number_hiddens, cols=1)
    self.bias_h.map(lambda x: 1.0)
    self.bias_o = Matrix(rows=self.number_outputs, cols=1)
    self.bias_o.map(lambda x: 1.0)

    # initialize the Weights with random values
    self.weights_ih.randomize()
    self.weights_ho.randomize()

  def feedforward(self, input):
    in_matrix = Matrix.fromList(input)
    hidden = self.weights_ih.multiply(in_matrix)
    hidden.add(self.bias_h)
    hidden.map(self.__activate)

    output = self.weights_ho.multiply(hidden)
    output.add(self.bias_o)
    output.map(self.__activate)

    return output.toList()

  def __activate(self, val):
    return 1.0 / (1 + math.exp(-val))
#end NeuralNetwork
