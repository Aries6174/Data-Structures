class Entry:
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


class HashTableLP:
    def __init__(self, slots=30):
        self.slots = slots
        self.table = [None] * slots
        self.size = 0

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.slots

    def isEmpty(self):
        return self.size == 0

    def get(self, key):
        index = HashFunction(key, self.slots)
        start_index = index
        values = []

        while self.table[index] is not None:
            if self.table[index].getKey() == key:
                values.append(self.table[index].getValue())
            index = (index + 1) % self.getCapacity()

            if index == start_index:
                break

        if values:
            return values
        else:
            return None

    def put(self, key, value):
        index = HashFunction(key, self.slots)
        entry = Entry(key, value)

        while self.table[index] is not None:
            index = (index + 1) % self.getCapacity()

        self.table[index] = entry
        self.size += 1

    def remove(self, key):
        index = HashFunction(key, self.slots)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].getKey() == key:
                removed_entry = self.table[index]
                self.table[index] = None
                self.size -= 1
                return removed_entry

            index = (index + 1) % self.getCapacity()

            if index == start_index:
                break

        return None

    def keys(self):
        keys = []

        for entry in self.table:
            if entry is not None:
                keys += [entry.getKey()]
        return keys

    def values(self):
        values = []

        for entry in self.table:
            if entry is not None:
                values += [entry.getValue()]
        return values

    def entries(self):
        entries = []

        for entry in self.table:
            if entry is not None:
                entries += [(entry.getKey(), entry.getValue())]
        return entries


class SLLNode:
    def __init__(self, entry, nextNode = None):
        self.entry = entry
        self.nextNode = nextNode

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.entry

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode


class SLL:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return (self.size == 0)

    def addNode(self, entry):
        newNode = SLLNode(entry)
        newNode.setNext(self.head)
        self.head = newNode

    def removeNode(self,entry):
        current = self.head
        previous = None
        while current:
            if current.getValue() == entry:
                break
            else:
                previous = current
                current = current.getNext()
        if current:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

class HashTableSC:
    def __init__(self, slots=100):
        self.slots = slots
        self.table = [SLL() for _ in range(slots)]  # Initialize each slot with an empty linked list
        self.size = 0

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.slots

    def isEmpty(self):
        return self.size == 0

    def get(self, key):
        index = HashFunction(key, self.slots)
        current = self.table[index].head
        
        while current is not None:
            if current.getValue()[0] == key:
                return current.getValue()[1]
            
            current = current.getNext()
        return "None"

    def put(self, key, value):
        index = HashFunction(key, self.slots)
        self.table[index].addNode((key, value))  
        self.size += 1

    def remove(self, key):
        index = HashFunction(key, self.slots)
        previous = None
        current = self.table[index].head
        while current:
            if current.getValue()[0] == key:
                if previous:
                    previous.nextNode = current.nextNode
                else:
                    self.table[index].head = current.nextNode
                self.size -= 1
                return
            previous = current
            current = current.nextNode

    def keys(self):
        keys_list = []
        for i in range(self.slots):
            current = self.table[i].head
            while current:
                keys_list += [current.getValue()[0]]
                current = current.getNext()
        return keys_list

    def values(self):
        values_list = []
        for i in range(self.slots):
            current = self.table[i].head
            while current:
                values_list += [current.getValue()[1]]
                current = current.getNext()
        return values_list

    def entries(self): 
        entries = [] 
        for i in range(self.slots):
            if self.table[i].head is None:
                entries += ["None"]
            else:
                current = self.table[i].head
                slot_entry = []
                while current:
                    slot_entry += [str(current.getValue())]
                    current = current.getNext()
                entries += [" --> ".join(slot_entry)]
        return entries

def HashFunction(key, capacity):
    return key % capacity

def print_entries(header, hash_table):
    print(f"\n{header} ENTRIES:")
    entries = hash_table.entries()
    for entry in entries:
        print(entry)

def main():
    print("-------------------------------------------")
    print("\nHASH TABLE LINEAR PROBING TEST:")
    hash_table_lp = HashTableLP(5)
    for i in range(5):
        hash_table_lp.put(i, i)

    print_entries("HashTable LP", hash_table_lp)

    print("\nRemove 2,2")  # index 2 = none
    hash_table_lp.remove(2)
    print_entries("HashTable LP", hash_table_lp)

    print("\nAdd 4, 44")
    hash_table_lp.put(4, 44)  # index 4 -> 2
    print_entries("HashTable LP", hash_table_lp)

    print("Key 2:", hash_table_lp.get(2))
    print("Key 4:", hash_table_lp.get(4))


    print("-------------------------------------------")
    print("\nHASH TABLE SEPARATE CHAINING TEST:")
    hash_table_sc = HashTableSC(10)

    for i in range(4):
        hash_table_sc.put(i, i)

    print_entries("HashTable SC", hash_table_sc)

    print("\nAdded index 4 with 57")
    hash_table_sc.put(12, 57)  # index 2
    print_entries("HashTable SC", hash_table_sc)

    print("\nRemoved index 1")
    hash_table_sc.remove(1)  # index 1
    print_entries("HashTable SC", hash_table_sc)

    print("\nAdded index 22 with 222")
    hash_table_sc.put(22, 222)  # index 2
    print_entries("HashTable SC", hash_table_sc)

    print("\nRemove 3, 3")
    hash_table_sc.remove(3)  # index 4
    print_entries("HashTable SC", hash_table_sc)

    print("\nRemoving 2,22")
    hash_table_sc.remove(2)
    print_entries("HashTable SC", hash_table_sc)

    print("\nRemoving 222")
    hash_table_sc.remove(22)
    print_entries("HashTable SC", hash_table_sc)

    print("\nRemoving 22")
    hash_table_sc.remove(12)
    print_entries("HashTable SC", hash_table_sc)

    print("\nPutting 2")
    hash_table_sc.put(2, 2)
    print_entries("HashTable SC", hash_table_sc)

    print("\nPutting 6")
    hash_table_sc.put(4, 6)
    print_entries("HashTable SC", hash_table_sc)

    print("\nPutting 27")
    hash_table_sc.put(14, 27)
    print_entries("HashTable SC", hash_table_sc)

    print("\nKey 0: ", hash_table_sc.get(0))
    print("Key 1: ", hash_table_sc.get(1))
    print("Key 2: ", hash_table_sc.get(2))
    print("Key 3: ", hash_table_sc.get(3))
    print("Key 4: ", hash_table_sc.get(4))
    print("All Keys: ", hash_table_sc.keys())
    print("All Values: ", hash_table_sc.values())

main()
