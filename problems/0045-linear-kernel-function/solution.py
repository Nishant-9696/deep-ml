import numpy as np

def kernel_function(x1, x2):
	sum=0
	for i in range(0,len(x1)):
		sum += x1[i]*x2[i]
	return sum
