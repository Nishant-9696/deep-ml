import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	m=np.array(matrix)
	return np.linalg.eigvals(m)