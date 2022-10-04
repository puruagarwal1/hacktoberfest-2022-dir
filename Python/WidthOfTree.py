class Node:
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

maxx = 0

hm_min = {}
hm_max = {}

def getMaxWidthHelper(node, lvl, i):
	if (node == None):
		return
	if (lvl in hm_max):
		hm_max[lvl] = max(i, hm_max[lvl])
	else:
		hm_max[lvl] = i

	if (lvl in hm_min):
		hm_min[lvl] = min(i, hm_min[lvl])

	else:
		hm_min[lvl] = i

	getMaxWidthHelper(node.left, lvl + 1, 2 * i + 1)

	getMaxWidthHelper(node.right, lvl + 1, 2 * i + 2)

def getMaxWidth(root):
	global maxx
	getMaxWidthHelper(root, 0, 0)

	for lvl in hm_max.keys():
		maxx = max(maxx, hm_max[lvl] - hm_min[lvl] + 1)

	return maxx
	
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

print(getMaxWidth(root))

