def isMat(a):
    try:
        height = len(a)
        print("Height: " + str(height))
        width = len(a[0])
        print("Width: " + str(width))
        for row in range(0,height):
            if len(a[row]) != width:
                return False
        return True
    except:
        return False

matA = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]

print("Matrix? " + str(isMat(matA)))
