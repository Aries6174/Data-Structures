# WARNING: DO NOT EDIT THE CONTENTS OF THIS FILE UNLESS PROMPTED TO DO SO
# LABORATORY EXERCISE NO. 1 TESTER

import random

# Array Tester
def ArrayTest():
	import Array

	score = 0
	TOTAL = 30
	testArray = Array.Array()
	
	if testArray.isEmpty():
		score+=2

	randNums = []
	for i in range(5):
		randNums.append(random.random())
		testArray.addElement(randNums[i])

	if testArray.size == 5:
		score+=2

	for i in range(testArray.size):
		if testArray.contents[i].getValue() == randNums[i]:
			score+=1

	randNums = []
	for i in range(5):
		randNums.append(random.random())
		testArray.contents[i].setValue(randNums[i])

	for i in range(testArray.size):
		if testArray.contents[i].getValue() == randNums[i]:
			score+=2

	for i in range(testArray.size):
		if testArray.contents[i].index == i:
			score+=1

	for i in range(2):
		prevSize = testArray.size
		testArray.removeElement(0)
		if testArray.contents[0].getValue() == randNums[1]:
			score+=2
		if testArray.size == (prevSize - 1):
			score+=1

	for i in range(3):
		testArray.removeElement(0)

	if testArray.isEmpty():
		score+=2

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# SLL Tester
def SLLTest():
	import SLL

	score = 0
	TOTAL = 35
	testSLL = SLL.SLL()
	
	if testSLL.isEmpty():
		score+=2
	if (testSLL.first.getValue() == None):
		score+=2
	if (testSLL.last.getValue() == None):
		score+=2

	randNums1 = []
	for i in range(5):
		randNums1.append(random.random())
		testSLL.addNode(randNums1[i])
	
	if testSLL.size == 5:
		score+=2

	i = 0
	current = testSLL.first
	while current:
		if current.getValue() == randNums1[i]:
			score+=1
			current = current.getNext()
			i+=1

	i = 0
	randNums1 = []
	current = testSLL.first

	while current:
		randNums1.append(random.random())
		current.setValue(randNums1[i])
		current = current.getNext()
		i+=1

	i = 0
	current = testSLL.first
	while current:
		if current.getValue() == randNums1[i]:
			score+=2
			current = current.getNext()
			i+=1
	
	for i in range(2):
		prevSize = testSLL.size
		testSLL.removeNode(randNums1[i])
		if testSLL.first.getValue() != randNums1[i]:
			score+=2
		if testSLL.size == (prevSize - 1):
			score+=1

	for i in range(3):
		testSLL.removeNode(randNums1[i + 2])
	
	if testSLL.isEmpty():
		score+=2
	if (testSLL.first.getValue() == None):
		score+=2
	if (testSLL.last.getValue() == None):
		score+=2

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# DLL Tester
def DLLTest():
	import DLL

	score = 0
	TOTAL = 35
	testDLL = DLL.DLL()
	
	if testDLL.isEmpty():
		score+=1
	if (testDLL.first.getValue() == None):
		score+=1
	if (testDLL.last.getValue() == None):
		score+=1

	randNums2 = []
	for i in range(5):
		randNums2.append(random.random())
		testDLL.addNode(randNums2[i])

	if testDLL.size == 5:
		score+=1

	i = 0
	current = testDLL.first
	while current:
		if current.getValue() == randNums2[i]:
			score+=1
			current = current.getNext()
			i+=1

	i = testDLL.size - 1
	current = testDLL.last
	while current:
		if current.getValue() == randNums2[i]:
			score+=1
			current = current.getPrev()
			i-=1

	i = 0
	randNums2 = []
	current = testDLL.first
	while current:
		randNums2.append(random.random())
		current.setValue(randNums2[i])
		current = current.getNext()
		i+=1

	i = 0
	current = testDLL.first
	while current:
		if current.getValue() == randNums2[i]:
			score+=2
			current = current.getNext()
			i+=1

	for i in range(2):
		prevSize = testDLL.size
		toRemove = testDLL.first
		testDLL.removeNode(toRemove.getValue())
		if testDLL.first.getValue() != toRemove.getValue():
			score+=2
		if toRemove.getNext().getValue() == None:
			score+=1
		if testDLL.size == (prevSize - 1):
			score+=1

	for i in range(3):
		testDLL.removeNode(randNums2[i + 2])

	if testDLL.isEmpty():
		score+=1
	if (testDLL.first.getValue() == None):
		score+=1
	if (testDLL.last.getValue() == None):
		score+=1

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# User Choice Prompt
def main():
	print("LABORATORY EXERCISE #1 TESTER\nOptions:\n1 - Array\n2 - Singly Linked List\n3 - Doubly Linked List\n* - Exit")
	choice = int(input("Choice: "))
	if choice == 1:
		ArrayTest()
	elif choice == 2:
		SLLTest()
	elif choice == 3:
		DLLTest()
	else:
		exit()

main()