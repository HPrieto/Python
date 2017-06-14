"""
File: linkedbag.py
Author: Heriberto Prieto
"""

from node import Node

class LinkedBag(object):
	"""A link-based bag implementation."""

	#Constructor
	def __init__(self,sourceCollection=None):
		"""Sets the initial state of self, which includes the
		contents of sourceCollection, if it's present."""
		self._items = None
		self._size  = 0
		if sourceCollection:
			for item in sourceCollection:
				self.add(item)

	def __iter__(self):
		"""Supports iteration over a view of self."""
		cursor = self._items
		while not cursor is None:
			yield cursor.data
			cursor = cursor.next

	def add(self,item):
		"""Adds item to self."""
		self._items = Node(item,self._items)
		self._size += 1

	def remove(self,item):
		"""Precondition: item is in self.
		Raises: KeyError if item is not in self
		postcondition: item is removed from self."""
		#Check precondition and raise if necessary
		if not item in self:
			raise KeyError(str(item) + ' not in bag.')
		#Search for the node containing the target item
		#Probe will point to the target node, and trailer
		#will point to the one before it, if it exists
		probe   = self._items
		trailer = None
		for targetItem in self:
			if targetItem == item:
				break
			trailer = probe
			probe   = probe.next
		#Unhook the node to be deleted, either the first one or the
		#once thereafter
		if probe == self._items:
			self._items = self._items.next
		else:
			trailer.next = prob.next
		#Decrement logical size
		self._size -= 1




























