import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to a target [c, d] range.
    """
    # Your code here
    v=np.array(values,dtype=float)
    a=np.min(v)
    b=np.max(v)
    return np.round(c+(d-c)/(b-a)*(values-a),6)