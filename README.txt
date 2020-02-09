TOM'S EXPRESSION TREE CONSTRUCTOR AND EVALUATOR

For this program to run, you must first install python 3.6 which can be found at 
python.org/downloads/release/python-360/

To run this program:
	-1) go to the directory where exptree.py and binarytree.py is installed.
	-2a) for windows systems, click the icon for exptree.py
	-2b) for unix-systems, enter the following command: 
		'python3 exptree.py' 
	-3) follow the prompt, it should say 'enter an infix expression delimited by spaces (integers only):'.

An infix expression delimited by spaces is an arithmetic expression where each operator (+, -, etc.)
or operand (integer) is seperated by spaces. For example:
	5 + 30 - 1
is valid, and it evaluates to 34. However,
	5+30-1
is invalid, and it will produce an error. 

Supported operators:
	^ = exponentiation
	* = multiplication
	/ = division
	+ = addition
	- = subtraction
