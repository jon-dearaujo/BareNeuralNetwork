import math

from matrix import Matrix

class NeuralNetwork():
  def __init__(self, number_inputs, number_hiddens, number_outputs):
    self.number_inputs = number_inputs 
    self.number_hiddens = number_hiddens
    self.number_outputs = number_outputs

    self.weights_ih = Matrix(rows=self.number_hiddens, cols=self.number_inputs)
    self.weights_ho = Matrix(rows=self.number_outputs, cols=self.number_hiddens)

    self.bias_h = Matrix(rows=self.number_hiddens, cols=1)
    self.bias_h.map(lambda x: 1.0)
    self.bias_o = Matrix(rows=self.number_outputs, cols=1)
    self.bias_o.map(lambda x: 1.0)

    self.learning_rate = 0.1

    # initialize the Weights with random values
    self.weights_ih.randomize()
    self.weights_ho.randomize()

  def feedforward(self, input):
    # Extracts the output array from the 3-tuple returned by self.__guess
    return self.__guess(input)[0]

  def __guess(self, input):
    in_matrix = Matrix.fromList(input)
    hidden = Matrix.product(self.weights_ih, in_matrix)
    hidden.add(self.bias_h)
    hidden.map(self.__activate)

    output = Matrix.product(self.weights_ho, hidden)
    output.add(self.bias_o)
    output.map(self.__activate)

    return (output.toList(), hidden, in_matrix)

  def train(self, inputs, target_label):
    guess_r = self.__guess(inputs) # (output as list, hidden, input matrix)
    guess = Matrix.fromList(guess_r[0])
    hidden = guess_r[1]
    input_matrix = guess_r[2]
    target_matrix = Matrix.fromList(target_label)
    
    # Calculate output errors
    output_errors = Matrix.subtract(target_matrix, guess)

    # Calculating gradients for Hidden -> output
    gradients_ho = Matrix(guess.data)
    gradients_ho.map(self.__activate_derivative)
    gradients_ho.multiply(output_errors)
    gradients_ho.multiply(self.learning_rate)
    
    # Calculating deltas
    weights_ho_deltas = Matrix.product(gradients_ho, Matrix.transpose(hidden))

    # Tweaking weights_ho with the calculated deltas
    self.weights_ho.add(weights_ho_deltas)
    # Tweaking hidden -> output bias with the gradients
    self.bias_o.add(gradients_ho)
    
    # Calculate hidden layer errors
    hidden_errors = Matrix.product(Matrix.transpose(self.weights_ho), output_errors)

    # Calculating gradients for Input -> Hidden
    gradients_ih = Matrix(hidden.data)
    gradients_ih.map(self.__activate_derivative)
    gradients_ih.multiply(hidden_errors)
    gradients_ih.multiply(self.learning_rate)

    # Calculating deltas
    weights_ih_deltas = Matrix.product(gradients_ih, Matrix.transpose(input_matrix))

    # Tweaking weights_ih with the calculated deltas
    self.weights_ih.add(weights_ih_deltas)
    # Twaeking input -> hidden bias with the gradients
    self.bias_h.add(gradients_ih)

  def __activate(self, val):
    # Activate uses Sigmoid function
    # https://en.wikipedia.org/wiki/Sigmoid_function
    return 1.0 / (1 + math.exp(-val))

  def __activate_derivative(self, active_val):
    return active_val * (1 - active_val)
#end NeuralNetwork
