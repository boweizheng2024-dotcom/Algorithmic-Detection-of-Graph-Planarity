import numpy as np
from Examples import Dodecahedron

def DELETING_DEGREE_ONE_AND_TWO(AdjMatrix,w):
    N_w = []
    for i in range(AdjMatrix.shape[0]):
        if AdjMatrix[i][w] == 1:
            N_w.append(i)
    
    if len(N_w) == 2:
        u = N_w[0]
        v = N_w[1]
        AdjMatrix[w][u] = 0
        AdjMatrix[u][w] = 0
        AdjMatrix[w][v] = 0
        AdjMatrix[v][w] = 0  
        AdjMatrix[u][v] = 1
        AdjMatrix[v][u] = 1
        DELETING_DEGREE_ONE_AND_TWO(AdjMatrix, u)
        DELETING_DEGREE_ONE_AND_TWO(AdjMatrix, v)
    elif len(N_w) == 1:
        y = N_w[0]
        AdjMatrix[y][w] = 0
        AdjMatrix[w][y] = 0
        DELETING_DEGREE_ONE_AND_TWO(AdjMatrix, y)

def FIND_THE_CORE(AdjMatrix):
    for x in range(AdjMatrix.shape[0]):
        DELETING_DEGREE_ONE_AND_TWO(AdjMatrix, x)

    return AdjMatrix