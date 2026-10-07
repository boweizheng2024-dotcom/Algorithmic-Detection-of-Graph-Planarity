from ConnectedComponents import COMPREP, MERGE, FIND_COMPONENT
from Examples import Dodecahedron

def ASSIGNMENT(AdjList_G, partition, parents):
    if len(parents) == 0:
        return True
    else:       
        sons = []
        for u in parents:
            for w in AdjList_G[u-1]:
                if partition[w-1] == -1:
                    partition[w-1] = (-partition[u-1] + 3)
                    sons.append(w)
                elif partition[w-1] != (-partition[u-1] + 3):
                    return False      
        parents = sons
        
        return ASSIGNMENT(AdjList_G, partition, parents)

def TEST_BIPARTITE(AdjList_G):
    CompPtr = FIND_COMPONENT(AdjList_G)

    Representatives = []
    for i in range(1, len(AdjList_G)+1):
        if CompPtr[i] < 0:
            Representatives.append(i)

    partition = [-1] * len(AdjList_G)

    for v in Representatives:
        if partition[v-1] == -1:
            partition[v-1] = 1
            parents = [v]

            Result = ASSIGNMENT(AdjList_G, partition, parents)
            if Result == False:
                return False
    
    return True

# example
# AdjList_1 = [
#     [4,5,6],
#     [4,5,6],
#     [4,5,6],
#     [1,2,3,13],
#     [1,2,3],
#     [1,2,3],
#     [10,11,12,13],
#     [10,11,12],
#     [10,11,12],
#     [7,8,9],
#     [7,8,9],
#     [7,8,9],
#     [4,7]
# ]

# Dodecahedron = [[2,5,12],   # v1
#        [1,3,14],   # v2
#        [2,4,6],   # v3
#        [3,5,8],   # v4
#        [1,4,10],   # v5
#        [3,7,15],   # v6
#        [6,8,17],   # v7
#        [4,7,9],   # v8
#        [8,10,18],   # v9
#        [5,9,11],   # v10
#        [10,12,19],   # v11
#        [1,11,13],   # v12
#        [12,14,20],   # v13
#        [2,13,15],   # v14
#        [6,14,16],   # v15
#        [15,17,20],   # v16
#        [7,16,18],   # v17
#        [9,17,19],   # v18
#        [11,18,20],   # v19
#        [13,16,19]   # v20
# ]

# print(TEST_BIPARTITE(Dodecahedron))
