print('Interfaces, Implementations, and Polymorphism')

print('Developing an Interface')

print('Designing the Bag Interface')

print('Specifying Arguments and Return Values')

print('Constructors and Implementing Classes')

print('Preconditions, Postconditions, Exceptions, and Documentation')

def remove(self,item):
	"""Precondition: item is in self. 
	Raises: KeyError if item in not in self. 
	Postcondition: items is removed from self."""


print('\n\nCoding an Interface in Python')

print('\n\nDeveloping an Array-Based Implementation')

print('\n\nChoose and Initialize the Data Structures')

print('\n\nDeveloping a Link-Based Implementation')

print('\n\nRun-Time Performance of the Two Bag Implementations')

"""
File: testbag.py 
Author: Heriberto Prieto
A tester program for bag implementation
"""

from arraybag import ArrayBag 
from linkedbag import LinkedBag 

def test(bagType):
	"""Expects a bag type as an argument and runs some tests
	on objects of that type."""
	lyst=[2013,61,1973]
	print('The list of items added is: ',lyst)
	b1=bagType(lyst)
	print('Expect 3:',len(b1))
	print('Expect the bag\'s string: ',b1)
	print('Expect True: ',2013 in b1)
	print('Expect False: ',2012 in b1)
	print('Expect the items on seperate lines:')
	for item in b1:
		print(item)
	b1.clear()
	print('Expect {}: ',b1)
	b1.add(25)
	b1.remove(25)
	print('Expect {}: ',b1)
	b1 = bagType(lyst)
	b2 = bagType(b1)
	print('Expect True: ',b1==b2)
	print('Expect False: ',b1 is b2)
	print('Expect two of each item: ',b1+b2)
	for item in lyst:
		b1.remove(item)
	print('Expect {}:',b1)
	print('Expect crash with KeyError:')
	b2.remove(99)
#Test(ArrayBag)
test(LinkedBag)

print('\n\nDiagramming the Bag Resource with UML')




































