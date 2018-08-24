from node import Node 


class LinkedList:
	def __init__(self):
		self.first_node = ''


	def getLastNode(self):
		this_node = self.first_node
		while( not this_node.getNext()=='EOF' ):
			this_node = this_node.getNext()
		return this_node

	def insert(self, value):
		if not self.first_node=='':
			new_node = Node(value)
			last_node = self.getLastNode()
			last_node.setNext(new_node)
		else:
			new_node = Node(value)
			self.first_node = new_node

	def findFirstNodeWithGivenValue(self, value):
		prev = ''
		curr = self.first_node
		while( not curr=='EOF' ):
			if curr.getValue()==value:
				return curr, prev
			else:
				prev = curr
				curr = curr.getNext()
		return -1, -1


	def deleteByValue(self, value):
		this_node, prev = self.findFirstNodeWithGivenValue(value)
		if prev==-1:
			print('Element not found!')
		elif prev=='':
			self.first_node = this_node.getNext() 
		else:
			prev.setNext(this_node.getNext())

	def findNodeAtPosition(self, position):
		prev = ''
		curr = self.first_node
		pos = 1
		while( not curr=='EOF' ):
			if pos==position:
				return curr, prev
			else:
				pos += 1
				prev = curr
				curr = curr.getNext()
		return -1, -1


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
			this_node, prev = self.findNodeAtPosition(position)
			if prev==-1:
				print('Element not found!')
			elif prev=='':
				self.first_node = this_node.getNext() 
			else:
				prev.setNext(this_node.getNext())

	def printAllElements(self):
		this_node = self.first_node
		while( not this_node=='EOF' ):
			print(this_node.getValue())
			this_node = this_node.getNext()

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
		nth_element, prev = self.findNodeAtPosition(n)
		if prev==-1:
			print('Element not found!')
		else:
			nth_element.setValue(value)




