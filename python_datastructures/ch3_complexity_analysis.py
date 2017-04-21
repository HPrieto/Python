print('Searching, Sorting and Complexity Analysis')

print('Measuring the Efficiency of Algorithms')

print('Measuring the Run Time of an Algorithm')

"""
File: timingly.py
Prints the running times for problem sizes that double,
using a single loop.
"""

import time

problemSize = 1000000
print('%12s%16s'%('ProblemSize 1','Seconds'))
for count in range(5):
	start = time.time()
	#Start of the algorithm
	work=1
	for x in range(problemSize):
		work+=1
		work-=1
	#End of the algorithm
	elapsed = time.time()-start
	print('%12s%16.3f'%(problemSize,elapsed))
	problemSize*=2

problemSize = 100
print('%12s%16s'%('ProblemSize 2','Seconds'))
for count in range(5):
	start = time.time()
	#Start of the algorithm
	work=1
	for j in range(problemSize):
		for k in range(problemSize):
			work+=1
			work-=1
	#End of the algorithm
	elapsed = time.time()-start
	print('%12s%16.3f'%(problemSize,elapsed))
	problemSize*=2


"""
File: counting.py
Prints the number of iterations for problem sizes
that double, using a nested loop.
"""

problemSize=100
print('%12s%15s'%('ProblemSize 3','Iterations'))
for count in range(5):
	number=0

	#Start of algorithm
	work=1
	for j in range(problemSize):
		for k in range(problemSize):
			number+=1
			work+=1
			work-=1
	#End of the algorithm
	print('%12d%15d'%(problemSize,number))
	problemSize*=2

"""
File: countfib.py
Prints the number of calls of a recursive Fibonacci
function with problem sizes that double
"""

#Create Counter Class
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

def fib(n,counter):
	"""Count the number of calls of the Fibonacci
	function."""
	counter.increment()
	if n<3:
		return 1
	else:
		return fib(n-1,counter)+fib(n-2,counter)

problemSize=2
print('%12s%15s',('ProblemSize 4','Calls'))
for count in range(5):
	counter = Counter()

	#Start of the algorithm
	fib(problemSize,counter)
	#The end of the algorithm

	print('%12s%15s'%(problemSize,counter.getValue()))
	problemSize*=2

print('\n\nMeasuring the Memory Used by an Algorithm\n\n')

print('\n\nComplexity Analysis\n\n')

print('\n\nOrders of Complexity\n\n')

print('\n\nBig-O Notation\n\n')

print('\n\nThe Role of the Constant of Proportionality\n\n')

print('\n\nSearch Algorithms\n\n')

print('\n\nSearch for the Minimum\n\n')

import random as rand

lyst = []
for index in range(1,101):
	lyst.append(rand.randint(1,101))

def indexOfMin(lyst):
	"""Returns the index of the minimum item."""
	minIndex=0
	currentIndex=1
	while currentIndex<len(lyst):
		if lyst[currentIndex]<lyst[minIndex]:
			minIndex=currentIndex
		currentIndex+=1
	return minIndex

index = indexOfMin(lyst)
print('Smallest value in list:',lyst[index])

print('\n\nSequential Search of a List\n\n')

def sequentialSearch(target,lyst):
	"""Returns the position of the target item if found,
	or -1 otherwise."""
	position=0
	while position<len(lyst):
		if target==lyst[position]:
			return position
		position+=1
	return -1

randTarget = rand.randint(1,101)
sequentialIndex = sequentialSearch(randTarget,lyst)
print('Target: ',randTarget)
print('Index:  ',sequentialIndex)
print('Value:  ',lyst[sequentialIndex])

print('\nBinary Search\n')

def binarySearch(target,sortedLyst):
	left=0
	right=len(sortedLyst)-1
	while left<=right:
		midpoint=(left+right)//2
		if target==sortedLyst[midpoint]:
			return midpoint
		elif target<sortedLyst[midpoint]:
			right=midpoint-1
		else:
			left=midpoint+1
	return -1

randTarget = rand.randint(1,101)
binaryIndex = binarySearch(randTarget,lyst)
print('Binary Target: ',randTarget)
print('Binary Index:  ',binaryIndex)
print('Binary Value:  ',lyst[binaryIndex])

print('Comparing Data Items\n\n')

class SavingsAccount(object):
	"""This class represents a savings account
	with the owner's name, PIN, and balance."""

	def __init__(self,name,pin,balance=0.0):
		self._name=name
		self._pin=pin
		self._balance=balance

	def __lt__(self,other):
		return self._name<other._name

	#Other methods, including __eq__
s1=SavingsAccount('Heriberto','1000',0)
s2=SavingsAccount('Nancy','1001',30)
print('s1<s2',s1<s2)
print('s1>s2',s1>s2)
print('s1==s2',s1==s2)


print('\n\nBasic Sort Algorithms\n\n')

def swap(lyst,i,j):
	"""Exchanges the items at positions i and j."""
	#you could say lyst[i],lyst[j]=lyst[j],lyst[i]
	#but the following code shows what is really going on
	temp=lyst[i]
	lyst[i]=lyst[j]
	lyst[j]=temp

print('\n\nSelection Sort\n\n')

def selectionSort(lyst):
	i=0
	while i<len(lyst)-1:
		minIndex=i
		j=i+1
		while j<len(lyst):
			if lyst[j]<lyst[minIndex]:
				minIndex=j
			j+=1
		if minIndex!=1:
			swap(lyst,minIndex,i)
		i+=1

selectionSortLyst=[]
for index in range(1,101):
	selectionSortLyst.append(rand.randint(1,101))
print('Lyst before sorting:')
print(selectionSortLyst)
print('\n\nPerform SelectionSort\n\n')
selectionSort(selectionSortLyst)
print(selectionSortLyst)
print('\n\nEnd of SelectionSortExample\n\n')

print('\n\nBubble Sort\n\n')

def bubbleSort(lyst):
	n=len(lyst)
	while n>1:
		i=1
		while i<n:
			if lyst[i]<lyst[i-1]:
				swap(lyst,i,i-1)
			i+=1
		n-=1

bubbleList=[]
for index in range(1,101):
	bubbleList.append(rand.randint(1,101))

print('BubbleList before sort:\n',bubbleList)
print('\nPerform BubbleSort\n')
bubbleSort(bubbleList)
print('BubbleList after sort:\n',bubbleList)

print('\nImproved BubbleSort')

def improvedBubbleSort(lyst):
	n=len(lyst)
	while n>1:
		swapped=False
		i=1
		while i<n:
			if lyst[i]<lyst[i-1]:
				swap(lyst,i,i-1)
				swapped=True
			i+=1
		if not swapped: return
		n-=1

improvedBubbleList=[]
for index in range(1,101):
	improvedBubbleList.append(rand.randint(1,101))

print('ImprovedBubbleList Before Sort:\n',improvedBubbleList)
print('\nImprovedBubbleSort performed.\n')
improvedBubbleSort(improvedBubbleList)
print('ImprovedBubbleList after sort:\n',improvedBubbleList)

print('\n\nInsertion Sort\n\n')

def insertionSort(lyst):
	i=1
	while i<len(lyst):
		itemToInsert=lyst[i]
		j=i-1
		while j>=0:
			if itemToInsert<lyst[j]:
				lyst[j+1]=lyst[j]
				j-=1
			else:
				break
		lyst[j+1]=itemToInsert
		i+=1

insertionList=[]
for index in range(1,101):
	insertionList.append(rand.randint(1,101))

print('InsertionList before Sort:\n',insertionList)
print('\nPerform InsertionSort\n')
insertionSort(insertionList)
print('\nInsertionList after Sort:\n',insertionList)

print('\n\nQuicksort\n')
print('Complexity Analysis of Quicksort\n')

def quicksort(lyst):
	quicksortHelper(lyst,0,len(lyst)-1)

def quicksortHelper(lyst,left,right):
	if left<right:
		pivotLocation=partition(lyst,left,right)
		quicksortHelper(lyst,left,pivotLocation-1)
		quicksortHelper(lyst,pivotLocation+1,right)

def partition(lyst,left,right):
	#Find the pivot and exchange it with the last item
	middle=(left+right)//2
	pivot=lyst[middle]
	lyst[middle]=lyst[right]
	lyst[right]=pivot
	#Set boundary point to first position
	boundary=left
	#Move items less than pivot to the left
	for index in range(left,right):
		if lyst[index]<pivot:
			swap(lyst,index,boundary)
			boundary+=1
	#Exchange the pivot item and the boundary item
	swap(lyst,right,boundary)
	return boundary

quickList=[]
for index in range(1,101):
	quickList.append(rand.randint(1,101))

print('QuickList Before Sort:\n',quickList)
print('\nPerform Quicksort.')
quicksort(quickList)
print('\nQuickList After Sort:\n',quickList)

print('\n\nMerge Sort\n\n')

from arrays import Array 

def mergeSort(lyst):
	#lyst 		list being sorted
	#copyBuffer temprorary space needed during merge
	copyBuffer=Array(len(lyst))
	mergeSortHelper(lyst,copyBuffer,0,len(lyst)-1)

def mergeSortHelper(lyst,copyBuffer,low,high):
	#high 			list being sorted
	#copyBuffer temp space needed during merge
	#low, high 		bounds of sublist
	#middle 		midpoint of sublist
	if low<high:
		middle=(low+high)//2
		mergeSortHelper(lyst,copyBuffer,low,middle)
		mergeSortHelper(lyst,copyBuffer,middle+1,high)
		merge(lyst,copyBuffer,low,middle,high)

def merge(lyst,copyBuffer,low,middle,high):
	#lyst 		list that is being sorted
	#copyBuffer temp space needed during the mrege process
	#low 		beginning of first sorted sublist
	#middle 	end of first sorted sublist
	#middle+1 	beginning of second sorted sublist
	#high 		end of second sorted sublist

	#initialize i1 and i2 to the first items in each sublist
	i1=low
	i2=middle+1

	#Interleave items from the sublists into the
	#copyBuffer in such a way that order is maintained
	for i in range(low,high+1):
		if i1>middle:
			copyBuffer[i]=lyst[i2]#First sublist exhausted
			i2+=1
		elif i2>high:
			copyBuffer[i]=lyst[i1]#Second sublist exhausted
			i1+=1
		elif lyst[i1]<lyst[i2]:
			copyBuffer[i]=lyst[i1]#Item in first sublist<
			i1+=1
		else:
			copyBuffer[i]=lyst[i2]#Item in second sublist
			i2+=1
	for i in range(low,high+1):   #Copy sorted items back to
		lyst[i]=copyBuffer[i] 	  #proper position in lyst


print('An Exponential Algorithm: Recursive Fibonacci')

print('Convertin Fibonacci to a Linear Algorithm')

def linearFib(n,counter):
	"""Count the number of iterations in the Fibonacci
	function."""
	nSum=1
	first=1
	second=1
	count=3
	while count<=n:
		counter.increment()
		nSum=first+second
		first=second
		second=nSum
		count+=1
	return nSum

print('Case Study: An Algorithm Profiler')

from profiler import Profiler
from algorithms import selectionSort

p=Profiler()

p.test(selectionSort) 	#Default behavior

p.test(selectionSort,size=5,trace=True)

p.test(selectionSort,size=100)

p.test(selectionSort,size=1000)

p.test(selectionSort,size=10000,exch=False,comp=False)

#Design

print('Implementation (Coding)')

"""
File: algorithms.py
Algorithms configured for profiling.
"""

def selectionSort(lyst,profiler):
	i=0
	while i<len(lyst)-1:
		minIndex=i
		j=i+1
		while j<len(lyst):
			profiler.comparison()
			if lyst[j]<lyst[minIndex]:
				minIndex=j
			j+=1
		if minIndex!=i:
			swap(lyst,minIndex,i,profiler)
		i+=1

def swap(lyst,i,j,profiler):
	"""Exchanges the elements at positions i and j."""
	profiler.exchange() 	#count
	temp=lyst[i]
	lyst[i]=lyst[j]
	lyst[j]=temp

#Testing code can go here, optionally

"""
File: profiler.py

Defines a class for profiling sort alagorithms. 
A profiler object tracks the list, the number of comparisons
and exchanges, and the running time. The Profiler can also
print a trace and can create a list of unique or duplicate
numbers. 

Example use:

from profiler import Profiler
from algorithms import selectionSort

p=Profiler()
p.test(selectionSort,size=15,comp=True,exch=True,trace=True)
"""

import time
import random

class Profiler(object):
	def test(self,function,lyst=None,size=10,
		unique=True,comp=True,exch=True,
		trace=False):
	"""
	function: the algorithm being profiled
	target:   the search target if profiling a search
	lyst:     allows the caller to use her list
	size:     the size of the list, 10 by default
	unique:   if True, list contains unique integers
	comp:     if True, count comparisons
	exch:     if True,count exchanges
	trace:    if True, print the list after each exchange

	Run the function with the given attributes and print
	its profile results.
	"""
	self._comp=comp
	self._exch=exch
	self._trace=trace
	if lyst!=None:
		self._lyst=lyst
	elif unique:
		self._lyst=range(1,size+1)
		random.shuffle(self._lyst)
	else:
		self._lyst=[]
		for count in range(size):
			self._lyst.append(random.randint(1,size))
	self._exchCount=0
	self._cmpCount=0
	self._startClock()
	function(self._lyst,self)
	self._stopClock()
	print(self)

def exchange(self):
	"""Counts exchanges if on."""
	if self._exch:
		self._exchCount+=1
	if self._trace:
		print(self._lyst)

def comparison(self):
	"""Counts comparisons if on."""
	if self._comp:
		self._cmpCount+=1

def _startClock(self):
	"""Record the starting time."""
	self._start=time.time()

def _stopClock(self):
	"""Stops the clock and computes the elapsed time
	in seconds. to the nearest millisecond."""
	self._elapsedTime=round(time.time()-self._start,3)

def _str_(self):
	"""Returns the results as a string."""
	result="Problem size: "
	result+=str(len(self._lyst))+'\n'
	result+='Elapsed time: '
	result+=str(self._elapsedTime)+'\n'
	if self._comp:
		result+='Comparisons: '
		result+=str(self._cmpCount)+'\n'
	if self._exch:
		result+='Exchanges: '
		result+=str(self._exchCount)+'\n'
	return result