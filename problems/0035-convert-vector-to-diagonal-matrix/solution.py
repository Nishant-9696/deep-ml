import numpy as np

def make_diagonal(x):
	l=len(x)
	shape=l,l
	matrix=np.zeros(shape)
	for i in range(l):
		matrix[i][i] = x[i]
	return matrix