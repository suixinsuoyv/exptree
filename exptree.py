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
	__slots__ = ['left', 'right', 'data', 'leftsh', 'leftsp', 'rightsh', 'rightsp', 'size', 'alti']
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
			n.left = stack.pop()
			n.alti = max(n.right.alti, n.left.alti) + 1
			setbranchwidths(n)
			stack.append(n)
	return stack.pop()	

# performs a level-order traversal on the tree
def listoflevels(tree):
	levels = list()
	for i in range(0, tree.alti + 1):
		level = list()
		getlevel(tree, i, level)
		levels.append(level)
	return levels
# helper for levelorder
def getlevel(tree, i, level):
	if tree is None:
		return
	if i == 0:
		level.append(tree)
	else:
		getlevel(tree.left, i - 1, level)
		getlevel(tree.right, i - 1, level)
# outputs the tree
def treetostr(treelist):
	treestr = ""
	for i in range(0, len(treelist)):
		levelstr = ""
		arms = ""
		for j in treelist[i]:
			#if isop(j.data):
			levelstr += " " * j.leftsp + "_" * j.leftsh
			levelstr += j.data
			levelstr += "_" * j.rightsh + " " * (j.rightsp + 1)
			arm = ""
			if isop(j.data): 
				arms += " " * j.leftsp + "|" + " " * j.leftsh
				arms += " " * (j.rightsh - 1) + "|" + " " * (j.rightsp + 1)
			else:
				arms += " " * j.leftsp + " " * j.size + " " * j.leftsh
				arms += " " * (j.rightsh - 1) + " " * (j.rightsp + 1)
		treestr += levelstr + "\n"
		treestr += arms + "\n"
	return treestr
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
		print(tree.data, end=" ")

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
	print(treetostr(listoflevels(n)))
	print("Pre-order traversal / prefix / polish notation: ")
	preorder(n)
	print("\nPost-order traversal / postfix / reverse polish notation: ")
	postorder(n)
	print("\nIn-order traversal / infix notation: ")
	inorder(n)
	print("\nEvaluation of expression: ")
	print(evaluate(exp))
	

