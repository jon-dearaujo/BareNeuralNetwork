from nn import NeuralNetwork

nn = NeuralNetwork(2, 2, 2)

input = [1, 0] #2 x 1

output = nn.feedforward(input)

print(output)