import numpy as np 

#Create array
Z = np.zeros(10)

print "np.zeros(10):"
print Z

#Create 2d array of all zeros
Z2 = np.zeros((10,10))
print "np.zeros((10,10))"
print Z2

#Create 2d array of all ones
O2 = np.ones((10,10))
print "np.ones((10,10))"
print O2

#Create random 2D array of random values
R2 = np.random.random((10,10))
print "np.random.random((10,10))"
print R2

#Create Gaussian Number 2D array
G2 = np.random.randn(10,10)
print "np.random.randn(10,10):"
print G2

#Print mean of gaussian 2D array
print "Mean:     ",G2.mean()

#Print the variance of gaussian 2D array
print "Variance: ",G2.var()