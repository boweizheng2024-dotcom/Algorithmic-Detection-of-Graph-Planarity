def TEST_INTERLEAVING(front, back, a, b):
    if abs(a-b) == 1:
        return False
    else:
        start = back[0]
        end = back[len(back)-1]
        m = int((a+b)/2)

        if front[m]>start and front[m]<end:
            return True
        elif front[m] >= end:
            return TEST_INTERLEAVING(front, back, a, m)
        else:
            return TEST_INTERLEAVING(front, back, m, b)
        

def TEST_EDGES(attB_q, attB_p):
    L = min(len(attB_q), len(attB_p))
    if L == 1:
        return False
    else:
        for i in range(min(L,4)):
            if attB_q[i] < attB_p[i]:
                if attB_q[len(attB_q)-1] <= attB_p[i]:
                    return False
                elif attB_q[len(attB_q)-1] > attB_p[i] and attB_q[len(attB_q)-1] < attB_p[len(attB_p)-1]:
                    return True
                else:
                    return TEST_INTERLEAVING(attB_q, attB_p, i, len(attB_q)-1)
            elif attB_q[i] > attB_p[i]:
                if attB_p[len(attB_p)-1] <= attB_q[i]:
                    return False
                elif attB_p[len(attB_p)-1] > attB_q[i] and attB_p[len(attB_p)-1] < attB_q[len(attB_q)-1]:
                    return True
                else:
                    return TEST_INTERLEAVING(attB_p, attB_q, i, len(attB_p)-1)
        
        if L == 2:
            return False
        else:
            return True


def CONSTRUCTION(Attachments):
    n = len(Attachments)
    AdjList_H = [[] for _ in range(n)]
 
    for i in range(len(Attachments)-1):
        for j in range(i+1, len(Attachments)):
            if TEST_EDGES(Attachments[i], Attachments[j]) == True:
                AdjList_H[i].append(j+1)
                AdjList_H[j].append(i+1)
    
    return AdjList_H

# example
# print(CONSTRUCTION([[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]))
# print('V_H = ' + str(CONSTRUCTION([[1,2], [1,2,3], [1,2,3,4], [1,2,3,4]])[0]))
# print('E_H = ' + str(CONSTRUCTION([[1,2], [1,2,3], [1,2,3,4], [1,2,3,4]])[1]))