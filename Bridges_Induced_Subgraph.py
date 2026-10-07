from ConnectedComponents import COMPREP
from Examples import Dodecahedron

def Finding_the_Bridges(AdjList_G, CompPtr):
    BRIDGE = [-1] * (len(CompPtr))
    BRIDGE[0] = 0
    m = 0
    B = []

    for u in range(1, len(CompPtr)):
        if CompPtr[u] < 0:
            m = m + 1
            BRIDGE[u] = m
            B.append([])

    for u in range(1, len(CompPtr)):
        if CompPtr[u] > 0:
            theBridge = BRIDGE[COMPREP(CompPtr, u)]
            BRIDGE[u] = theBridge
            for v in AdjList_G[u-1]:
                B[theBridge-1].append(str(u)+'-'+str(v))
                
        elif CompPtr[u] < 0:
            for v in AdjList_G[u-1]:
                B[BRIDGE[u]-1].append(str(u)+'-'+str(v))

    return(m, BRIDGE, B)



# example (inherits the example in Algorithm 6)
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
# CompPtr_1 = [0, 0, 0, 0, 0, 0, 0, -3, 7, 7]

# print('bridges = ' + str(Finding_the_Bridges(AdjList_1,CompPtr_1)[2]))