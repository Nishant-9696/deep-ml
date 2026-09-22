import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    """
    Calculate P50, P95, and P99 latency percentiles.
    
    Args:
        latencies: List of latency measurements
    
    Returns:
        Dictionary with keys 'P50', 'P95', 'P99' containing
        the respective percentile values rounded to 4 decimal places
    """
    l=np.asarray(latencies,dtype=float)
    if len(l) <= 0:
        return {'P50': 0.0, 'P95': 0.0, 'P99': 0.0}
    else:
        return {'P50': np.round(np.percentile(l,50),4),
         'P95': np.round(np.percentile(l,95),4), 'P99': np.round(np.percentile(l,99
        ),4)}


