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
# uses an infix expression to build an expression tree 
def exptree(exp):
	nums = list()
	ops = list()
	bottom = bt.Node("!")
	ops.append(bottom)
	for i in exp:
		n = bt.Node(i)
		if isnum(i):
			nums.append(n)
		else:
			while prec(i) <= prec(ops[len(ops)-1].data):
				t = ops.pop()
				bt.mergetrees(t, nums.pop(), nums.pop())
				nums.append(t)
			ops.append(n)
	while len(ops) > 1:
		t = ops.pop()
		bt.mergetrees(t, nums.pop(), nums.pop())
		nums.append(t)
	return nums.pop()	
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
	n = exptree(exp)	
	
	print("Expression tree: ")
	bt.drawtree(n)
	print("Pre-order traversal / prefix / polish notation: ")
	for i in bt.preorder(n):
		print(i, end=" ")
	print("\nPost-order traversal / postfix / reverse polish notation: ")
	exp = bt.postorder(n)
	for i in exp:
		print(i, end=" ")
	print("\nIn-order traversal / infix notation: ")
	for i in bt.inorder(n):
		print(i, end=" ")
	print("\nEvaluation of expression: ")
	print(evaluate(exp))

