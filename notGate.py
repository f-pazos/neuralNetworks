#Felipe Pazos
#05/17/2016
#A simple neural network to simulate binary negation.

import random
import math

def main():
	#Dictionary with input / outputs.
	examples = { 1:0, 0:1 }

	#Initialize weights.
	weights = [ 0,  0 ]

	#Run the learning alg 100 times.
	for t in range( 1000 ):
		if ( t % 10 ) == 0:
			print( "t: ", error( weights, examples ), weights)
		#x is randomly one of the inputs we know the output to. Calculate the z from the current neuron state.
		x = random.randint(0, 1)
		inputs = [1, x]

		z = f( inputs, weights )

		#Calculate the error by finding the difference to what we do know.
		err = error( weights, examples )

		delta = 1

		#Create an array to hold all the possible newWeights.
		newWeights = []

		for i in range( len(weights ) ):
			weights[i] += delta
			newWeights.append( weights[:] )
			weights[i] -= 2*delta
			newWeights.append( weights[:] )
			weights[i] += delta
		
		bestWeight = newWeights[0]
		bestError = error( bestWeight, examples )

		for newWeight in newWeights:
			newZ = f( inputs, newWeight )
			if error( newWeight, examples ) < bestError:
				bestWeight = newWeight
				bestError = error( bestWeight, examples)

		weights = bestWeight

	print( f([1, 1], weights ) )
	print( f([1, 0], weights ) )
	print( error( weights, examples ) )

def error( weights, exp ):
	inputs = list( exp.keys() )

	z1 = f( [1, inputs[0] ], weights )
	z2 = f( [1, inputs[1] ], weights )

	return .5 * ( z1 - exp[inputs[0]] )**2 + .5 * ( z2 - exp[inputs[1]])**2 

def f( x, weights ):
	dotProduct = 0
	for i in range( len( x ) ):
		dotProduct += x[i]*weights[i]

	z = 1 / ( 1 + math.exp( -dotProduct ) )

	return z


main()