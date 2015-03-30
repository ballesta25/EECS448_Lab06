# multMatrix.py
import transpose

def dotProd(x, y):
    return reduce(lambda x, y: x + y, [x[i] * y[i] for i in range(len(x))], 0)


def mult(A, B):
    T = transpose.transpose(B)
    return [[dotProd(A[i], T[j]) for j in range(len(T))] for i in range(len(A))]
