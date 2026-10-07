from ConnectedComponents import COMPREP, MERGE

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
