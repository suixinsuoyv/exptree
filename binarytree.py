# Methods and structures for a binary tree

# conventional node for a binary tree, with extra variables for building a string representation of the tree
class Node:
	__slots__ = ['left', 'right', 'data', 'leftsh', 'leftsp', 'rightsh', 'rightsp', 'size', 'alti', 'place']
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = str(data)
		# widths of the left and right shoulders, and left and right spaces
		self.leftsh = 0
		self.leftsp = 0
		self.rightsh = 0
		self.rightsp = 0
		self.size = len(self.data)
		# alti = altitude of the node relative to its lowest subtree
		self.alti = 0 
		# values can be empty string, "left", or "right" depending on where the node is relative to its parent
		self.place = ""
# sets values to be used for drawing the tree
def setbranchwidths(n):
	if n.left is not None and n.right is not None:
		n.leftsh = n.left.rightsh + n.left.rightsp + n.left.size
		n.leftsp = n.left.leftsh + n.left.leftsp
		n.rightsh = n.right.leftsh + n.right.leftsp + n.right.size
		n.rightsp = n.right.rightsh + n.right.rightsp
# draws tree by calling recursive method "drawtr"
def drawtree(root):
	row = 2*root.alti + 1
	col = root.leftsp + root.leftsh + root.size + root.rightsh + root.rightsp
	matrix = [[" "]*col for x in range(row)]
	drawtr(root, matrix, 0, root.leftsp + root.leftsh)
	for i in matrix:
		print("\t", end="")
		for j in i:
			print(j, end="")
		print()
# recursively draws tree
def drawtr(node, matrix, i, j):
	if node == None:
		return
	if node.place == "right":
		j1 = j
		while j1 > j - node.size:
			matrix[i][j1] = node.data[j1 - j + node.size - 1]
			j1 -= 1
		while j1 > j - node.size - node.leftsh:
			matrix[i][j1] = "_"
			if j1 == j - node.size - node.leftsh + 1:
				matrix[i+1][j1] = "|"
			j1 -= 1
		drawtr(node.left, matrix, i + 2, j1 + 1)
		j2 = j + 1
		while j2 <= j + node.rightsh:
			matrix[i][j2] = "_"
			if j2 == j + node.rightsh:
				matrix[i+1][j2] = "|"
			j2 += 1
		drawtr(node.right, matrix, i + 2, j2 - 1)
	else:
		j1 = j
		while j1 < j + node.size:
			matrix[i][j1] = node.data[j1 - j]
			j1 += 1
		while j1 < j + node.size + node.rightsh:
			matrix[i][j1] = "_"
			if j1 == j + node.size + node.rightsh - 1:
				matrix[i+1][j1] = "|"
			j1 += 1
		drawtr(node.right, matrix, i + 2, j1 - 1)
		j2 = j - 1
		while j2 >= j - node.leftsh:
			matrix[i][j2] = "_"
			if j2 == j - node.leftsh:
				matrix[i+1][j2] = "|"
			j2 -= 1
		drawtr(node.left, matrix, i + 2, j2 + 1)
# attaches a parent node to its child nodes
def mergetrees(t, r, l):
	t.right = r
	t.right.place = "right"
	t.left = l
	t.left.place = "left"
	t.alti = max(t.right.alti, t.left.alti) + 1
	setbranchwidths(t)
# performs an in-order traversal on the tree
def inorder(tree):
	l = list()
	inord(tree, l)
	return l
# helper for inorder
def inord(tree, l):
	if tree is not None:
		inord(tree.left, l)
		l.append(tree.data)
		inord(tree.right, l)
# performs a pre-order traversal on the tree
def preorder(tree):
	l = list()
	preord(tree, l)
	return l
# helper for preorder
def preord(tree, l):
	if tree is not None:
		l.append(tree.data)
		preord(tree.left, l)
		preord(tree.right, l)
# performs a post-order traversal on the tree
def postorder(tree):
	l = list()
	postord(tree, l)
	return l
# helper for postorder
def postord(tree, l):
	if tree is not None:
		postord(tree.left, l)
		postord(tree.right, l)
		l.append(tree.data)
