import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.array(data,dtype=float)
    mean=np.mean(data)
    median=np.median(data)
    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)]
    variance=np.var(data)
    standard_deviation=np.std(data)
    percentile25=np.percentile(data,[25])
    percentile50=np.percentile(data,[50])
    percentile75=np.percentile(data,[75])
    interquartile_range=np.percentile(data,[75])-np.percentile(data,[25])
    return {'mean':mean,'median':median,'mode':mode,'variance':variance,'standard_deviation':standard_deviation,'25th_percentile': percentile25, '50th_percentile': percentile50, '75th_percentile': percentile75, 'interquartile_range':interquartile_range}