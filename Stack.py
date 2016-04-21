import DLinkedList


class Stack(DLinkedList.DLinkedList):
	def __init__(self, data=None):
		super(Stack, self).__init__(data)

	def __str__(self, arrows=False, stack=False, format=False):
		if arrows:
			copy = self.copy()
			copy.reverse()
			return copy.__str__(True)
		elif stack:
			self.reverse()
			mystr = '\nStack:\nLength: ' + str(len(self)) + '\nTop: ' + str(self.head.data) + '\n'
			for item in self:
				mystr += '    ' + str(item) + '\n'
			mystr += 'Bottom: ' + str(self.tail.data) + '\n'
			self.reverse()
			return mystr
		elif format:
			mystr = '\n'
			self.reverse()
			for item in self:
				mystr += '    '+ str(item) + '\n'
			self.reverse()
			return mystr
		else:
			copy = self.copy()
			copy.reverse()
			return copy.__str__()

	def push(self, value):
		self.append(value)

	def peek(self):
		return self.tail.data

	def is_empty(self):
		if len(self) == 0:
			return True
		else:
			return False

	def arrows(self):
		print(self.__str__(arrows=True))

	def printstack(self):
		print(self.__str__(stack=True))

	def format(self):
		print(self.__str__(format=True))
