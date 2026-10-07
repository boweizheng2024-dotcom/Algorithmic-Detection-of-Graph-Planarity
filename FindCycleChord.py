from Examples import Dodecahedron

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
    
# example
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
# print('cycle = ' + str(Find_a_Cycle_with_a_Chord(Dodecahedron)[0]))
# print('chord = ' + str(Find_a_Cycle_with_a_Chord(Dodecahedron)[1]))
# print(algorithm17(Dodecahedron))