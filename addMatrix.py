# Matrix addition


def add(A, B):
    """add two matrices (represented as 2D arrays)"""
    return [[A[x][y] + B[x][y] for y in range(len(A[x]))] for x in range(len(A))]
