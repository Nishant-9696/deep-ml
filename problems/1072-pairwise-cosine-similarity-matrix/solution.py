import numpy as np

def pairwise_cosine_similarity(X):
    x=np.asarray(X,dtype=float)
    s=[]
    n=len(x)
    norms=np.linalg.norm(x,axis=1)
    for i in range(n):
        row=[]
        for j in range(n):
            if norms[i]==0 or norms[j]==0:
                sim=0.0
            else:
                dot=np.dot(x[i],x[j])
                sim=dot/(norms[i]*norms[j])
            row.append(float(round(sim, 4)))
        s.append(row)
    return s
                
