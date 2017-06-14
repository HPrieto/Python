#import libraries
import functools

print('Built-In Python Collections and their Operations')

#Lists
print([])
print(['heriberto'])
print(['heriberto','prieto'])
print(['heriberto','male',24])
print(['heriberto',['male',24]])

playerList = []
print(playerList)
playerList.append('messi')
print(playerList)
playerList.append('heriberto')
print(playerList)
playerList.append('ronaldo')
print(playerList)
playerList.sort()
print(playerList)
playerList.pop()
print(playerList)
playerList.insert(2,'neymar')
print(playerList)
playerList.insert(3,'ronaldo')
print(playerList)
playerList.pop()
print(playerList)
playerList.remove('neymar')
print(playerList)
playerList.remove('messi')
print(playerList)

#Tuple
print('Tuples:')
tuple1 = ('physics','chemistry',2010,2019)
tuple2 = (1,2,3,4,5)
tuple3 = 'a','b','c','d'
tuple4 = (1992,)
tuple5 = ()
tuple6 = tuple2 + tuple3
print(tuple1)
print(tuple1[0])
print(tuple1[1:5])
print(tuple2)
print(tuple2[2])
print(tuple3)
print(tuple4)
print(tuple5)
print(tuple6)
del tuple6
print('cannot print tuple6, does not exist anymore.')
print('tuple1[1:] = ', tuple1[1:])
print('tuple1[-2]: ', tuple1[-2])

#Splitting and Joining Strings
print("Heriberto is the best".split())

print("".join(['heriberto',' is',' the',' best']))

#For Loop
testList = [67,100,22]
for item in testList:
	print(item)
print(67 in testList)

week  = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
nDays = len(week)
for day in range(nDays):
	print(week[day])


#Dictionaries
print({})
print({'name':'heriberto','lastname':'prieto'})
print({'hobbies':['programming','reading','soccer']})

table = {'name':'heriberto','age':24}
print(table)
print('age in table:')
print('age' in table)
print('hairColor in table:')
print('hairColor' in table)

#Pattern matching with Collections
colorTuple = ((120,90,40),'#AAD453')
rgbTuple   = colorTuple[0]
hexString  = colorTuple[1]
r = rgbTuple[0]
g = rgbTuple[1]
b = rgbTuple[2]

((red,grn,blu),hString) = colorTuple
print('((red,grn,blu),hString) = colorTuple')
print('red:     ',red)
print('green:   ',grn)
print('blue:    ',blu)
print('hString: ',hString)

#Creating New Functions
#Compute/Return the square of a number:
def square(n):
	"""Returns the square of n."""
	result=n**2
	return result

def firstMethod():
	secondMethod()
	print('calling firstMethod.')

def secondMethod():
	print('calling secondMethod.')

firstMethod()

#Recursive Functions
print("NonRecursive displayRange")
def displayRange(lower,upper):
	"""Outputs the numbers from lower to upper."""
	while lower<=upper:
		print(lower)
		lower=lower+1

displayRange(1,10)

print('Display Range Using Recursion')
def displayRangeWithRecursion(lower,upper):
	"""Outputs the numbers from lower to upper"""
	if lower<=upper:
		print(lower)
		displayRange(lower+1,upper)

displayRangeWithRecursion(1,10)

#Recursive method with Return Value
def ourSum(lower,upper):
	"""Returns the sum of the numbers from lower thru upper."""
	if lower>upper:
		return 0
	else:
		return lower+ourSum(lower+1,upper)

print('ourSum(1,5) => ',ourSum(1,5))

def traceOurSum(lower,upper,margin=0):
	"""Returns the sum of the numbers from lower to upper,
	and outputs a trace of the arguments and return values
	on each call."""
	blanks=" "*margin
	print(blanks,lower,upper)
	if lower>upper:
		print(blanks,0)
		return 0
	else:
		result=lower+traceOurSum(lower+1,upper,margin+4)
		print(blanks,result)
		return result

traceOurSum(1,5)

#Nested Function Definitions
print('Nested Function Definitions')

#First Definition
def factorial(n):
	"""Returns the factorial of n."""
	def recurse(n,product):
		if n==1: return product
		else: return recurse(n-1,n*product)
	recurse(n,1)

#Second Definition
def secondFactorial(n,product=1):
	"""Returns the factorial of n."""
	if n==1: return product
	else: return secondFactorial(n-1,n*product)

print(factorial(5))
print(secondFactorial(5))

#Higher-Order Functions
print('Higher-order Functions')
grades    = [50,0,76,89,96,67,78,0,54,67,0]
newGrades = []
for grade in grades:
	if grade > 0: newGrades.append(grade)

print('Grades:    ',grades)
print('newGrades: ',newGrades)

#Anonymous functions
print('filter using Lambda:')
finalGrades = list(filter(lambda number:number>70,grades))
print(finalGrades)

#Catching Exceptions
"""
Author: Heriberto Prieto
Demonstrates a function that traps number format errors during input
"""

def safeIntegerInput(prompt):
	"""Prompts the user for an interger and returns the
	integer if it is well-formed. Otherwise, prints an
	error message and repeats this process."""
	inputString = input(prompt)
	try:
		number = int(inputString)
		return number
	except ValueError:
		print('Error in number format: ', inputString)
		return safeIntegerInput(prompt)

if __name__=="__main__":
	age=safeIntegerInput('Enter your age:')
	print('your age is: ',age)

#Files and operations
textFile = open('python.txt','w')
textFile.write('First line.\nSecond line.\n')
textFile.close()

#Write Random values to textfile
import random
f = open('integers.txt','w')
for count in range(500):
	number = random.randint(1,500)
	f.write(str(number)+' ')
	if count%10==0:f.write('\n')
f.close()

#Reading from textfile
r = open('integers.txt','r')
fileText = r.read()
print('first pass', fileText)

#Read and process file line by line
print('\n\nRead line by line\n\n')
r = open('integers.txt','r')
lineNumber = 0
for line in r:
	lineNumber+=1
	print('Line #'+str(lineNumber)+':',line)

""" Write integers to file and add them all up """
f = open('integer1.txt','w')
for count in range(500):
	number = random.randint(1,500)
	f.write(str(number)+'\n')
f.close()

r = open('integer1.txt','r')
fileSum = 0
for line in r:
	line = line.strip()
	number = int(line)
	fileSum += number
print('\n\nThe sum is: ',fileSum)

print('\n\n\nReading and Writing Objects with pickle.\n\n')

import pickle

#Write objects to file using pickle
lyst = [25,'String Object',1992]
fileObj = open('items.dat','wb')
for item in lyst:
	pickle.dump(item,fileObj)
fileObj.close()

#Load objects from file using pickle
loadedLyst = list()
fileObj = open('items.dat','rb')
while True:
	try:
		item = pickle.load(fileObj)
		loadedLyst.append(item)
	except EOFError:
		fileObj.close()
		break
print(loadedLyst)

print('\n\n\nCreating New Classes\n\n')

class Counter(object):
	"""Models a counter."""
	#Class Data Member(s)
	instances=0

	#Constructor
	def __init__(self):
		"""Sets up the counter."""
		Counter.instances+=1
		self.reset()

	#Mutator Methods
	def reset(self):
		"""Sets the counter to 0."""
		self._value=0

	def increment(self,amount=1):
		"""Adds amount to the counter."""
		self._value+=amount

	def decrement(self,amount=1):
		"""Subtracts amount from the counter."""
		self._value-=amount

	#Accessor methods
	def getValue(self):
		"""Returns the counter's value."""
		return self._value

	def __str__(self):
		"""Returns the string representation of the counter."""
		return str(self._value)

	def __eq__(self,other):
		"""Returns True if self equals other
		or False otherwise."""
		if self is other: return True
		if type(self) != type(other):return False
		return self._value==other._value

c1 = Counter()
print('Counter initial value: ',c1)
print('Counter getValue:      ',c1)

c1.increment()
print('Value After increment: ',c1)

c1.increment(10)
print('After incrementing 5:  ',c1)

c1.decrement()
print('After decrement:       ',c1)

print('Number of instances before c2:',Counter.instances)

c2 = Counter()

print('Number of instances after c2: ',Counter.instances)

print('c1==c2 before c1 reset: ',c1==c2)

c1.reset()

print('c1==c2 after reset:     ',c1==c2)













