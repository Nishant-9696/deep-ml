import numpy as np

def disorder(apples: list) -> float:
    """
    Compute the disorder in a basket of apples.
    """
    a = np.array(apples)

    _, counts = np.unique(a, return_counts=True)

    p = counts / len(a)

    return -np.sum(p * np.log2(p))