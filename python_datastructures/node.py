"""
File: testnode.py
Tests the Node class.
"""
class Node(object):
	"""Represents a singly linked node."""
	def __init___(self,data,next=None):
		"""Instantiates a Node with a default next of None."""
		self.data = data
		self.next = next