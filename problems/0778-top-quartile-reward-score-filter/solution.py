import numpy as np

def top_quartile_mask(scores: list) -> list:
    """
    Return a boolean list marking scores in the top quartile (>= 75th percentile).
    """
    scores=np.asarray(scores)
    result=[]
   
    if len(scores) <= 0:
        return result
    q=np.percentile(scores,75)
    for i in range(len(scores)):
        if q <= scores[i]:
            result.append(True)
        else:
            result.append(False)
    return result