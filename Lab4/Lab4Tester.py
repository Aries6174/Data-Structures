# WARNING: DO NOT EDIT THE CONTENTS OF THIS FILE UNLESS PROMPTED TO DO SO
# LABORATORY EXERCISE NO. 4 TESTER
# NOTE: EVEN IF YOUR CODE WORKS IN THE TESTER, IT IS NOT NECESSARILY THE CORRECT IMPLEMENTATION

import random

# Circular Queue Tester
def CircularQueueTest():
	import CircularQueue

	score = 0
	TOTAL = 50
	testArray = CircularQueue.CircularQueue()
	
	# Initial Test for 'CircularQueue'
	try:
		if testArray.isEmpty():
			score+=1
		if (testArray.frontIndex==0):
			score+=1
		if (testArray.rearIndex==0):
			score+=1
	except:
		print("Error: Problem initializing Circular Queue")
		return

	randNums = []
	try:
		# Initial Test for 'enqueue()'
		for i in range(10):
			randNums.append(random.random())
			testArray.enqueue(randNums[i])
			score+=0.5

		# Size Test
		if testArray.getSize() == 10:
			score+=2
	except:
		print("Error: enqueue() not working properly")
		return

	try:
		for i in range(testArray.getSize()):
			if testArray.contents[i].getValue() == randNums[i]:
				score+=0.5
	except:
		print("Error: CircularQueue values do not match enqeueued elements' values")
		return

	# Initial Test for 'dequeue()'
	try:
		for i in range(10):
			prevSize = testArray.getSize()
			prevFront = testArray.frontIndex
			removed = testArray.dequeue()
			front = testArray.front()
			if removed.getValue() != front.getValue():
				score+=0.5
			if removed.getIndex() == prevFront:
				score+=0.5
			if testArray.getSize() == (prevSize - 1):
				score+=0.5
			if removed.getValue() == randNums[i]:
				score+=0.5
	except:
		print("Error: dequeue() not working properly")
		return

	# Empty Queue Test
	if testArray.isEmpty():
		score+=1
		try:
			testArray.dequeue()
			print("Error: dequeue() still working even if array is empty")
			return
		except:
			score+=3

	randNums = []
	try:
		# Trying 'enqueue()' again
		for i in range(10):
			randNums.append(random.random())
			testArray.enqueue(randNums[i])
			score+=0.5

		# Size Test
		if testArray.getSize() == 10:
			score+=1
	except:
		print("Error: enqueue() not working properly")
		return

	try:
		# Compare values again
		start = testArray.frontIndex
		i = 0
		while i < testArray.getSize():
			if testArray.contents[start].getValue() == (randNums[i]):
				score+=0.5
				i+=1
				if start != testArray.getSize():
					start+=1
				else:
					start = 0

	except:
		print("Error: enqueue() not working properly")
		return

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# DLL Deque Tester
def DLLDequeTest():
	import DLLDeque

	score = 0
	TOTAL = 50
	testDLL = DLLDeque.DLLDeque()
	
	try:
		if testDLL.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing DLL Deque")
		return

	randNums1 = []
	try:
		for i in range(5):
			randNums1.append(random.random())
			testDLL.insertFirst(randNums1[i])
		
		if testDLL.getSize() == 5:
			score+=2

		i = 0
		current = testDLL.last()
		while current:
			if current.getValue() == randNums1[i]:
				score+=1
				i+=1
			current = current.getPrev()
	except:
		print("Error: insertFirst() not working properly")
		return

	randNums1 = []
	try:
		for i in range(5):
			randNums1.append(random.random())
			testDLL.insertLast(randNums1[i])
		
		if testDLL.getSize() == 10:
			score+=2

		i = 0
		current = testDLL.first()
		while current:
			if current.getValue() == randNums1[i]:
				score+=1
				i+=1
			current = current.getNext()
	except:
		print("Error: insertLast() not working properly")
		return
	
	try:
		for i in range(5):
			prevSize = testDLL.getSize()
			removed = testDLL.removeFirst()
			front = testDLL.first()
			if testDLL.getSize() == (prevSize - 1):
				score+=0.5
			if front.getValue() != removed.getValue():
				score+=1.5
			if removed.getNext() == None:
				score+=0.5
	except:
		print("Error: removeFirst() not working properly")
		return

	try:
		for i in range(5):
			prevSize = testDLL.getSize()
			removed = testDLL.removeLast()
			last = testDLL.last()
			if testDLL.getSize() == (prevSize - 1):
				score+=0.5
			if last.getValue() != removed.getValue():
				score+=1.5
			if removed.getPrev() == None:
				score+=0.5
	except:
		print("Error: removeLast() not working properly")
		return
	
	# Empty SLL Test
	try:
		if testDLL.isEmpty():
			score+=2
		if (testDLL.first().getValue() == None):
			score+=2
		if (testDLL.last().getValue() == None):
			score+=2

	except:
		print("Error: removeFirst() or removeLast() not working properly [does not empty SLL]")
		return

	try:
		testDLL.removeFirst()
		print("Error: removeFirst() still working even if SLL is empty")
		return
	except:
		score+=2
	try:
		testDLL.removeLast()
		print("Error: removeLast() still working even if SLL is empty")
		return
	except:
		score+=2

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# User Choice Prompt
def main():
	print("LABORATORY EXERCISE #4 TESTER\nOptions:\n1 - Circular Queue\n2 - DLLDeque\n* - Exit")
	choice = int(input("Choice: "))
	if choice == 1:
		CircularQueueTest()
	elif choice == 2:
		DLLDequeTest()
	else:
		exit()

main()