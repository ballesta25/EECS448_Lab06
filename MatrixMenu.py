import addMatrix
import checkMatrices
import multMatrix
import ReadMatrix
import transpose
import sys


def printMenu():
	print("\n1) Add matrices.")
	print("2) Multiply matrices.")
	print("3) Transpose matrix 1.")
	print("4) Transpose matrix 2.")
	print("5) Change matrix 1.")
	print("6) Change Matrix 2.")
	print("7) Exit.")


#Read in first matrix from matrixA
print("Matrix 1 set to 'matrixA.csv', matrix 2 set to 'matrixB.csv'")
try:
	m1 = ReadMatrix.readMatrix("matrixA.csv")
	if (not ReadMatrix.getDimensions(m1)):
		print("Error with 'matrixA.csv'. Defaulting to 2x2 Identity matrix.")
		m1 = [[1,0],[0,1]]
except:
	print("Error with 'matrixA.csv'. Defaulting to 2x2 Identity matrix.")
	m1 = [[1,0],[0,1]]
	
try:
	m2 = ReadMatrix.readMatrix("matrixB.csv")
	if (not ReadMatrix.getDimensions(m2)):
		print("Error with 'matrixB.csv'. Defaulting to 2x2 Identity matrix.")
		m2 = [[1,0],[0,1]]
except:
	print("Error with 'matrixB.csv'. Defaulting to 2x2 Identity matrix.")
	m12 = [[1,0],[0,1]]





#menu loop
while True:
	printMenu()
	num = int(raw_input(">"))
	if 1 == num:
		if checkMatrices.checkAdd(m1,m2):
			print("m1 + m2 = ", addMatrix.add(m1,m2))
		else:
			print("Mismatched dimensions. Cannot add.")
	elif 2 == num:
		if checkMatrices.checkMult(m1,m2):
			print(multMatrix.mult(m1,m2))
		else:
			print("Incorrect dimensions for multiplication.")
	elif 3 == num:
		print(transpose.transpose(m1))
	elif 4 == num:
		print(transpose.transpose(m2))
	elif 5 == num:
		try:
			inp1 = ReadMatrix.readMatrix(raw_input('Input file name: '))
			dim = ReadMatrix.getDimensions(inp1)
			if dim:
				m1 = inp1
				print("Matrix 1 set to ", m1)
			else: 
				print("Invalid matrix.")
		except:
			print("Input error.")
	elif 6 == num:
		try:
			inp2 = ReadMatrix.readMatrix(raw_input('Input file name: '))
			dim = ReadMatrix.getDimensions(inp2)
			if dim:
				m2 = inp2
				print("Matrix 2 set to ", m2)
			else: 
				print("Invalid matrix. Matrix 2 not changed.")
		except:
			print("Input error.")
	elif 7 == num:
		break
	
