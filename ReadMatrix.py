def readMatrix(filename):
    matFile = open(filename, 'r')
    mat = []
    try:
        for line in matFile:
            newRow = line.split(',')
            for x in range(0, len(newRow)):
                newRow[x] = float(newRow[x])
            mat.append(newRow)
    except:
        mat = 0
    if isMatrix(mat):
        return mat
    else:
        return 0

def isMatrix(a):
    try:
        height = len(a)
        width = len(a[0])
#        print("Width: " + str(width))
#        print("Height: " + str(height))
        for row in range(0, height):
            if len(a[row]) != width:
                return False
        return True
    except:
        return False

def main():
    try:
        matrixA = readMatrix("matrixA.csv")
    except:
        print("Error: invalid file")
    
    if matrixA == 0:
        print("Error: invalid matrix")
    else:
        print("Matrix:")
        for row in range(0, len(matrixA)):
            print(matrixA[row])
    return

if __name__ == "__main__":
    main()
