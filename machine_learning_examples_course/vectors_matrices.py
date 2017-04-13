import numpy as np 

M = np.array([[1,2], [3,4]])
L = [[1,2],[3,4]]

print "L[0]:"
print L[0]

print "M[0]:"
print M[0]

print "M[0,0]"
print M[0,0]

print "Matrix:"
print "matrix = np.matrix([[1,2],[3,4]])"

matrix = np.matrix([[1,2],[3,4]])
print matrix

#Convert matrix into array
array = np.array(matrix)
print "array = np.array(matrix)"
print array

#Transpose array
print "Transpose of array:"
print array.T

