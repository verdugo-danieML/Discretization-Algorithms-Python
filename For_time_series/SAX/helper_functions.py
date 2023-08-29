import numpy as np

def paa(ts : np.array, paa_size : int):
    ts_size = len(ts)
    if ts_size == paa_size:
        return ts
    else:
        if (ts_size % paa_size) == 0:
            ts_matrix = ts.reshape(-1, paa_size, order = 'F')
            col_means = np.mean(ts_matrix, axis = 0)
            return col_means

        else:
            res = np.zeros(paa_size)
            
            for i in range(ts_size * paa_size):
                idx = i // ts_size  # the spot
                pos = i // paa_size  # the col spot
                res[idx] += ts[pos]
            
            for i in range(paa_size):
                res[i] /= ts_size
                
            return res
            
            
