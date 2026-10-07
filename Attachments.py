def Finding_Vertices_of_Attachment(AdjList_G, V_C, BRIDGE, m):
    Attachments = [[] for _ in range(m)]

    for i in range(len(V_C)):
        u = V_C[i]
        for v in AdjList_G[u-1]:
            if BRIDGE[v] > 0:
                a = BRIDGE[v]
                Attachments[a-1].append(i)
    
    return Attachments
