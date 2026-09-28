import numpy as np

def diff(a: np.ndarray) -> np.ndarray:
    """out[0]=a[0]; out[i]=a[i]-a[i-1] for i>0."""

    r = []

    for i in range(len(a)):

        if i == 0:
            r.append(a[i])
        else:
            r.append(a[i] - a[i-1])

    return np.array(r, dtype=float)
