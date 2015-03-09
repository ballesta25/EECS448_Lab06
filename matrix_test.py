def isMat(a):
    try:
        height = len(a)
        width = len(a[0])
        print("Width: " + str(width))
        print("Height: " + str(height))
        for row in range(0, height):
            if len(a[row]) != width:
                return False
        return True
    except:
        return False

matA = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]

for row in range(0, len(matA)):
    print(matA[row])
print("Matrix? " + str(isMat(matA)))
