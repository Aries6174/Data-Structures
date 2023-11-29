# WARNING: DO NOT EDIT THE CONTENTS OF THIS FILE UNLESS PROMPTED TO DO SO
# LABORATORY EXERCISE NO. 6 TESTER

import random
import PriorityQueue

# Unsorted Priority Queue Tester
def UnsortedPQTest():
	score = 0
	TOTAL = 50
	testPQ = PriorityQueue.UnsortedPQ()
	
	# Initial Test for 'size'
	try:
		if testPQ.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing Unsorted Priority Queue")

	testDict = {
	10:"wholly",
	2:"wand",
	11:"nice",
	5:"ease",
	8:"silent",
	1:"eye",
	13:"knew",
	4:"kurisumasu",
	0:"all",
	15:"!!!",
	7:"bay bee",
	14:"here",
	3:"four",
	9:"knight",
	6:"ewe",
	12:"happee"
	}
	try:
		# Initial Test for 'insert()'

		for testKey in testDict:
			testValue = testDict.get(testKey)
			entry = PriorityQueue.Entry(testKey,testValue)
			testPQ.insert(entry)
			score+=0.5

		# Size Test
		if testPQ.getSize() == 16:
			score+=2
	except:
		print("Error: Entry() instantiation, insert(), and/or getSize() not working properly")

	try:
		current = testPQ.headNode
		while (current != None):
			if testDict[current.getEntry().getKey()]==current.getEntry().getValue():
				score+=0.5
			current = current.getNext()
	except:
		print("Error: insert() not working properly")
	
	# Print Unsorted PQ
	print("=== Unsorted Priority Queue ===")
	string = ""
	current = testPQ.headNode
	while (current.getNext() != None):
		string += (str(current.getEntry().getValue()) + " ")
		current = current.getNext()
	print(string)
	print("=== <$$$> ===\n")

	try:
		while testPQ.getSize()>4:
			minKey = min(testDict.keys())
			if minKey == testPQ.min().getKey():
				score+=0.5
			minKey2 = testPQ.remove_min().getKey()
			if minKey2 == minKey:
				score+=0.5
			testDict.pop(minKey)

			# After removal
			if minKey != testPQ.min().getKey():
				score+=0.5
	except:
		print("Error: min() or remove_min() not working properly")

	try:
		testPQ.insert(PriorityQueue.Entry(0,"We Wish You A Merry Christmas"))
		testPQ.insert(PriorityQueue.Entry(0,"White Christmas"))
		testPQ.insert(PriorityQueue.Entry(-1,"Santa Claus is Coming to Town"))
		testPQ.insert(PriorityQueue.Entry(0,"Rockin' Around the Christmas Tree"))
		testPQ.insert(PriorityQueue.Entry(1,"Jingle Bells"))
		testPQ.insert(PriorityQueue.Entry(2,"Fa La La"))
		testPQ.insert(PriorityQueue.Entry(3,"Little Drummer Boy"))
		testPQ.insert(PriorityQueue.Entry(-1,"Deck the Halls"))
		testPQ.insert(PriorityQueue.Entry(1,"Christmas In Our Hearts"))
		score+=4

		print("=== After Insertion Of New Entries ===")
		string = ""
		current = testPQ.headNode
		while (current.getNext() != None):
			string += "| "+ (str(current.getEntry().getValue()) + " |")
			current = current.getNext()
		print(string)
		print("=== <$$$> ===\n")

	except:
		print("Error: inserting with existing keys should overwrite the values")

	while not testPQ.isEmpty():
		if testPQ.remove_min():
			score+=0.5

	try:
		if testPQ.isEmpty():
			score+=1
	except:
		print("Error: Unsorted Priority Queue not empty after removing all items")

	try:
		if testPQ.min():
			print("Error: Unsorted Priority Queue does not allow min() if empty")
		if testPQ.remove_min():
			print("Error: Unsorted Priority Queue does not allow remove_min() if empty")
	except:
		score+=3

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# Sorted Priority Queue Tester
def SortedPQTest():
	score = 0
	TOTAL = 50
	testPQ = PriorityQueue.SortedPQ()
	
	# Initial Test for 'size'
	try:
		if testPQ.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing Sorted Priority Queue")

	testDict = {
	10:"wholly",
	2:"wand",
	11:"nice",
	5:"ease",
	8:"silent",
	1:"eye",
	13:"knew",
	4:"kurisumasu",
	0:"all",
	15:"!!!",
	7:"bay bee",
	14:"here",
	3:"four",
	9:"knight",
	6:"ewe",
	12:"happee"
	}
	try:
		# Initial Test for 'insert()'

		for testKey in testDict:
			testValue = testDict.get(testKey)
			entry = PriorityQueue.Entry(testKey,testValue)
			testPQ.insert(entry)
			score+=0.5

		# Size Test
		if testPQ.getSize() == 16:
			score+=2
	except:
		print("Error: Entry() instantiation, insert(), and/or getSize() not working properly")

	try:
		sortedDict = sorted(testDict)
		current = testPQ.headNode
		for i in range(16):
			if current.getEntry().getKey()==i:
				score+=0.5
			if current.getEntry().getValue()==testDict[sortedDict[i]]:
				score+=0.5
			current = current.getNext()
	except:
		print("Error: insert() not working properly")
	
	# Print Sorted PQ
	print("=== Sorted Priority Queue ===")
	string = ""
	current = testPQ.headNode
	while (current.getNext() != None):
		string += (str(current.getEntry().getValue()) + " ")
		current = current.getNext()
	print(string)
	print("=== <$$$> ===\n")

	try:
		while testPQ.getSize()>4:
			minKey = min(testDict.keys())
			assumedMinKey = min([testPQ.headNode.getEntry().getKey(),testPQ.tailNode.getEntry().getKey()])
			if minKey == assumedMinKey:
				score+=0.5
			if minKey == testPQ.min().getKey():
				score+=0.25
			if minKey == testPQ.remove_min().getKey():
				score+=0.25
			testDict.pop(minKey)

			# After removal
			if minKey != testPQ.min().getKey():
				score+=0.5
	except:
		print("Error: min() or remove_min() not working properly")

	try:
		testPQ.insert(PriorityQueue.Entry(2,"Fa La La"))
		testPQ.insert(PriorityQueue.Entry(3,"Little Drummer Boy"))
		testPQ.insert(PriorityQueue.Entry(-1,"Deck the Halls"))
		testPQ.insert(PriorityQueue.Entry(1,"Christmas In Our Hearts"))
		testPQ.insert(PriorityQueue.Entry(0,"We Wish You A Merry Christmas"))
		testPQ.insert(PriorityQueue.Entry(0,"White Christmas"))
		testPQ.insert(PriorityQueue.Entry(-1,"Santa Claus is Coming to Town"))
		testPQ.insert(PriorityQueue.Entry(0,"Rockin' Around the Christmas Tree"))
		testPQ.insert(PriorityQueue.Entry(1,"Jingle Bells"))	
		score+=3

		print("=== After Insertion Of New Entries ===")
		string = ""
		current = testPQ.headNode
		while (current.getNext() != None):
			string += "| "+ (str(current.getEntry().getValue()) + " |")
			current = current.getNext()
		print(string)
		print("=== <$$$> ===\n")

	except:
		print("Error: inserting with existing keys should overwrite the values")

	while not testPQ.isEmpty():
		testPQ.remove_min()

	try:
		if testPQ.isEmpty():
			score+=1
	except:
		print("Error: Sorted Priority Queue not empty after removing all items")

	try:
		if testPQ.min():
			print("Error: Sorted Priority Queue does not allow min() if empty")
		if testPQ.remove_min():
			print("Error: Sorted Priority Queue does not allow remove_min() if empty")
	except:
		score+=1

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")

# User Choice Prompt
def main():
	print("LABORATORY EXERCISE #6 TESTER\nOptions:\n1 - Unsorted Priority Queue\n2 - Sorted Priority Queue\n* - Exit")
	choice = int(input("Choice: "))
	if choice == 1:
		UnsortedPQTest()
	elif choice == 2:
		SortedPQTest()
	else:
		exit()

main()