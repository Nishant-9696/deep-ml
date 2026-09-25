import numpy as np

def compute_norm(arr, norm_type):
    arr = np.array(arr)

    if norm_type == 'l1':
        return float(np.sum(np.abs(arr)))

    elif norm_type == 'l2':
        return float(np.sqrt(np.sum(arr ** 2)))

    elif norm_type == 'linf':
        return float(np.max(np.abs(arr)))

    elif norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("Frobenius norm requires a 2D array")
        return float(np.sqrt(np.sum(arr ** 2)))

    else:
        raise ValueError("Invalid norm type")