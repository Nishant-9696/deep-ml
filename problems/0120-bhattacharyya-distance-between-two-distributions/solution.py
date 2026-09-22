import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    p=np.asarray(p,dtype=float)
    q=np.asarray(q,dtype=float)
    if p.shape != q.shape:
        return 0.0
    else:
        return np.round(-np.log(np.sum(np.sqrt(p*q))),4)