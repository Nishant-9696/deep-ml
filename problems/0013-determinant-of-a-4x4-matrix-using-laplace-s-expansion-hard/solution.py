import numpy as np
def determinant_4x4(matrix: list[list[int|float]]) -> float:
	matrix=np.asarray(matrix,dtype=float)
	l=len(matrix)
	return np.linalg.det(matrix)