#import libraries
import numpy as np
#Dot products
#Multiplication of vectors
a = np.array([1,2])
b = np.array([2,1])
dot = 0
for e, f in zip(a,b):
	dot += e*f
print "dot += e*f:"
print dot

print "a*b"
print a*b

print "np.sum(a*b)"
print np.sum(a*b)

print "(a*b).sum()"
print (a*b).sum()

print "np.dot(a,b)"
print np.dot(a,b)

print "a.dot(b)"
print a.dot(b)

print "b.dot(a)"
print b.dot(a)

#magnitude
print "np.sqrt((a*a).sum())"
amag = np.sqrt((a*a).sum())
print amag

print "np.linalg.norm(a)"
print np.linalg.norm(a)

#Cosine of an angle
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print "a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))"
print cosangle

#Angle
angle = np.arccos(cosangle)
print "np.arccos(cosangle)"
print angle