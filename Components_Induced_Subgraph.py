from ConnectedComponents import COMPREP, MERGE
from Examples import Dodecahedron

def Finding_Components_of_Induced_Subgraph(AdjList_G, V_C):
    CompPtr = [-1] * (len(AdjList_G)+1)
    CompPtr[0] = 0
    for w in V_C:
        CompPtr[w] = 0

    for u in range(1, len(AdjList_G)+1):
        if CompPtr[u] != 0:
            for v in AdjList_G[u-1]:
                if CompPtr[v] != 0:
                    uRep = COMPREP(CompPtr,u)
                    vRep = COMPREP(CompPtr,v)
                    if uRep != vRep:
                        MERGE(CompPtr, uRep, vRep)
    
    return(CompPtr)


# example
# AdjList_1 = [
#     [2,6,7],
#     [1,3],
#     [2,4,9],
#     [3,5],
#     [4,6,8],
#     [1,5],
#     [1,8,9],
#     [5,7,9],
#     [3,7,8]
# ]
# V_C_1 = [1,2,3,4,5,6]

# AdjList_2 = [[2, 5, 12], #v1
#              [1, 3, 14], #v2
#              [2, 4, 6], #v3
#              [3, 5, 8], #v4
#              [1, 4, 10], #v5
#              [3, 7, 15], #v6
#              [6, 8, 17], #v7
#              [4, 7, 9], #v8
#              [8, 10, 18], #v9
#              [5, 9, 11], #v10
#              [10, 12, 18], #v11
#              [1, 11, 13], #v12
#              [12, 14, 16], #v13
#              [2, 13, 15], #v14
#              [6, 14, 16], #v15
#              [13, 15, 17], #v16
#              [7, 16, 18], #v17
#              [9, 11, 17], #v18
#              [], #v19
#              [] #v20
# ]
# V_C_2 = [16, 17, 18, 11, 12, 13, 14, 15]
# print('CompPtr = ' + str(Finding_Components_of_Induced_Subgraph(AdjList_1, V_C_1)))