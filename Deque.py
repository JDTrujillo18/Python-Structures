import DLinkedList


class Deque(DLinkedList.DLinkedList):
	def __init__(self, data):
		super(Deque, self).__init__(data)

	def __str__(self, arrows=False, queue=False):
		if queue:
			mystr = '\nDeque:\nLength: ' + str(len(self)) + '\nFront: ' + str(self.head.data) + '\n'
			for item in self:
				mystr += ' ' + str(item) + ' ->'
			mystr += ' Null\nRear: ' + str(self.tail.data) + '\n'
			return mystr
		elif arrows:
			return super(Deque, self).__str__(arrows=True)
		else:
			return super(Deque, self).__str__()

	def is_empty(self):
		return len(self) == 0

	def addFront(self, value):
		self.insert(value, 0)

	def addRear(self, value):
		self.append(value)

	def removeFront(self):
		return self.pop(0)

	def removeRear(self):
		return self.pop()

	def size(self):
		return len(self)

	def arrows(self):
		print(self.__str__(arrows=True))

	def format(self):
		return print(self.__str__(queue=True))
