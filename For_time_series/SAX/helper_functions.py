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
                pos = i // paa_size # the col spot
                res[idx] += ts[pos]
            
            for i in range(0,paa_size):
                res[i] /= ts_size
                
            return res

def sax(ts_paa : np.array, alphabet_size : int):
    breakpoints = {3: [-0.43, 0.43], 4: [-0.67, 0, 0.67], 5: [-0.84, -0.25, 0.25, 0.84]}

    sax_symbols = []

    for value in ts_paa:
        for i, b in enumerate(breakpoints[alphabet_size]):
            if value < b: 
                sax_symbols.append(chr(97 + i)) 
                break
            elif value >= breakpoints[alphabet_size][-1]:
                sax_symbols.append(chr(97 + (alphabet_size - 1)))
                break
                
    
    return ''.join(sax_symbols) 

def sax_distance(ts1_SAX, ts2_SAX):
    ts1_letras = [i for i in ts1_SAX]
    ts2_letras = [i for i in ts2_SAX]

   
    dist = np.zeros(len(ts1_letras))
    for i,(ts1, ts2) in enumerate(zip(ts1_letras,ts2_letras)):
        if ((ts1 == 'a') and (ts2 == 'b')) or ((ts1 == 'b') and (ts2 == 'a')):
            dist[i] = 0
    
        elif ((ts1 == 'a') and (ts2 == 'a')) or ((ts1 == 'b') and (ts2 == 'b')):
            dist[i] = 0
    
        elif ((ts1 == 'c') and (ts2 == 'b')) or ((ts1 == 'c') and (ts2 == 'c')):
            dist[i] = 0
    
        elif ((ts1 == 'b') and (ts2 == 'c')):
            dist[i] = 0
    
        elif ((ts1 == 'c') and (ts2 == 'd')) or ((ts1 == 'd') and (ts2 == 'c')):
            dist[i] = 0
    
        elif ((ts1 == 'd') and (ts2 == 'd')):
            dist[i] = 0
    
        elif ((ts1 == 'c') and (ts2 == 'a')) or ((ts1 == 'a') and (ts2 == 'c')):
            dist[i] = 0.67
    
        elif ((ts1 == 'd') and (ts2 == 'b')) or ((ts1 == 'b') and (ts2 == 'd')):
            dist[i] = 0.67
    
        elif ((ts1 == 'd') and (ts2 == 'a')) or ((ts1 == 'a') and (ts2 == 'd')):
            dist[i] = 1.34

    return dist

def MINDIST(sax_dist, n, w):
    return np.sqrt(n/w)*np.sqrt(np.sum(sax_dist**2))
    
            
            
