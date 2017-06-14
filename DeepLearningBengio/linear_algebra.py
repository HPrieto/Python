"""
    Chapter 2: Linear Algebra

    Widely used throughout science and engineering.
"""

"""
	2.1 Scalars, Vectors, Matrices and Tensors

	Scalars:
		- Single number
		- Scalars are written in italics
		- We give scalars lower-case variable names
		- When introduced, we specify what kind of number scalars are.

	Vectors:
		- A vector is an array of numbers
		- Numbers are arranged in order
		- Numbers can be identified using index
		- Vectors are given lower-case names with bold lettering
		- The elements of a vector are identified by writing its name in italic
			typeface, with a subscript.

	Matrices:
		- 2D Array of numbers
		- Each element is identified by two indices instead of one
		- Upper-case variable names with bold typeface
		- if m==height and n==width then A 'E' R^m*n
		- Matrices can be added together as long as they have the same shape

	Tensors:
		- An Array with more than two axes
		- An array of numbers arranged on a regular grid with a variable
			number of axes

	Transpose:
		- The mirror image of a matrix across a diagnol line called 'Main Diagonal'
		
	* The addition of matrix and a vector.
		- In other words, the vector is added to each row of the matrix.

	Broadcasting: The implicit copying of b to many locations
"""

"""
	2.2 Multiplying Matrices and Vectors

	* The 'matrix' product of matrices A and B is a third matrix C.
		- A must have the same number of columns as B has rows
		- if A is of shape m * n and B is of shape n * p, then
			C is of shape m * p.

	Element-wise Product or Hadamard product:
		- Standard product of two matrices that contains the product
			of the individual elements.
"""

"""
	2.3 Identity and Inverse Matrices

	Matrix Inversion:

	Identity Matrix:
		- A matrix that does not change any vector when we multiply
			that vector by that matrix.
"""

"""
	2.4 Linear Dependence and Span

	* In order for A^-1 to exist, the equation must have exactly one solution for 
		every value of b.

	* To analyze how many solutions the equation has, we can think of the columns
		of 'A' as specifying different directions we can travel from the 'origin'
		- Then determine how many ways there are of reaching b.

	'Origin': The point specified by the vector of all zeros

	Linear Combination: 
		- A combination of some set of vectors {v^(1),...,v^(i)} is given by 
			multiplying each vector v^(i) by a corresponding scalar coefficient
			and adding the results.

	* The 'SPAN' of a set of vectors is the set of all points obtainable
		by linear combination of the original vectors

	Column Space or 'Range of A':
		- Determing whether Ax=b has a solution thus amounts to testing
			whether b is in the span of the columns of A
"""





































