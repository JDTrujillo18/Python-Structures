class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class SLIterator:
	def __init__(self, SLList):
		self._cur = SLList.head

	def __next__(self):
		if self._cur is None:
			raise StopIteration
		else:
			val = self._cur.data
			self._cur = self._cur.next
			return val


class SLinkedList:
	def __init__(self, data=None):
		self.head = None
		self.tail = None
		self.count = 0
		if data:
			if isinstance(data, int) or isinstance(data, float):
				self.append(data)
			elif isinstance(data, list) or isinstance(data, SLinkedList):
				for value in data:
					self.append(value)
			else:
				print("Invalid input")

	def __len__(self):
		return self.count

	def __iter__(self):
		return SLIterator(self)

	def __getitem__(self, item):
		if isinstance(item, int):
			if item == 0:
				return self.head.data
			elif item == self.count - 1:
				return self.tail.data
			elif item < self.count - 1:
				currentnode = self.head
				for node in range(0, item):
					currentnode = currentnode.next
				return currentnode.data
		elif isinstance(item, slice):
			return SLinkedList([self[x] for x in range(*item.indices(len(self)))])
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
				print("Error: No item at index exists")
		elif isinstance(key, slice):
			if len([x for x in range(*key.indices(len(self)))]) != len(value):
				print('Indices out of range')
			else:
				count = 0
				for x in range(*key.indices(len(self))):
					self[x] = value[count]
					count += 1
		else:
			print("Key must be a slice or an index")

	def __add__(self, other):
		if isinstance(other, SLinkedList) or isinstance(other, list):
			datalist = []
			for item in self:
				datalist.extend([item])
			for item in other:
				datalist.extend([item])
			return SLinkedList(datalist)
		elif isinstance(other, int) or isinstance(other, float):
			return self.__iadd__(other)
		else:
			print('Cannot add type SLinkedList and ' + str(type(other)))

	def __radd__(self, other):
		return self.__add__(other)

	def __iadd__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			currentnode = self.head
			for node in range(0, self.count):
				currentnode.data += other
				currentnode = currentnode.next
		elif isinstance(other, SLinkedList):
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
			other = SLinkedList(other)
		if isinstance(other, SLinkedList):
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
				if isinstance(self[node], SLinkedList) or isinstance(self[node], list):
					self[node] - other
				else:
					self[node] = self[node] - other
		else:
			print("Cannot subtract ", str(type(other)), "from SLinkedList")
		return self

	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			currentnode = self.head
			for node in range(0, self.count):
				if isinstance(currentnode.data, SLinkedList):
					currentnode.data * other
				else:
					currentnode.data = currentnode.data * other
				currentnode = currentnode.next
		else:
			print("Cannot multiple SLLinkedList with " + str(type(other)))

	def __rmul__(self, other):
		self.__mul__(other)

	def __truediv__(self, other):
		if isinstance(other, float) or isinstance(other, int):
			currentnode = self.head
			for node in range(0, self.count):
				if isinstance(currentnode.data, SLinkedList):
					currentnode.data = currentnode.data / other
				else:
					currentnode.data = currentnode.data / other
				currentnode = currentnode.next
		else:
			print("Cannot divide SLinkedList with ", str(type(other)))
		return self

	def __str__(self, arrows=False):
		if self.count == 0:
			print("Linked List is empty")
		else:
			currentnode = self.head
			nodelist = []
			for node in range(0, self.count):
				nodelist.extend([str(currentnode.data)])
				currentnode = currentnode.next
			if not arrows:
				return '[' + ', '.join(nodelist) + ']'
			else:
				mystr = '\nSingly Linked List: \nLength: ' + str(self.count) + '\nHead: ' + str(self.head.data) + '\n'
				for node in range(0, len(nodelist) - 1):
					mystr += '    ' + nodelist[node] + ' -> ' + nodelist[node + 1] + '\n'
				mystr += 'Tail: ' + str(self.tail.data) + '\n'
				return mystr

	def append(self, data):
		if isinstance(data, list):
			data = SLinkedList(data)
		if isinstance(data, int) or isinstance(data, float) or isinstance(self, SLinkedList):
			newnode = Node(data)
			if self.count == 0:
				self.head = newnode
				self.tail = newnode
			else:
				self.tail.next = newnode
				self.tail = newnode
			self.count += 1

	def copy(self):
		return SLinkedList([x for x in self])

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
		newnode = Node(value)
		if index == 0:
			newnode.next = self.head
			self.head = newnode
			self.count += 1
		elif index >= self.count:
			print("Index out of range")
		else:
			currentnode = self.head
			previousnode = None
			for node in range(0, index):
				previousnode = currentnode
				currentnode = currentnode.next
			previousnode.next = newnode
			newnode.next = currentnode
			self.count += 1

	def remove(self, index):
		if index == 0:
			currentnode = self.head
			currentnode = currentnode.next
			self.head = currentnode
			self.count -= 1
		elif index >= self.count:
			print("Index out of range")
		else:
			currentnode = self.head
			previousnode = None
			for node in range(0, index):
				previousnode = currentnode
				currentnode = currentnode.next
			if index == self.count - 1:
				previousnode.next = None
				self.tail = previousnode
			else:
				previousnode.next = currentnode.next
			self.count -= 1

	def reverse(self):
		currentnode = self.head
		previous = None
		while currentnode:
			next = currentnode.next
			currentnode.next = previous
			previous = currentnode
			currentnode = next
			self.head = previous

	def pop(self, index=None):
		if index is None:
			previousnode = None
			currentnode = self.head
			for node in range(0, self.count - 1):
				previousnode = currentnode
				currentnode = currentnode.next
			value = currentnode.data
			previousnode.next = None
			self.tail = previousnode
			self.count -= 1
		else:
			value = self[index]
			self.remove(index)
		return value

	def format(self):
		print(self.__str__(True))

	def repeat(self, n):
		return SLinkedList(n * [x for x in self])

mylist = SLinkedList([[1, 2], [3, 4]])
print(mylist)
mylist.madd([1, 2])
print(mylist)
mylist.format()
