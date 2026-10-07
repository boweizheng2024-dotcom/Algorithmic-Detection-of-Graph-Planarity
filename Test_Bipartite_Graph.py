from ConnectedComponents import COMPREP, MERGE, FIND_COMPONENT

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
