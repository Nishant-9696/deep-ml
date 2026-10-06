import numpy as np

def compute_null_space(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """
    Compute an orthonormal basis for the null space of A.

    Returns:
        Matrix of shape (n, k), where each column is a basis vector.
        If the null space is trivial, returns shape (n, 0).
    """

    A = np.asarray(A, dtype=float)

    # SVD
    U, S, Vt = np.linalg.svd(A, full_matrices=True)

    # Number of columns of A
    n = A.shape[1]

    # Rank = number of singular values greater than tolerance
    rank = np.sum(S > tol)

    # Null-space basis = last n-rank columns of V
    null_space = Vt[rank:n].T

    return null_space