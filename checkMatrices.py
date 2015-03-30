# checkMatrices.py

from ReadMatrix import getDimensions

def checkAdd(A, B):
    dimA = getDimensions(A)
    dimB = getDimensions(B)
    if dimA and dimB:
        return dimA == dimB
    else:
        return False

def checkMult(A, B):
    dimA = getDimensions(A)
    dimB = getDimensions(B)
    if dimA and dimB:
        return dimA[1] == dimB[0]
    else:
       return False
