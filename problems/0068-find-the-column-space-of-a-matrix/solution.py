
import numpy as np

def matrix_image(A):
	result=[]
	rank=np.linalg.matrix_rank(A)
	for i in range(len(A[0])):
		row=[]
		for j in range(rank):
			row.append(A[i][j])
		result.append(row)
	return result

