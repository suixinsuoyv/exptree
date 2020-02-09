# Thomas Sadowski's Expression Tree Software
import binarytree as bt
# checks if a string is a number
def isnum(c):
	for i in c:
		if not (i >= '0' and i <= '9'):
			return False
	return True
# checks if string is an operator
def isop(c):
	ops = {"+", "-", "*", "/", "^", "coffee"}
	if c not in ops:
		return False
	return True
# returns precedence of operator
def prec(c):
	if c == "-" or c == "+":
		return 1
	if c == "*" or c == "/":
		return 2
	if c == "^" or c == "coffee":
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
		elif isnum(i):
			post.append(i)
		else:
			raise Exception("There are either invalid characters or improper spacing... ")
	while not (len(stack)-1) == 0:
		post.append(stack.pop())
	return post
# builds the expression tree out of nodes of class Node
def exptree(exp):
	stack = list()
	for i in exp:
		n = bt.Node(i)
		if isnum(i):
			stack.append(n)
		else:
			n.right = stack.pop()
			n.right.place = "right"
			n.left = stack.pop()
			n.left.place = "left"
			n.alti = max(n.right.alti, n.left.alti) + 1
			bt.setbranchwidths(n)
			stack.append(n)
	return stack.pop()	
# evaluates a postfix expression
def evaluate(exp):
	stack = list()
	for i in exp:
		if i == "coffee":
			return ":D"
		if isnum(i):
			i = int(i)
			stack.append(i)
		else:
			b = stack.pop()
			a = stack.pop()
			stack.append(operate(a, b, i))
	return stack.pop()
# performs an operation on two operands
def operate(a, b, op):
	if op == "^":
		return a**b 
	if op == "*":
		return a*b
	if op == "/":
		return a//b
	if op == "+":
		return a+b
	if op == "-":
		return a-b
	else:
		return 1
# main 
if __name__ == "__main__":
	print("Enter an infix expression delimited by spaces (integers only). ")
	exp = input()
	exp = exp.split()
	exp = intopost(exp)
	n = exptree(exp)	
	
	print("Expression tree: ")
	bt.drawtree(n)
	print("Pre-order traversal / prefix / polish notation: ")
	bt.preorder(n)
	print("\nPost-order traversal / postfix / reverse polish notation: ")
	bt.postorder(n)
	print("\nIn-order traversal / infix notation: ")
	bt.inorder(n)
	print("\nEvaluation of expression: ")
	print(evaluate(exp))

