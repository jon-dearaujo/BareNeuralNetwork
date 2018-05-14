'''
  Some ludicrously stupid ways of use nn.NeuralNetwork. :D
  LUDICROUSLY STUPID is the word here
'''
import random

from nn import NeuralNetwork

def pretty_print(output):
  print(output)
  output = [round(x) for x in output]
  if output == [1, 0]:
    return True

  if output == [0, 1]:
    return False

nn = NeuralNetwork(2, 1, 2)

# start training for AND operation
for i in range(1000):
  nn.train([1, 1], [1, 0])
  nn.train([1, 0], [0, 1])
  nn.train([0, 0], [0, 1])
  nn.train([0, 1], [0, 1])
# end training
print('AND OPERATION')
print([1,0], ' => ', pretty_print(nn.feedforward([1,0])))
print([1,1], ' => ', pretty_print(nn.feedforward([1,1])))
print([0,1], ' => ', pretty_print(nn.feedforward([0,1])))
print([0,0], ' => ', pretty_print(nn.feedforward([0,0])))


#start training for XOR operation
nn = NeuralNetwork(2, 2, 1)
training_data = [
  {'i': [1, 1], 'o': [0]},
  {'i': [1, 0], 'o': [1]},
  {'i': [0, 0], 'o': [0]},
  {'i': [0, 1], 'o': [1]},
]
for i in range(50000):
  data = training_data[random.randint(0, 3)]
  nn.train(data['i'], data['o'])
# end training

print('\nXOR OPERATION')
print([1,0], ' => ', round(nn.feedforward([1,0])[0]))
print([1,1], ' => ', round(nn.feedforward([1,1])[0]))
print([0,1], ' => ', round(nn.feedforward([0,1])[0]))
print([0,0], ' => ', round(nn.feedforward([0,0])[0]))
