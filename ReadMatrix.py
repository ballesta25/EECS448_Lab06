import sys

def readMatrix(filename):
    matFile = open(filename, 'r')
    mat = []
    for line in matFile:
        newRow = line.split(',')
        for x in range(0, len(newRow)):
            if is_number(newRow[x]):            
                newRow[x] = float(newRow[x])
            else:
                newRow.remove(newRow[x])
        mat.append(newRow)
    return mat

def getDimensions(a):
    try:
        height = len(a)
        width = len(a[0])
#        print("Width: " + str(width))
#        print("Height: " + str(height))
        for row in range(0, height):
            if len(a[row]) != width:
                return False
        return (height, width)
    except:
        return False

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def main():
    if len(sys.argv) < 2:
        print("Error: no file name provided")
        return
    else:
        filename = sys.argv[1]
    try:
        matrixA = readMatrix(filename)
    except:
        print("Error: invalid file")
        return
    try:
        dim = getDimensions(matrixA)
        if dim:
            print("Dimensions:")
            print(str(getDimensions(matrixA)) + '\n')
            print("Matrix:")
            for row in range(0, len(matrixA)):
                print(matrixA[row])
        else:
            print("Error: invalid matrix")
    except:
        print("Error: invalid matrix")
    return

if __name__ == "__main__":
    main()
