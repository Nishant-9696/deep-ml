import numpy as np
import numpy as np
from itertools import combinations

def matrix_rank(A, tol=1e-10):
    m, n = A.shape

    for r in range(min(m, n), 0, -1):
        for rows in combinations(range(m), r):
            for cols in combinations(range(n), r):

                minor = A[np.ix_(rows, cols)]

                if abs(np.linalg.det(minor)) > tol:
                    return r

    return 0
