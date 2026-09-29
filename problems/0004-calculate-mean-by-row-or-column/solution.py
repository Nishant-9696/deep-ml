import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix=np.asarray(matrix,dtype=float)
	if mode=="row":
		return np.mean(matrix, axis=1)

	if mode=="column":
		return np.mean(matrix, axis=0) 