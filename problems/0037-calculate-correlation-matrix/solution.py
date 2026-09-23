import numpy as np

def calculate_correlation_matrix(X: np.ndarray, Y: np.ndarray = None) -> np.ndarray:
    if Y is None:
        return np.corrcoef(X, rowvar=False)

    return np.corrcoef(X.T, Y.T)[:X.shape[1], X.shape[1]:]