import numpy as np

def matrixmul(a: list[list[int|float]],
              b: list[list[int|float]]) -> list[list[int|float]]:

    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    if a.shape[1] != b.shape[0]:
        return -1

    c = np.dot(a, b)

    return c.tolist()