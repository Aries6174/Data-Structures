from Employees import Employee, employee_list, display_employees

class SLLNode:
    def __init__(self, entry, nextNode=None):
        self.entry = entry
        self.nextNode = nextNode

    def getValue(self):
        return self.entry

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

class SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return (self.size == 0)

    def addNode(self, entry):
        newNode = SLLNode(entry)
        newNode.setNext(self.head)
        self.head = newNode
        self.size += 1

    def removeNode(self, entry):
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
            self.size -= 1

class HashTableSC:
    def __init__(self, slots=30):
        self.slots = slots
        self.table = [SLL() for _ in range(slots)]
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
        return None  # Return None if key is not found

    def put(self, key, value):
        index = HashFunction(key, self.slots)
        existing_value = self.get(key)
        if existing_value is not None:
            # Key already exists, update the value
            self.remove(key)
        self.table[index].addNode((key, value))
        self.size += 1

    def remove(self, key):
        index = HashFunction(key, self.slots)
        previous = None
        current = self.table[index].head
        while current:
            if current.getValue()[0] == key:
                if previous:
                    previous.setNext(current.getNext())
                else:
                    self.table[index].head = current.getNext()
                self.size -= 1
                return
            previous = current
            current = current.getNext()

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

class Handler:
    def __init__(self):
        self.hash_table = HashTableSC()
        self.employee_list = employee_list
        self.hash_table_name = {}
        self.hash_table_years = {}
        self.populate_hash_tables()

    def populate_hash_tables(self):
        for i, employee in enumerate(self.employee_list):
            name_key = employee.getFullName().lower()  # Convert to lowercase
            self.hash_table_name[name_key] = i
            self.hash_table.put(name_key, i)  # Use put instead of direct assignment

            years_key = int(employee.getYears())
            self.hash_table_years[years_key] = i

    def search_by_name_specific(self, name):
        name_lower = name.lower()
        index = self.hash_table.get(name_lower)
        if index is not None:
            results = [self.employee_list[index]]
            return results
        else:
            print(f"{name} is not one of our employees.")
            return []


    def search_by_name_containing(self, name):
        name = name.lower()
        results = []
        for key in self.hash_table.keys():
            if name in key.lower():
                index = self.hash_table.get(key)
                results.append(self.employee_list[index])
        if not results:
            print(f"There is no one in the employees list that contains the name '{name.capitalize()}'.")
        return results

    def search_by_years_active(self, years):
        matching_employees = [employee for employee in self.employee_list if employee.years == years]
        return matching_employees
    
    def search_by_job(self, job):
        job = job.lower()
        results = [employee for employee in self.employee_list if job in [j.lower() for j in employee.joblist]][:30]
        return results if results else None

    def display_employee_info(self, employee_info=None):
        print()
        if employee_info is None:
            display_employees()
        elif isinstance(employee_info, list):
            for employee in employee_info:
                print("\n===========| Employee No.", employee_list.index(employee) + 1, "|===========")
                print("Name:", employee.getFullName())
                print("Address:", employee.getAddress())
                print("Years In Industry:", employee.getYears())
                print("Description:", employee.getDesc())
                print("\n--------| List Of Assigned Jobs |--------", employee.getJobs())
                print("==========================================")
        else:
            # Display for the case when search_by_years_active returns a single Employee object
            print("\n===========| Employee No.", employee_list.index(employee_info) + 1, "|===========")
            print("Name:", employee_info.getFullName())
            print("Address:", employee_info.getAddress())
            print("Years In Industry:", employee_info.getYears())
            print("Description:", employee_info.getDesc())
            print("\n--------| List Of Assigned Jobs |--------", employee_info.getJobs())
            print("==========================================")
            print()

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Search by Name")
            print("2. Search by Years Active")
            print("3. Search by Job")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                search_type = input("Choose search type (1 for specific, 2 for containing): ")
                name = input("Enter the name: ")

                if search_type == '1':
                    employee_info = self.search_by_name_specific(name)
                    self.display_employee_info(employee_info)
                elif search_type == '2':
                    employee_info = self.search_by_name_containing(name)
                    self.display_employee_info(employee_info)
                else:
                    print("Invalid search type. Please enter 1 or 2.")

            elif choice == '2':
                try:
                    years_active = int(input("Enter the years active: "))
                    results = self.search_by_years_active(years_active)
                    if results is not None:
                        for result in results:
                            self.display_employee_info(result)
                    else:
                        print()
                        print("Employee not found.")
                except ValueError:
                    print("Please input a valid integer for years active.")

            elif choice == '3':
                job = input("Enter the job: ")
                results = self.search_by_job(job)
                if results is not None:
                    for result in results:
                        self.display_employee_info(result)
                else:
                    print()
                    print("Employee not found.")

            elif choice == '4':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                
def HashFunction(key, capacity):
    # Simple hash function using the sum of ASCII values of characters
    hash_value = sum(ord(char) for char in key)
    return hash_value % capacity

if __name__ == "__main__":
    handler = Handler()
    handler.main_menu()

'''
Which function is the fastest?
    The fastest function is searching by name because it iterates through the
    whole list trying to find the names that matched, if not it continues to the
    next up to the end. Running time is O(n), where in n is the number of employees
    in the list.

Which function is most efficient?
    The most efficient function is searching by name (specific) because it directly
    looks up the name in the hash table, providing constant time complexity on average.
    The hash table provides faster retrieval compared to iterating through the entire list.

Which function is most reliable?
    The most reliable function depends on the use case. If you want a precise match for
    a specific name, then searching by name (specific) is more reliable. If you want to
    find names that contain a certain substring, then searching by name (containing) is
    more suitable.
'''