from linkedlist import LinkedList

def testInsert(ll):
	print('Testing inserts: ')
	ll.insert(2)
	ll.insert(3)
	ll.insert(87)
	ll.insert(77)
	ll.insert(123)
	ll.insert(5)
	ll.printAllElements()

def testDeleteByPosition(ll):
	print('Testing delete by value: ')
	ll.deleteByValue(2)
	ll.deleteByValue(5)
	ll.printAllElements()

def testDeleteByPosition(ll):
	print('Testing delete by position: ')
	ll.deleteByPosition(4)
	ll.deleteByPosition(2)
	ll.printAllElements()

def testSearch(ll):
	print('Testing search: ')
	ll.searchByValue(333)
	ll.searchByValue(123)

def testChangeNthElement(ll):
	print('Testing change nth element: ')
	ll.changeValueOfNthElement(1, 12)
	ll.printAllElements()

if __name__ == '__main__':
	ll = LinkedList()
	testInsert(ll)
	testDeleteByPosition(ll)
	testSearch(ll)
	testChangeNthElement(ll)
	
	

	
