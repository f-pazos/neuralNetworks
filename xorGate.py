#Felipe Pazos
#May 19, 2016
#XOR Gate using a neural network.

import math
from random import randint

def main():



	#	      x1  x2
	#         |\ /|
	# bias--> O   O
	#    |     \ /
	#    |-->   O
	#			|
	#			z
	#
	#
	#
	#

	#weights{fromLayer}{toNode}{fromNode} 


	#Create weights based on list of nodes per layer.
	layerStructure = [2, 2, 1] 
	weights = createWeights( layerStructure )

	for layer in weights:
		print( layer ) 
	input()


	#Training Examples
	examples = {(0,0): 0, (0,1): 1, (1,0): 1, (1,1): 0}

	for t in range( 100 ):
		#Forward propagation

		inputs = [ randint(0, 1), randint(0, 1), 1 ]

		#Iterate through the layers. l gives the index of the current layer.
		for l in range( len( layerStructure ) - 1):
			outputs = []
			print( inputs )
			#Iterate through all the nodes in the destination Layer.
			for nodeIndex in range( layerStructure[ l + 1 ] ):
				nodeWeights = weights[l][ nodeIndex ]

				print( nodeWeights )
				z = computeNeuron( nodeWeights, inputs ) 
				input( z )
				outputs.append( z )

			#Use the current outputs as the next inputs.
			inputs = outputs 

#Crate weight structure for network consisting of layers based on size of layers given in nodeStructure.
def createWeights( nodeStructure ):

	weights = []
	count = 0

	for l in range( len( nodeStructure ) - 1 ):
		#Create 'layers' of weights. Subtract 1 for the layer of inputs.
		weights.append( [] )
		#Weights connect to the nodes in the next layer.
		for b in range( nodeStructure[l+1] ):
			weights[l].append( [] )
			#The weights come from the current layer.
			for c in range( nodeStructure[l]):
				weights[l][b].append( count )
				count += 1
			#Append a bias weight.
			weights[l][b].append( count )
			count += 1

	return weights



#Compute the output of a neuron given certain weights and inputs.
def computeNeuron( weights, inputs ):

	#Weights -1 is the bias.
	dot = weights[-1]

	for i in range( len( inputs ) ):
		dot += weights[i] * inputs[i]


	z = 1 / ( 1 + math.exp( -dot ) )

	return z

main()