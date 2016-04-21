class DNode:
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev


class DLIterator:
	def __init__(self, DLList):
		self._cur = DLList.head

	def __next__(self):
		if self._cur is None:
			raise StopIteration
		else:
			val = self._cur.data
			self._cur = self._cur.next
			return val


class DLinkedList:
	def __init__(self, data=None):
		self.head = None
		self.tail = None
		self.count = 0
		if data:
			if isinstance(data, int) or isinstance(data, float):
				self.append(data)
			elif isinstance(data, list) or isinstance(data, DLinkedList):
				for value in data:
					self.append(value)
			else:
				print("Invalid Input")

	def __str__(self, arrows=False):
		if self.count == 0:
			return "Linked list is empty"
		else:
			datalist = []
			for node in range(0, self.count):
				datalist.extend([str(self[node])])
			if not arrows:
				return '[' + ', '.join(datalist) + ']'
			else:
				mystr = '\nDouble Linked List:\nLength: ' + str(self.count) + '\nHead: ' + str(self.head.data) + '\n'
				for node in range(0, len(datalist) - 1):
					mystr += '    ' + str(datalist[node]) + ' <--> ' + str(datalist[node + 1]) + '\n'
				mystr += 'Tail: ' + str(self.tail.data) + '\n'
				return mystr

	def __len__(self):
		return self.count

	def __iter__(self):
		return DLIterator(self)

	def __getitem__(self, item):
		if isinstance(item, int):
			if item == 0:
				return self.head.data
			else:
				currentnode = self.head
				for node in range(0, item):
					currentnode = currentnode.next
				return currentnode.data
		elif isinstance(item, slice):
			return DLinkedList([self[x] for x in range(*item.indices(len(self)))])
		else:
			print('Index must be an integer or slice')

	def __setitem__(self, key, value):
		if isinstance(key, int):
			if key == 0:
				self.head.data = value
			elif key < self.count:
				currentnode = self.head
				for node in range(0, key):
					currentnode = currentnode.next
				currentnode.data = value
			else:
				print("Index out of range")
		elif isinstance(key, slice):
			if isinstance(value, int):
				if len([x for x in range(*key.indices(len(self)))]) == 1:
					count = 0
					for x in range(*key.indices(len(self))):
						self[x] = value
						count += 1
				else:
					print("Sizes don't match")
			elif isinstance(value, list) or isinstance(value, DLinkedList):
				if len([x for x in range(*key.indices(len(self)))]) != len(value):
					print('Indices out of range')
				else:
					count = 0
					for x in range(*key.indices(len(self))):
						self[x] = value[count]
						count += 1

	def __add__(self, other):
		if isinstance(other, DLinkedList) or isinstance(other, list):
			datalist = []
			for item in self:
				datalist.extend([item])
			for item in other:
				datalist.extend([item])
			return DLinkedList(datalist)
		elif isinstance(other, int) or isinstance(other, float):
			return self.__iadd__(other)
		else:
			print('Cannot add type DLinkedList and ' + str(type(other)))

	def __radd__(self, other):
		return self.__add__(other)

	def __iadd__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			currentnode = self.head
			for node in range(0, self.count):
				currentnode.data += other
				currentnode = currentnode.next
		elif isinstance(other, DLinkedList):
			if len(other) != len(self):
				print("Cannot iteratively add vectors of different lengths")
			else:
				for node in range(0, len(self)):
					self[node] += other[node]
		else:
			print("Cannot iteratively add type " + str(type(other)))
		return self

	def madd(self, other):
		if isinstance(other, int) or isinstance(other, float):
			self.__add__(other)
		if isinstance(other, list):
			other = DLinkedList(other)
		if isinstance(other, DLinkedList):
			if len(self) % len(other) != 0:
				print("Error: Cannot add vectors/matrices of different lengths")
			elif len(other) == 1:
				self + other[0]
			else:
				currentnode = self.head
				for node in range(0, self.count):
					currentnode.data += other[node]
					currentnode = currentnode.next

	def __sub__(self, other):
		if isinstance(other, float) or isinstance(other, int):
			for node in range(0, self.count):
				if isinstance(self[node], DLinkedList) or isinstance(self[node], list):
					self[node] - other
				else:
					self[node] = self[node] - other
		else:
			print("Cannot subtract ", str(type(other)), "from DLinkedList")
		return self

	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			currentnode = self.head
			for node in range(0, self.count):
				if isinstance(currentnode.data, DLinkedList):
					currentnode.data * other
				else:
					currentnode.data = currentnode.data * other
				currentnode = currentnode.next
		else:
			print("Cannot multiply DLinkedList with " + str(type(other)))

	def __rmul__(self, other):
		self.__mul__(other)

	def __truediv__(self, other):
		if isinstance(other, float) or isinstance(other, int):
			currentnode = self.head
			for node in range(0, self.count):
				if isinstance(currentnode.data, DLinkedList):
					currentnode.data = currentnode.data / other
				else:
					currentnode.data = currentnode.data / other
				currentnode = currentnode.next
		else:
			print("Cannot divide DLinkedList with ", str(type(other)))
		return self

	def append(self, value):
		if isinstance(value, list):
			value = DLinkedList(value)
		if isinstance(value, int) or isinstance(value, str) or isinstance(value, float) or isinstance(value, DLinkedList):
			newnode = DNode(value)
			if self.count == 0:
				self.head, self.tail = newnode, newnode
			else:
				newnode.prev = self.tail
				self.tail.next = newnode
				self.tail = newnode
			self.count += 1

	def copy(self):
		return DLinkedList([x for x in self])

	def find(self, value, start=0):
		index = start
		currentnode = self.head
		if start != 0:
			for node in range(0, start):
				currentnode = currentnode.next
		if currentnode.data == value:
			return index
		else:
			while currentnode.data is not value:
				if currentnode.next is None:
					return None
				currentnode = currentnode.next
				index += 1
			return index

	def insert(self, value, index):
		newnode = DNode(value)
		if index == 0:
			newnode.next = self.head
			self.head = newnode
			self.count += 1
		elif index > self.count:
			print("Index out of range")
		elif index == self.count:
			self.append(value)
		elif index == self.count - 1:
			self.count += 1
			self.tail.prev.next = newnode
			newnode.prev = self.tail.prev
			newnode.next = self.tail
			self.tail.prev = newnode
		else:
			currentnode = self.head
			for node in range(0, index):
				currentnode = currentnode.next
			newnode.prev = currentnode.prev
			newnode.next = currentnode
			currentnode.prev = newnode
			self.count += 1

	def remove(self, index):
		if isinstance(index, int):
			if index == 0:
				self.head = self.head.next
				self.head.prev = None
				self.count -= 1
			elif index >= self.count:
				print("Index out of range")
			else:
				currentnode = self.head
				for node in range(0, index):
					currentnode = currentnode.next
				currentnode.prev.next = currentnode.next
				currentnode.next.prev = currentnode.prev
				self.count -= 1
		else:
			print("Index must be an integer")

	def reverse(self):
		for index in range(self.count - 2, -1, -1):
			self.append(self.pop(index))

	def pop(self, index=None):
		if index == None:
			value = self.tail.data
			self.tail.prev.next = None
			self.tail = self.tail.prev
			self.count -= 1
			return value
		elif isinstance(index, int):
			if index >= self.count:
				print('Index out of range')
			elif index == 0:
				val = self.head.data
				self.head = self.head.next
				self.head.prev = None
				self.count -= 1
				return val
			else:
				currentnode = self.head
				for node in range(0, index):
					currentnode = currentnode.next
				val = currentnode.data
				currentnode.prev.next = currentnode.next
				currentnode.next.prev = currentnode.prev
				self.count -= 1
				return val
		else:
			print("Index must be an integer")

	def format(self):
		print(self.__str__(True))

	def repeat(self, n):
		return DLinkedList(n * [x for x in self])

mylist = DLinkedList([[1, 2], [3, 4], [5, 6]])
print(mylist)
mylist.format()
mylist.madd([1, 2, 3])
print(mylist)
