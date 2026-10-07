import numpy as np

def AdjList_to_AdjMatrix(AdjList):
    n = len(AdjList)
    AdjMatrix = np.zeros((n,n),dtype=int)
    for u in range(1,n+1):
        for v in AdjList[u-1]:
            AdjMatrix[u-1][v-1] = 1
            AdjMatrix[v-1][u-1] = 1

    return AdjMatrix


def AdjMatrix_to_AdjList(AdjMatrix):
    n = AdjMatrix.shape[0]
    AdjList = [[] for _ in range(n)]
    for u in range(1,n+1):
        for v in range(1,n+1):
            if AdjMatrix[u-1][v-1] == 1:
                AdjList[u-1].append(v)

    return AdjList
