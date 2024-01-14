# WARNING: DO NOT EDIT THE CONTENTS OF THIS FILE UNLESS PROMPTED TO DO SO
# LABORATORY EXERCISE NO. 7 TESTER

import random

# Array Dictionary Tester
def ArrayDictionaryTest():
	import ArrayDictionary
	score = 0
	TOTAL = 50
	testAD = ArrayDictionary.ArrayDictionary()
	
	# Initial Test for 'size'
	try:
		if testAD.isEmpty():
			score+=1
	except:
		print("Error: Problem initializing Array Dictionary")

	testDict = {
	10:"wholly",
	1:["eye","wand","four"],
	11:["nice","happee"],
	13:"knew",
	0:"all",
	15:"!!!",
	4:["ease","kurisumasu"],
	7:["bay bee","silent","knight"],
	14:"here",
	6:"ewe",
	}

	removeDict = {
	10:"wholly",
	1:["wand","four"],
	4:["ease"],
	13:"knew",
	0:"all",
	15:"!!!",
	7:["bay bee","knight"],
	14:"here",
	6:"ewe",
	11:["happee"]
	}
	try:
		# Initial Test for 'insert()'

		for testKey in testDict:
			testValue = testDict.get(testKey)
			if type(testValue) is list:
				for item in testValue:
					testAD.insert(testKey,item)
					score+=0.5
			else:
				testAD.insert(testKey,testValue)
				score+=0.5

		# Size Test
		if testAD.getSize() == 16:
			score+=2
	except:
		print("Error: Entry() instantiation, insert(), and/or getSize() not working properly")

	try:
		for key in testDict:
			if testAD.find(key).getValue() in testDict[key]:
				score+=0.5
	except:
		print("Error: insert() and/or find() not working properly")
	
	# Print Array Dictionary
	print("=== < Array Dictionary > ===")
	string = ""
	i = 0
	while (testAD.contents[i] != None):
		string += " (" + (str(testAD.contents[i].getKey())) + " : " + (str(testAD.contents[i].getValue())) + ") "
		i += 1
	print(string)
	print("=== <$$$> ===\n")

	try:
		for key1 in removeDict:
			if type(removeDict[key1]) is list:
				for value in removeDict[key1]:
					entry1 = ArrayDictionary.Entry(key1,value)
					entry2 = testAD.remove(entry1)
					if entry1.getValue() == entry2.getValue():
						score+=1
					testDict[key1].remove(value)

					# After removal
					if entry2.getValue() not in testDict[key1]:
						score+=0.5
			else:		
				if testAD.find(key1).getValue() == testDict[key1]:
					score+=0.5
				entry1 = ArrayDictionary.Entry(key1,removeDict[key1])
				entry2 = testAD.remove(entry1)
				if entry1.getValue() == entry2.getValue():
					score+=0.5
				testDict.pop(key1)

				# After removal
				try:
					testAD.find(key1).getValue()		
				except:
					score+=0.5
	except:
		print("Error: find() or remove() not working properly")

	try:
		testAD.insert(0,"We Wish You A Merry Christmas")
		testAD.insert(0,"White Christmas")
		testAD.insert(-1,"Santa Claus is Coming to Town")
		testAD.insert(0,"Rockin' Around the Christmas Tree")
		testAD.insert(1,"Jingle Bells")
		testAD.insert(2,"Fa La La")
		testAD.insert(3,"Little Drummer Boy")
		testAD.insert(-1,"Deck the Halls")
		testAD.insert(1,"Christmas In Our Hearts")
		testAD.insert(3,"Santa Tell Me")
		score+=5

		testDict[-1] = ["Santa Claus is Coming to Town", "Deck the Halls"]
		testDict[0] = ["We Wish You A Merry Christmas", "White Christmas", "Rockin' Around the Christmas Tree"]
		testDict[1] += ["Jingle Bells", "Christmas In Our Hearts"]
		testDict[2] = "Fa La La"
		testDict[3] = ["Little Drummer Boy", "Santa Tell Me"]
	except:
		print("Error: inserting with existing keys should NOT overwrite the values and instead create new entries")

	try:
		print("=== After Insertion Of New Entries ===")
		testAD.find_all(0)
		testAD.find_all(1)
		testAD.find_all(-1)
		testAD.find_all(3)
		# Note that your score is not added here, so the score for find_all() will be based on output/presentation
		
		testAD.entries()
		# Note that your score is not added here, so the score for entries() will be based on output/presentation
		print("=== <$$$> ===\n")
	except:
		print("Error: find_all() and/or entries() not working properly")
	
	for key1 in testDict:
		entryValue = testDict[key1]
		if type(entryValue) is list:
			for value in entryValue:
				oldList = testDict[key1]
				entry = ArrayDictionary.Entry(key1,value)
				testAD.remove(entry)
				score+=0.5
		else:
			entry = ArrayDictionary.Entry(key1,entryValue)
			testAD.remove(entry)
			score+=0.5

	try:
		if testAD.isEmpty():
			score+=1
	except:
		print("Error: Array Dictionary not empty after removing all items")

	try:
		if testAD.find(key1):
			print("Error: Array Dictionary does not allow find() if empty")
		if testAD.remove(entry1):
			print("Error: Array Dictionary does not allow remove() if empty")
	except:
		score+=3

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")
	else:
		print ("TRY AGAIN!!!")

# DLL Map Tester
def DLLMapTest():
	import DLLMap
	score = 0
	TOTAL = 50
	testMap = DLLMap.DLLMap()
	
	# Initial Test for 'size'
	try:
		if testMap.isEmpty():
			score+=1 #check
	except:
		print("Error: Problem initializing DLL Map")

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
		# Initial Test for 'put()'

		for testKey in testDict:
			testValue = testDict.get(testKey)
			testMap.put(testKey,testValue)
			score+=0.5 # check

		# Size Test
		if testMap.getSize() == 16:
			score+=2 # check
	except:
		print("Error: Entry() instantiation, put(), and/or getSize() not working properly")



	try:
		current = testMap.headNode
		for i in range(16):
			if current.getEntry().getKey() in testDict.keys():
				score+=0.5 # 8 points check
				
			if testMap.get(current.getEntry().getKey()) == testDict[current.getEntry().getKey()]:
				score+=0.5 # 8 points
			current = current.getNext()
	except:
		print("Error: get() not working properly")
	
	# Print DLL Map
	print("=== DLL Map ===")
	string = ""

	current = testMap.headNode
	while (current != None):
		string += " (" + (str(current.getEntry().getKey())) + " : " + (str(current.getEntry().getValue())) + ") "
		current = current.getNext()
	print(string)
	print("=== <$$$> ===\n")

	try:
		while testMap.getSize()>4:
			minKey = min(testDict.keys())
			if minKey == testMap.find_node(minKey).getEntry().getKey():
				score+=0.5
			key2 = testMap.remove(minKey).getKey()
			if minKey == key2:
				score+=0.5
			testDict.pop(minKey)

			# After removal
			minKey2 = min(testDict.keys())
			if minKey != testMap.find_node(minKey2).getEntry().getKey():
				score+=0.5
	except:
		print("Error: find_node() or remove() not working properly")

	try:
		testMap.put(2,"Fa La La")
		testMap.put(3,"Little Drummer Boy")
		testMap.put(-1,"Deck the Halls")
		testMap.put(1,"Christmas In Our Hearts")
		testMap.put(0,"We Wish You A Merry Christmas")
		testMap.put(0,"White Christmas")
		testMap.put(-1,"Santa Claus is Coming to Town")
		testMap.put(0,"Rockin' Around the Christmas Tree")
		testMap.put(1,"Jingle Bells")
		score+=3

		testDict[-1] = "Santa Claus is Coming to Town"
		testDict[0] = "Rockin' Around the Christmas Tree"
		testDict[1] = "Jingle Bells"
		testDict[2] = "Fa La La"
		testDict[3] = "Little Drummer Boy"

	except:
		print("Error: inserting with existing keys should overwrite the values")

	try:
		print("=== After Insertion Of New Entries ===")
		testMap.keys()
		# Note that your score is not added here, so the score for keys() will be based on output/presentation
		
		testMap.values()
		# Note that your score is not added here, so the score for values() will be based on output/presentation
		
		testMap.entries()
		# Note that your score is not added here, so the score for entries() will be based on output/presentation
		print("=== <$$$> ===\n")
	except:
		print("Error: keys(),values() and/or entries() not working properly")

	try:
		for key1 in testDict:
			testMap.remove(key1)
	except:
		print("Error: DLL Map items are not equal to testDict[] items")

	try:
		if testMap.isEmpty():
			score+=1
	except:
		print("Error: DLL Map not empty after removing all items")

	try:
		if testMap.get(key1):
			print("Error: DLL Map does not allow get() if empty")
		if testMap.remove(key1):
			print("Error: DLL Map does not allow remove() if empty")
	except:
		score+=1

	print ("Your TOTAL SCORE is " + str(score) + "/" + str(TOTAL) + ".")
	print ("Percentage: %.2f" % ((score/TOTAL)*100) + "%")
	if score == TOTAL:
		print ("PERFECT SCORE!!!")
	else:
		print ("TRY AGAIN!!!")

# User Choice Prompt
def main():
	print("LABORATORY EXERCISE #7 TESTER\nOptions:\n1 - Array Dictionary\n2 - DLL Map\n* - Exit")
	choice = int(input("Choice: "))
	if choice == 1:
		ArrayDictionaryTest()
	elif choice == 2:
		DLLMapTest()
	else:
		exit()

main()