
def isdi(c):
	for i in c:
		if not (i >= '0' and i <= '9'):
			return False
	return True

def isop(c):
	ops = {'+', '-', '*', '/', '^'}
	if len(c) > 1 or c[0] not in ops:
		return False
	return True;

def prec(c):
	if c == '-' or c == '+':
		return 1
	if c == '*' or c == '/':
		return 2
	if c == '^':
		return 3
	else:
		return 0
	
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

class Node:
	__slots__ = ['left', 'right', 'data']
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def exptree(exp):
	stack = list()
	for i in exp:
		n = Node(i)
		if isdi(i):
			stack.append(n)
		else:
			n.right = stack.pop()
			n.left = stack.pop()
			stack.append(n)
	return stack.pop()	

def inorder(tree):
	if tree is not None:
		inorder(tree.left)
		print(tree.data, end=" ")
		inorder(tree.right)

def preorder(tree):
	if tree is not None:
		print(tree.data, end=" ")
		preorder(tree.left)
		preorder(tree.right)

def postorder(tree):
	if tree is not None:
		postorder(tree.left)
		postorder(tree.right)
		print(tree.data, end=" ")

if __name__ == "__main__":
	print("enter the expression in infix notation delimited by spaces. ")
	exp = input()
	exp = exp.split()
	exp = intopost(exp)
	
	n = exptree(exp)	
	inorder(n)
	print()
	preorder(n)
	print()
	postorder(n)
	print()
	print(exp)
	

