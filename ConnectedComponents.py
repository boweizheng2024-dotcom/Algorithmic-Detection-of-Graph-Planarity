def COMPREP(CompPtr,u):
    if CompPtr[u] < 0:
        return u
    else:
        theRep = COMPREP(CompPtr,CompPtr[u])
        CompPtr[u] = theRep
        return theRep


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
