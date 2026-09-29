import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a=np.asarray(a)
	if a.size != np.prod(new_shape):
		return []
	else:
	    r=np.reshape(a, new_shape)
		return r