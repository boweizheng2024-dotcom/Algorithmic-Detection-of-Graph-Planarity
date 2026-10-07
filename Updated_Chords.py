import numpy as np
from Examples import Dodecahedron

def FIND_CHORDS(AdjMatrix, m, V_C, B, Attachments):
    w = V_C[0]
    for i in range(2, len(V_C)-1):
        v = V_C[i]
        if AdjMatrix[w-1][v-1] == 1:
            m = m + 1
            B.append([str(w)+'-'+str(v)])
            Attachments.append([0, i])
     
    l = 2
    for j in range(1, len(V_C)-2):
        x = V_C[j]
        l = l + 1
        for k in range(l,len(V_C)):
            y = V_C[k]
            if AdjMatrix[x-1][y-1] == 1:
                m = m + 1
                B.append([str(x)+'-'+str(y)])
                Attachments.append([j, k])

    return m , B, Attachments



# AdjMatrix = np.array([
#     [0, 1, 1, 1, 0, 1],
#     [1, 0, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0, 0],
#     [1, 1, 1, 0, 1, 1],
#     [0, 1, 0, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0]
# ])
# m = 0
# V_C_ = [1,2,3,4,5,6]

# Tetrahedron = np.array([
#     [0, 1, 1, 1],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 0]
# ]) 
# m = 0
# V_C_ = [1,2,3,4]
# B = []
# Attachments = []

# print(FIND_CHORDS(Tetrahedron, m, V_C_, B, Attachments))