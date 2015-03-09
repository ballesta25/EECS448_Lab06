#Matrix Transpose

def transpose(A):
    """transpose the input matrix (uses 2D array representation)"""
    return [[A[y][x] for y in range(len(A))] for x in range(len(A[0]))]
