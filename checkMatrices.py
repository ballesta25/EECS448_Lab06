# checkMatrices.py
from ReadMatrix import getDimensions

def checkAdd(A, B):
    dimA = getDimensions(A)
    dimB = getDimensions(B)
    if dimA and dimB:
        return dimA == dimB
    else:
        return false

def checkMult(A, B):
    dimA = getDimensions(A)
    dimB = getDimensions(B)
    if dimA and dimB:
        return dimA[0] == dimB[1] and dimA[1] == dimB[0]
    else:
       return false