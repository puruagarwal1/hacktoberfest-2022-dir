class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class CircularLinkedList:
	def __init__(self):
		self.head = None

	def push(self, data, temp=None):
		if self.head == None:
			node = Node(data)
			self.head = node
			node.next = self.head
			return

		if temp == None:
			temp = self.head

		if temp.next == self.head:
			node = Node(data)
			node.next = self.head
			temp.next = node
			return

		self.push(data, temp.next)

	def traverse(self, temp=None):
		if temp == None:
			temp = self.head

		if temp.next == self.head:
			print(temp.data, end="\n")
			return
		print(temp.data, end="-->")
		self.traverse(temp.next)


if __name__ == "__main__":
	clist = CircularLinkedList()
	clist.push(2)
	clist.push(3)
	clist.push(7)
	clist.push(5)
	print("Traversed Circular Linked List: ", end="\n")
	clist.traverse()

# Code provided by SanketJ29