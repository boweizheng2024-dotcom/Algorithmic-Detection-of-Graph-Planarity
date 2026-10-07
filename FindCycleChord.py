def Find_a_Cycle_with_a_Chord(AdjList):
    n = len(AdjList)
    visited = [False] * n
    parent = [-1] * n
    cycle = []
        
    def FIND_CYCLE_CHORD(v, p):
        visited[v-1] = True
        for u in AdjList[v-1]:
            if visited[u-1] == False:
                parent[u-1] = v
                return FIND_CYCLE_CHORD(u,v)
        
        i = 0
        L = []
        while len(L) < 2:
            if AdjList[v-1][i] != p:
                L.append(AdjList[v-1][i])
            i = i+1
        u_i = L[0]
        u_j = L[1]

        u_m = v
        while v != u_i and v != u_j:
            cycle.append(v)
            v = parent[v-1]
        
        cycle.append(v)
        chord = str(v) + '-' + str(u_m)

        x = parent[v-1]
        if x == u_i or x == u_j:
            cycle.append(x)
        else:
            while x != u_i and x != u_j:
                cycle.append(x)
                x = parent[x-1]

            cycle.append(x)

        return cycle, chord, v, u_m
    
    for w in range(1, n+1):
        if len(AdjList[w-1]) != 0:
            return FIND_CYCLE_CHORD(w,-1)
