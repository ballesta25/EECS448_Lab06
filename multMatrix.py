# multMatrix.py
import transpose

def dotProd(x, y):
    return [x[i] * y[i] for i in range(len(x))]


def mult(A, B):
    T = transpose.transpose(B)
    return [[reduce(lambda x, y: x + y, dotProd(A[i], T[j]), 0) for j in range(len(T))] for i in range(len(A))]
