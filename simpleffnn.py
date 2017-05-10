from numpy import exp,array,random,dot

class NeuralNetwork():
	def __init__(self):
		#Seed the random number generator
		random.seed(1)

		#Model a single neuron, with 3 input connections and 1 output connection.
		#we assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
		#and mean 0
		self.synaptic_weights = 2 * random.random((3,1)) - 1

#Simple Feed Forward Neural Network
if __name__ = '__main__';
	#initialise a single neuron neural network
	neural_network = NeuralNetwork()

	print 'Random starting synaptic weights:'
	print neural_network.synaptic_weights

	#The train set. We have 4 examples, each consisting of 3 input values
	# and 1 output value
	training_set_inputs  = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
	training_set_outputs = array([[0,1,1,0]]).T

	#train the neural network using a training set.training
	#Do it 10,000 times and make small adjustments each time.
	neural_network.train(training_set_inputs,training_set_outputs,10000)

	print 'New synaptic weights after training: '
	print neural_network.synaptic_weights

	#Test the neural network with a new situation
	print 'Considering new situation [1,0,0] -> ?;'
	print neural_network