import numpy as np

def is_linearly_independent(vectors):
    if len(vectors) == 0:
        return True

    A = np.array(vectors, dtype=float)

    rank = np.linalg.matrix_rank(A)

    return rank == len(vectors)