import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    norm = np.sqrt(np.sum(x**2, axis=axis, keepdims=True) + eps)
    return (x / norm).tolist()
