import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	a=np.asarray(a,dtype=float)
	b=np.asarray(b,dtype=float)
	
	if a.shape[1] != b.shape[0]:
        return -1
	else:	
		return np.dot(a,b)
