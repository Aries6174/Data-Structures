# WARNING: DO NOT EDIT THE CONTENTS OF THIS FILE UNLESS PROMPTED TO DO SO
# LABORATORY EXERCISE NO. 2 TESTER

import random

# ArrayStack Tester
def ArrayStackTest():
	import ArrayStack

	score = 0
	TOTAL = 50
	testArray = ArrayStack.ArrayStack()
	
	# Initial Test for 'size'
	try:
		if testArray.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing stack")

	randNums = []
	try:
		# Initial Test for 'push()'
		for i in range(10):
			randNums.append(random.random())
			testArray.push(randNums[i])
			score+=1

		# Size Test
		if testArray.size == 10:
			score+=1
	except:
		print("Error: push() not working properly")

	try:
		for i in range(testArray.size):
			if testArray.contents[i].getValue() == randNums[i]:
				score+=1
	except:
		print("Error: ArrayStack values do not match pushed elements' values")

	# Capacity Test
	testCapacity = testArray.getCapacity()
	if (testArray.size == testCapacity):
		try:
			testArray.push(random.random())
			print("Error: push() still working even if array is full")
		except:
			score+=3

	# Initial Test for 'pop()'
	try:
		for i in range(10):
			prevSize = testArray.size
			removed = testArray.pop()
			if testArray.size == (prevSize - 1):
				score+=0.5
			if removed.getValue() == randNums[10-(i+1)]:
				score+=1.5
	except:
		print("Error: pop() not working properly")

	# Empty Stack Test
	if testArray.isEmpty():
		score+=2
		try:
			testArray.pop()
			print("Error: pop() still working even if array is empty")
		except:
			score+=3

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# SLL Stack Tester
def SLLStackTest():
	import SLLStack

	score = 0
	TOTAL = 50
	testSLL = SLLStack.SLLStack()
	
	try:
		if testSLL.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing stack")

	randNums1 = []
	try:
		for i in range(10):
			randNums1.append(random.random())
			testSLL.push(randNums1[i])
		
		if testSLL.size == 10:
			score+=2

		i = 0
		current = testSLL.top()
		while current:
			if current.getValue() == randNums1[10-(i+1)]:
				score+=1
				current = current.getNext()
				i+=1
	except:
		print("Error: push() not working properly")
	
	try:
		for i in range(10):
			removed = testSLL.pop()
			top = testSLL.top()

			if top.getValue() != removed.getValue():
				score+=2
			if removed.getValue() == randNums1[10-(i+1)]:
				score+=1
	except:
		print("Error: pop() not working properly")
	
	# Empty SLL Test
	try:
		if testSLL.isEmpty():
			score+=1
		if (testSLL.top().getValue() == None):
			score+=2
	except:
		print("Error: pop() not working properly [does not empty SLL]")
	try:
		testSLL.pop()
		print("Error: pop() still working even if SLL is empty")
	except:
		score+=3

	# Return Value Test
	try:
		rand = random.random()
		testSLL.push(rand)
		x = testSLL.pop()
		testSLL.push(x.getValue())
		if testSLL.top().getValue() == rand:
			score+=1
	except:
		print("Error: top(), push(), or pop() not working after SLL became empty")

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# User Choice Prompt
def main():
	print("LABORATORY EXERCISE #2 TESTER\nOptions:\n1 - Array Stack\n2 - SLL Stack\n* - Exit")
	choice = int(input("Choice: "))
	if choice == 1:
		ArrayStackTest()
	elif choice == 2:
		SLLStackTest()
	else:
		exit()

main()