# Thomas Sadowski
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
	__slots__ = ['left', 'right', 'data', 'alti']
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		# alti = altitude--however, it is only useful for denoting the height of the tree 
		# which is found at the root node
		self.alti = 0 
# builds the expression tree out of nodes of class Node
def exptree(exp):
	stack = list()
	for i in exp:
		n = Node(i)
		if isdi(i):
			stack.append(n)
		else:
			r = stack.pop()
			n.right = r
			l = stack.pop()
			n.left = l
			n.alti = max(r.alti, l.alti) + 1
			stack.append(n)
	return stack.pop()	
# performs a level-order traversal on the tree
def levelorder(tree):
	for i in range(0, tree.alti + 1):
		printlevel(tree, i)
		print()
# helper for levelorder
def printlevel(tree, level):
	if tree is None:
		return
	if level == 0:
		print(tree.data, end=" ")
	else:
		printlevel(tree.left, level - 1)
		printlevel(tree.right, level -1)
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
	levelorder(n)
	print("Pre-order traversal / prefix / polish notation: ")
	preorder(n)
	print("\nPost-order traversal / postfix / reverse polish notation: ")
	postorder(n)
	print("\nIn-order traversal / infix notation: ")
	inorder(n)
	print("\nEvaluation of expression: ")
	print(evaluate(exp))
	

