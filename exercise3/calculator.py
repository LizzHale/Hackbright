from arithmetic import *

flag = True

while flag:
	start = raw_input("> ")
	
	if start == "end":
		flag = False
	else:
		token = start.split(" ")
		operator = token[0]

		if operator == "+":
			print add(int(token[1]) , int(token[2]))

		elif operator == "-":
			print subtract(int(token[1]) , int(token[2]))

		elif operator == "*":
			print multiply(int(token[1]) , int(token[2]))

		elif operator == "/":
			print divide(int(token[1]) , int(token[2]))

		elif operator == "square":
			print square(int(token[1]))

		elif operator == "cube":
			print cube(int(token[1]))

		elif operator == "pow":
			print power(int(token[1]) , int(token[2]))

		elif operator == "mod":
			print mod(int(token[1]) , int(token[2]))

		else:
			print "I do not understand."

