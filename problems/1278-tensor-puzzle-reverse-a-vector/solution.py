import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    
    for i in range(len(a) // 2):
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
    
    return a