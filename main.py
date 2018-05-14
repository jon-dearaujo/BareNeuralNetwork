'''
  Some ludicrously stupid ways of use nn.NeuralNetwork. :D

  Using a 2x1 output to solve simple Boolean op.
  Yeah, it could be done with 1x1, but you know... LUDICROUSLY STUPID is the word here
'''

from nn import NeuralNetwork

def pretty_print(output):
  print(output)
  output = [round(x) for x in output]
  if output == [1, 0]:
    return True

  if output == [0, 1]:
    return False

nn = NeuralNetwork(2, 2, 2)

# start training for AND operation
for i in range(1000):
  nn.train([1, 1], [1, 0])
  nn.train([1, 0], [0, 1])
  nn.train([1, 1], [1, 0])
  nn.train([0, 1], [0, 1])
# end training
print('AND OPERATION')
print([1,0], ' => ', pretty_print(nn.feedforward([1,0])))
print([1,1], ' => ', pretty_print(nn.feedforward([1,1])))
print([0,1], ' => ', pretty_print(nn.feedforward([0,1])))


#start training for XOR operation
nn = NeuralNetwork(2, 2, 2)

for i in range(1000):
  nn.train([1, 1], [0, 1])
  nn.train([1, 0], [1, 0])
  nn.train([1, 1], [0, 1])
  nn.train([0, 1], [1, 0])
# end training

print('XOR OPERATION')
print([1,0], ' => ', pretty_print(nn.feedforward([1,0])))
print([1,1], ' => ', pretty_print(nn.feedforward([1,1])))
print([0,1], ' => ', pretty_print(nn.feedforward([0,1])))
