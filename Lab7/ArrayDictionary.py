class Entry:
    # Use the 'Entry' class used in Lab6, since they should be relatively the same
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


class Array:
    # Insert the 'Array' class you created in Lab2, since they should be the same
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.contents = [None] * capacity
        self.size = 0
        # The 'size' attribute must not exceed the 'capacity'

    def getSize(self):
        # returns the size of the array
        return self.size

    def getCapacity(self):
        # returns the capacity of the Array
        return self.capacity

    def isEmpty(self):
        # The isEmpty() operation returns true if the array is empty and false if the array is not empty
        return self.size == 0


class ArrayDictionary(Array):
    # Note: Class "ArrayDictionary" inherits the class "Array" attributes and methods
    # Note: Elements in the Array are Entries

    def insert(self, key, value):
        # inserts an entry with the specified key and value in the dictionary such that entries with the same key are grouped together
        new_entry = Entry(key, value)
        current_key = 0

        while (current_key < self.size and new_entry.getKey() > self.contents[current_key].getKey()):
            current_key += 1

        for i in range(self.size, current_key, -1):
            self.contents[i] = self.contents[i - 1]

        self.contents[current_key] = new_entry
        self.size += 1


    def remove(self, entry):
        # removes the specified entry, and returns the entry that was removed; move elements forward/backward when necessary
        for i in range(self.size):
            if (self.contents[i].getKey() == entry.getKey() and self.contents[i].getValue() == entry.getValue()):
                
                remove_entry = self.contents[i]

                for j in range(i, self.size - 1):
                    self.contents[j] = self.contents[j + 1]

                self.contents[self.size - 1] = None
                self.size -= 1

                return remove_entry
            
        raise Exception("Lmao its Empty")

    def find(self, key):
        # finds and returns the entry that matches the specified key (there could be multiple matches)
        for i in range(self.size):
            if (self.contents[i].getKey() == key):
                return self.contents[i]

        raise Exception("Lmao its None")

    # Iterator Methods
    def find_all(self, key):
        # iterates through the existing entries in the dictionary and prints all the entries (in the format "key:value") with the specified key in order
        for i in range(self.size):
            if self.contents[i].getKey() == key:
                print(f"({self.contents[i].getKey()}: {self.contents[i].getValue()})", end=" ")

    def entries(self):
        # iterates through the existing entries in the dictionary and prints all the entries (in the format "key:value") in order
        print("\n")
        for i in range(self.size):
            print(f"({self.contents[i].getKey()}: {self.contents[i].getValue()})", end=" ")