from Examples import Dodecahedron

def COMPREP(CompPtr,u):
    if CompPtr[u] < 0:
        return u
    else:
        theRep = COMPREP(CompPtr,CompPtr[u])
        CompPtr[u] = theRep
        return theRep


# Since the first index of the list on computer is zero, we set an additional zero on the first entry of the list CompPtr.
# The purpose of doing this is to ensure that no extra zeros are introduced into CompPtr in the subsequent Algorithm 6.


# example:
# L = [0,-1,3,-6,3,2,7,3]
# print('the representative of vertex 6 is vertex ' + str(COMPREP(L, 6)))



def MERGE(CompPtr, uRep, vRep):
    uSize = - CompPtr[uRep]
    vSize = - CompPtr[vRep]
    if uSize < vSize:
        CompPtr[uRep] = vRep
        CompPtr[vRep] = - (uSize + vSize)
    else:
        CompPtr[vRep] = uRep
        CompPtr[uRep] = - (uSize + vSize)




def FIND_COMPONENT(AdjList):
    CompPtr = [-1] * (len(AdjList)+1)
    CompPtr[0] = 0

    for u in range(1, len(AdjList)+1):
        for v in AdjList[u-1]:
            uRep = COMPREP(CompPtr,u)
            vRep = COMPREP(CompPtr,v)
            if uRep != vRep:
                MERGE(CompPtr, uRep, vRep)
    
    return(CompPtr)


# example
# AdjList = [[], [3,5], [2,4], [3,6], [2], [4,7], [6]]

# print('CompPtr = '+ str(algorithm5(AdjList)))