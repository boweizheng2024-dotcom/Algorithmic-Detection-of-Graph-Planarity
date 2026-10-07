from ConnectedComponents import COMPREP

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
