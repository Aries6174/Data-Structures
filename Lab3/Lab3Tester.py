# WARNING: DO NOT EDIT THE CONTENTS OF THIS FILE UNLESS PROMPTED TO DO SO
# LABORATORY EXERCISE NO. 3 TESTER

import random

# Array Queue Tester
def ArrayQueueTest():
	import ArrayQueue

	score = 0
	TOTAL = 50
	testArray = ArrayQueue.ArrayQueue()
	
	# Initial Test for 'size'
	try:
		if testArray.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing Array Queue")

	randNums = []
	try:
		# Initial Test for 'enqueue()'
		for i in range(10):
			randNums.append(random.random())
			testArray.enqueue(randNums[i])
			score+=1

		# Size Test
		if testArray.getSize() == 10:
			score+=1
	except:
		print("Error: enqueue() not working properly")

	try:
		for i in range(testArray.getSize()):
			if testArray.contents[i].getValue() == randNums[i]:
				score+=1
	except:
		print("Error: ArrayQueue values do not match enqeueued elements' values")

	# Capacity Test
	testCapacity = testArray.getCapacity()
	if (testArray.getSize() == testCapacity):
		try:
			testArray.enqueue(random.random())
			print("Error: enqueue() still working even if array is full")
		except:
			score+=3
			testArray.expand()

	# Initial Test for 'dequeue()'
	try:
		for i in range(10):
			prevSize = testArray.getSize()
			removed = testArray.dequeue()
			front = testArray.front()
			if removed.getValue() != front.getValue():
				score+=0.5
			if testArray.getSize() == (prevSize - 1):
				score+=0.5
			if removed.getValue() == randNums[i]:
				score+=1
	except:
		print("Error: dequeue() not working properly")

	# Empty Stack Test
	if testArray.isEmpty():
		score+=2
		try:
			testArray.dequeue()
			print("Error: dequeue() still working even if array is empty")
		except:
			score+=3

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# SLL Queue Tester
def SLLQueueTest():
	import SLLQueue

	score = 0
	TOTAL = 50
	testSLL = SLLQueue.SLLQueue()
	
	try:
		if testSLL.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing SLL Queue")

	randNums1 = []
	try:
		for i in range(10):
			randNums1.append(random.random())
			testSLL.enqueue(randNums1[i])
		
		if testSLL.getSize() == 10:
			score+=2

		i = 0
		current = testSLL.front()
		while current:
			if current.getValue() == randNums1[i]:
				score+=1
				current = current.getNext()
				i+=1
	except:
		print("Error: enqueue() not working properly")
	
	try:
		for i in range(10):
			prevSize = testSLL.getSize()
			removed = testSLL.dequeue()
			front = testSLL.front()
			if testSLL.getSize() == (prevSize - 1):
				score+=0.5
			if front.getValue() != removed.getValue():
				score+=1.5
			if removed.getValue() == randNums1[i]:
				score+=1
	except:
		print("Error: dequeue() not working properly")
	
	# Empty SLL Test
	try:
		if testSLL.isEmpty():
			score+=1
		if (testSLL.front().getValue() == None):
			score+=2
	except:
		print("Error: dequeue() not working properly [does not empty SLL]")
	try:
		testSLL.dequeue()
		print("Error: dequeue() still working even if SLL is empty")
	except:
		score+=3

	# Return Value Test
	try:
		rand = random.random()
		testSLL.enqueue(rand)
		x = testSLL.dequeue()
		testSLL.enqueue(x.getValue())
		if testSLL.front().getValue() == rand:
			score+=1
	except:
		print("Error: front(), enqueue(), or dequeue() not working after SLL became empty")

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# User Choice Prompt
def main():
	print("LABORATORY EXERCISE #3 TESTER\nOptions:\n1 - Array Queue\n2 - SLL Queue\n* - Exit")
	choice = int(input("Choice: "))
	if choice == 1:
		ArrayQueueTest()
	elif choice == 2:
		SLLQueueTest()
	else:
		exit()

main()