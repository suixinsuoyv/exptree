# Thomas Sadowski's Expression Tree Software

# checks if a string is a digit
def isdi(c):
	for i in c:
		if not (i >= '0' and i <= '9'):
			return False
	return True
# checks if string is an operator
def isop(c):
	ops = {'+', '-', '*', '/', '^'}
	if len(c) > 1 or c[0] not in ops:
		return False
	return True;
# returns precedence of operator
def prec(c):
	if c == '-' or c == '+':
		return 1
	if c == '*' or c == '/':
		return 2
	if c == '^':
		return 3
	else:
		return 0
# converts infix expression to postfix expression
def intopost(exp):
	stack = list()
	post = list()
	stack.append('!')
	for i in exp:
		if isop(i):
			while prec(i) <= prec(stack[len(stack)-1]):	
				post.append(stack.pop())
			stack.append(i)
		elif isdi(i):
			post.append(i)
		else:
			raise Exception("There are either invalid characters or improper spacing... ")
	while not (len(stack)-1) == 0:
		post.append(stack.pop())
	return post
# conventional node for a binary tree, with one extra variable
class Node:
	__slots__ = ['left', 'right', 'data', 'leftsh', 'leftsp', 'rightsh', 'rightsp', 'size', 'alti', 'place']
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = str(data)
		self.leftsh = 0
		self.leftsp = 0
		self.rightsh = 0
		self.rightsp = 0
		self.size = len(self.data)
		# alti = altitude of the node relative to its lowest subtree
		self.alti = 0 
		self.place = ""
# sets values to be used for printing the tree
def setbranchwidths(n):
	n.leftsh = n.left.rightsh + n.left.rightsp + n.left.size
	n.leftsp = n.left.leftsh + n.left.leftsp
	n.rightsh = n.right.leftsh + n.right.leftsp + n.right.size
	n.rightsp = n.right.rightsh + n.right.rightsp
# builds the expression tree out of nodes of class Node
def exptree(exp):
	stack = list()
	for i in exp:
		n = Node(i)
		if isdi(i):
			stack.append(n)
		else:
			n.right = stack.pop()
			n.right.place = "right"
			n.left = stack.pop()
			n.left.place = "left"
			n.alti = max(n.right.alti, n.left.alti) + 1
			setbranchwidths(n)
			stack.append(n)
	return stack.pop()	
# draws tree
def drawtree(root):
	row = 2*root.alti + 1
	col = root.leftsp + root.leftsh + root.size + root.rightsh + root.rightsp
	print(row, col)
	matrix = [[" "]*col for i in range(row)]
	j = root.leftsp + root.leftsh
	drawtr(root, matrix, 0, j)
	for i in matrix:
		for j in i:
			print(j, end="")
		print()
# draws tree for real
def drawtr(node, matrix, i, j):
	if node == None:
		return
	if node.place == "right":
		j1 = j
		while j1 > j - node.size:
			print(i, j1, node.data[j1 - j + node.size - 1])
			matrix[i][j1] = node.data[j1 - j + node.size - 1]
			j1 -= 1
		while j1 > j - node.size - node.leftsh:
			print(i, j1, "_")
			matrix[i][j1] = "_"
			if j1 == j - node.size - node.leftsh + 1:
				print(i+1, j1, "|")
				matrix[i+1][j1] = "|"
			j1 -= 1
		drawtr(node.left, matrix, i + 2, j1 + 1)
		j2 = j + 1
		while j2 <= j + node.rightsh:
			print(i, j2, "_")
			matrix[i][j2] = "_"
			if j2 == j + node.rightsh:
				print(i+1, j2, "|")
				matrix[i+1][j2] = "|"
			j2 += 1
		drawtr(node.right, matrix, i + 2, j2 - 1)
	else:
		j1 = j
		while j1 < j + node.size:
			print(i, j1, node.data[j1 - j])
			matrix[i][j1] = node.data[j1 - j]
			j1 += 1
		while j1 < j + node.size + node.rightsh:
			print(i, j1, "_")
			matrix[i][j1] = "_"
			if j1 == j + node.size + node.rightsh - 1:
				print(i+1, j1, "|")
				matrix[i+1][j1] = "|"
			j1 += 1
		drawtr(node.right, matrix, i + 2, j1 - 1)
		j2 = j - 1
		while j2 >= j - node.leftsh:
			print(i, j2, "_")
			matrix[i][j2] = "_"
			if j2 == j - node.leftsh:
				print(i+1, j2, "|")
				matrix[i+1][j2] = "|"
			j2 -= 1
		drawtr(node.left, matrix, i + 2, j2 + 1)
# performs an in-order traversal on the tree
def inorder(tree):
	if tree is not None:
		inorder(tree.left)
		print(tree.data, end=" ")
		inorder(tree.right)
# performs a pre-order traversal on the tree
def preorder(tree):
	if tree is not None:
		print(tree.data, end=" ")
		preorder(tree.left)
		preorder(tree.right)
# performs a post-order traversal on the tree
def postorder(tree):
	if tree is not None:
		postorder(tree.left)
		postorder(tree.right)
		print(tree.data, tree.place ,end=" ")

def evaluate(exp):
	stack = list()
	for i in exp:
		if isdi(i):
			i = int(i)
			stack.append(i)
		else:
			b = stack.pop()
			a = stack.pop()
			stack.append(operate(a, b, i))
	return stack.pop()

def operate(a, b, op):
	if op == '^':
		return a**b 
	if op == '*':
		return a*b
	if op == '/':
		return a//b
	if op == '+':
		return a+b
	else:
		return a-b
# main 
if __name__ == "__main__":
	print("Enter an infix expression delimited by spaces (integers only). ")
	exp = input()
	exp = exp.split()
	exp = intopost(exp)
	n = exptree(exp)	
	
	print("Expression tree: ")
	drawtree(n)
	print("Pre-order traversal / prefix / polish notation: ")
	preorder(n)
	print("\nPost-order traversal / postfix / reverse polish notation: ")
	postorder(n)
	print("\nIn-order traversal / infix notation: ")
	inorder(n)
	print("\nEvaluation of expression: ")
	print(evaluate(exp))

