from node import Node 


class LinkedList:
	def __init__(self):
		self.first_node = ''


	def getLastNode(self):
		if not self.first_node.getPrev()=='EOF':
			return self.first_node.getPrev()
		else:
			return self.first_node

	def insert(self, value):
		if not self.first_node=='':
			new_node = Node(value)
			last_node = self.getLastNode()
			last_node.setNext(new_node)
			new_node.setPrev(last_node)
		else:
			new_node = Node(value)
			self.first_node = new_node

	def findFirstNodeWithGivenValue(self, value):
		curr = self.first_node
		while( not curr=='EOF' ):
			if curr.getValue()==value:
				return curr
			else:
				curr = curr.getNext()
		return -1


	def deleteByValue(self, value):
		this_node, prev = self.findFirstNodeWithGivenValue(value)
		if prev==-1:
			print('Element not found!')
		elif prev=='':
			self.first_node = this_node.getNext() 
		else:
			prev.setNext(this_node.getNext())

	def findNodeAtPosition(self, position):
		curr = self.first_node
		pos = 1
		while( not curr=='EOF' ):
			if pos==position:
				return curr
			else:
				pos += 1
				curr = curr.getNext()
		return -1


	def getLength(self):
		count = 0
		this_node = self.first_node
		while( not this_node=='EOF' ):
			this_node = this_node.getNext()
			count+=1
		return count


	def deleteByPosition(self, position):
		length = self.getLength()
		if position>length:
			print('Given position larger than length!')
		else:
			this_node = self.findNodeAtPosition(position)
			if this_node==-1:
				print('Element not found!')
			elif this_node=='':
				self.first_node = this_node.getNext() 
			else:
				this_node.getPrev().setNext(this_node.getNext())

	def printAllElements(self):
		this_node = self.first_node
		while( not this_node=='EOF' ):
			print(this_node.getValue())
			this_node = this_node.getNext()

	def printAllElementsReverse(self):
		this_node = self.first_node
		while not this_node=='EOF':
			print(this_node.getValue())
			this_node = this_node.getPrev()


	def searchByValue(self, value):
		curr = self.first_node
		position = 1
		while( not curr=='EOF' ):
			if curr.getValue()==value:
				print('Element at position: (counting starts at 1) ', position)
				return 
			else:
				position += 1
				curr = curr.getNext()
		print('Element not found!')

	def changeValueOfNthElement(self, n, value):
		nth_element = self.findNodeAtPosition(n)
		if nth_element==-1:
			print('Element not found!')
		else:
			nth_element.setValue(value)




