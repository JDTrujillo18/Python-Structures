import DLinkedList


class Queue(DLinkedList.DLinkedList):
	def __init__(self, data=None):
		super(Queue, self).__init__(data)

	def __str__(self, arrows=False, queue=False):
		if queue:
			mystr = '\nQueue:\nLength: ' + str(len(self)) + '\nFront: ' + str(self.head.data) + '\n'
			for item in self:
				mystr += ' ' + str(item) + ' ->'
			mystr += ' Null\nBack: ' + str(self.tail.data) + '\n'
			return mystr
		elif arrows:
			return super(Queue, self).__str__(arrows=True)
		else:
			return super(Queue, self).__str__()

	def is_empty(self):
		if len(self) == 0:
			return True
		else:
			return False

	def enqueue(self, value):
		self.insert(value, 0)

	def dequeue(self):
		return self.pop()

	def front(self):
		return self.head.data

	def size(self):
		return len(self)

	def format(self):
		print(self.__str__(arrows=True))

	def printqueue(self):
		print(self.__str__(queue=True))
