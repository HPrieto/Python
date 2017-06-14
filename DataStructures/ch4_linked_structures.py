"""
Chapter 4
Arrays and Linked Structures
"""

print('The Array Data Structure')

"""
File: arrays.py

An Array is like a list, but the client can use
only [], len, iter and str. 

To instantiate, use

<variable>=Array(<capacity>,<optional fill value>)

The fill value is None by default
"""

class NArray(object):
	"""Represents an array"""
	def __init__(self,capacity,fillValue=None):
		"""Capacity is the static size of the array. 
		fillValue is placed at each position."""
		self._items=list()
		for count in range(capacity):
			self._items.append(fillValue)

	def __len__(self):
		"""->The capacity of the array."""
		return len(self._items)

	def __str__(self):
		"""->The string representation of the array."""
		return str(self._items)

	def __iter__(self):
		"""->Supports traversal with a for loop."""
		return iter(self._items)

	def __getitem__(self,index):
		"""Subscript operator for access at index."""
		return self._items[index]

	def __setitem__(self,index,newItem):
		"""Subscript operator for replacement at index."""
		self._items[index]=newItem


a = NArray(5)
l = len(a)
print('Array:',a)
print('Length: ',l)

for i in range(len(a)):
	a[i]=i+1

print('Array:',a)


print('\n\nRandom Access and Contiguous Memory')

print('\n\nStatic Memory and Dynamic Memory')

print('\n\nPysical Size and Logical Size')

print('\n\nOperations on Arrays')

print('\n\nIncreasing the Size of an Array')

logicalSize=10
def increaseArraySize(arr,logicalSize):
	if logicalSize==len(arr):
	temp=NArray(len(arr)+1)
	for i in range(logicalSize):
		temp[i]=arr[i]
	return temp

def doubleArraySize(arr,logicalSize):
	if logicalSize==len(a):
	temp=NArray(len(a)*2)
	for i in range(logicalSize):
		temp[i]=a[i]
	return temp

print('\n\nDecresing the Size of an Array')

def decreaseArraySize(arr,logicalSize):
	if logicalSize<=len(arr)//4 and len(arr)>=DEFAULT_CAPACITY*2:
		temp=Array(len(arr)//2)
		for i in range(logicalSize):
			temp[i]=arr[i]
		return temp

print('\n\nInserting an Item into an Array That Grows')

#Increasing physical size of array if necessary
#Shift items down by one position
def insertItemAtIndex(lyst,item,targetIndex,logicalSize):
	for i in range(logicalSize,targetIndex,-1):
		lyst[i]=lyst[i-1]
	#Add new item and increment logical size
	lyst[targetIndex]=newItem
	logicalSize+=1


print('\n\nRemoving an item from an array')

def removeItem(lyst,targetIndex,logicalSize):
	#Shift items up by one position
	for i in range(targetIndex,logicalSize-1):
		a[i]=a[i+1]
	#Decrement logical size
	logicalSize-=1
	#Decrement size of array if necessary

print('\n\nComplexity Trade-Off: Time, Space, and Arrays')

print('\n\nTwo-Dimensional Arrays(Grids)')

x = table[2][3] #Set x to 23, the value in (row 2, column 3)

print('\n\nProcessing a Grid')

def getSums(table):
	nSum=0
	for row in range(table.getHeight()):
		for column in range(table.getWidth()):
			nSum+=table[row][column]

print('\n\nCreating and initialize a Grid')

#Define Grid Class

from arrays import Array
class Grid(object):
	"""Represents a two-dimensional array."""
	def __init__(self,rows,columns,fillValue=None):
		self._data=Array(rows)
		for row in range(rows):
			self._data[row]=Array(columns,fillValue)

	def getHeight(self):
		"""Returns the number fo rows."""
		return len(self._data)

	def getWidth(self):
		"""Returns the number of columns."""
		return len(self._data[0])

	def __getitem__(self,index):
		"""Supports two-dimensional indexing
		with[row][column]."""
		return self._data[index]

	def __str___(self):
		"""Returns a string representation of the grid."""
		result=""
		for row in range(self.getHeight()):
			for col in range(self.getWidth()):
				result+=str(self._data[row][col])+" "
			result+="\n"
		return result

gridTable = Grid(10,10,0)
print(gridTable)

print('\n\nRagged Grids and Multidimensional Arrays')

print('Linked Structures')

print('Singly Linked Structures and Doubly Linked Structures')

print('Noncontinuous Memory and Nodes')

print('Defining a Singly Linked Node Class')

class Node(object):
	"""Represents a singly linked node."""
	def __init___(self,data,next=None):
		"""Instantiates a Node with a default next of None."""
		self.data = data
		self.next = next

print('Using the Singly Linked Node Class')

#Empty link
node1=None

#A node containing data and an empty link
node1 = Node('A',None)

#A node containing data and a link to node2
node3 = Node('B',node2)

head = None

#Add five nodes to the begining of the linked structure
for count in range(1,6):
	head = Node(count,head)

#Print the contents of the structure
while head!=None:
	print(head.data)
	head=head.next

print('\n\nOperations on Singly Linked Structures')

print('\n\nTraversal\n\n')

probe = head
while probe!=None:
	probe=probe.next

print('\n\nSearching')

probe = head
while probe!=None and targetItem!=probe.data:
	probe=probe.next
if probe!=None:
	print('Target item found')
else:
	print('Target is not in the linked structure')

#Access the ith item
#Assume 0<=index<n
probe=head
while index>0:
	probe=probe.next
	index-=1
return probe.data

print('\n\nReplacement')

probe = head
while probe!=None and targetItem!=probe.data:
	probe=probe.next
if probe!=None:
	probe.data=newItem
	return True
else:
	return False

#Assumes 0<=index<n
probe = head
while index>0:
	probe=probe.next
	index-=1
probe.data=newItem

print('\n\nInserting at the Beginning')

head = Node(newItem,head)

print('\n\nInserting at the End')

newNode = Node(newItem)
if head is None:
	head = newNode
else:
	probe = head
	while probe.next!=None:
		probe=probe.next
	prob.next = newNode

print('\n\nRemoving at the Beginning')

#Assumes at least one node in the structure
def removeHead(head):
	#Assumes at leas one node in the structure
	removedItem = head.data
	head = head.next
	return removedItem

print('\n\nRemoving at the End')

def removeTail(head):
	removedItem = head.data
	if head.next is None:
		head = None
	else:
		probe = head
		while probe.next.next!=None:
			probe = probe.next
		removedItem = probe.next.data
		probe.next = None
	return removedItem

print('\n\nInserting at Any Position')

def insertAtIndex(newItem,index,head):
	if head is None or index <= 0:
		head = Node(newItem,head)
	else:
		#Search for node at position index - 1 or the last position
		probe = head
		while index > 1 and probe.next != None:
			probe = probe.next
			index -= 1
		#Insert new node after node at position index - 1
		#or last position
		probe.next = Node(newItem,probe.next)

print('\n\nRemoving at Any Position')

#Assumes that the linked structure has at least one item
def removeAtIndex(removedItem,index,head):
	if index <= 0 or head.next is None:
		removedItem = head.data
		head = head.next
		return removedItem
	else:
		#Search for node at position index - 1 or
		#the next to last position
		probe = head
		while index > 1 and probe.next.next != None:
			probe = probe.next
			index -= 1
		removedItem = probe.next.data
		probe.next = probe.next.next
		return removedItem

print('\n\nComplexity Trage-Off: Time, Space, and Singly Structures')

print('\n\nVariations on a Link')

print('\n\nA Circular Linked Structure with a Dummy Header Node')

#Initialize head node
head = Node(None,None)
head.next = head

def insertAtIndexInCircularList(index,newItem,head):
	probe = head
	while index > 0 and probe.next != head:
		probe = probe.next
		index -= 1
	#Insert new node after node at position index -1 or
	#last position
	probe.next = Node(newItem,probe.next)

print('\n\nDouble Linked Structures')

class Node(object):
	def __init__(self,data,next=None):
		"""Instantiates a Node with default next of None"""
		self.data = data
		self.next = next

class TwoWayNode(Node):
	def __init__(self.data,previous=None,next=None):
		"""Instantiates a TwoWayNode."""
		Node.__init__(self,data,next)
		self.previous = previous

"""
File: testwowaynode.py
Tests the TwoWayNode class.
"""

#Create a doubly linked structure with one node
head = TwoWayNode(1)
tail = head

#Add four nodes tot he end of the doubly linked structure
for data in range(2,6):
	tail.next = TwoWayNode(data,tail)
	tail = tail.next

#Prints the contents of the linked structure in reverse order
probe = tail
while probe != None:
	print(probe.data)
	probe = probe.previous

tail.next = TwoWayNode(data,tail)
tail = tail.next






































