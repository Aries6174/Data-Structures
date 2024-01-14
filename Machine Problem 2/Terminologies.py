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
        if not isinstance(key, (int, str)):
            raise ValueError("Key must be an integer or a string")

        if isinstance(key, str):
            index = HashFunction(hash(key), self.slots)
        else:
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
        if not isinstance(key, (int, str)):
            raise ValueError("Key must be an integer or a string")

        if isinstance(key, str):
            index = HashFunction(hash(key), self.slots)
        else:
            index = HashFunction(key, self.slots)

        entry = Entry(key, value)

        while self.table[index] is not None:
            index = (index + 1) % self.getCapacity()

        self.table[index] = entry
        self.size += 1

    def remove(self, key):
        index = HashFunction(hash(key), self.slots)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].getKey() == key:
                removed_entry = self.table[index]
                self.table[index] = None
                self.size -= 1

                # Rehash subsequent elements if they were affected by the removal
                next_index = (index + 1) % self.getCapacity()
                while self.table[next_index] is not None:
                    # Calculate the original hash of the next entry
                    original_hash = HashFunction(self.table[next_index].getKey(), self.slots)

                    # If the original hash indicates that the next entry should be placed before the start_index,
                    # then move it to the current index and update the indices for the next iteration
                    if original_hash <= start_index:
                        self.table[index] = self.table[next_index]
                        self.table[next_index] = None
                        index = next_index

                    next_index = (next_index + 1) % self.getCapacity()

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

def HashFunction(key, capacity):
    return key % capacity

class Terminology:
    def __init__(self):
        self.terminologies = HashTableLP()

    field_names = {
        '0': 'N/A',
        '1': 'Programming and Logic',
        '2': 'Graphics and Visualization',
        '3': 'Artificial Intelligence',
        '4': 'Scientific Computing',
        '5': 'Data Structures and Algorithms',
        '6': 'Architecture and Networks',
        '7': 'Security and Safety'
    }

    def is_valid_field(self, field):
        valid_fields = set()
        for i in range(8):
            valid_fields.add(f"{i:02}")

        return field in valid_fields

    def add_term(self):
        try:
            term = input("Enter the Terminology: ")
            part_of_speech = int(input("Enter the Part of Speech (Noun-1, Verb-2, Adjective-3, N/A-0): "))
            definition = input("Enter the Definition of Terminology: ")
            fields = input("Enter Field(s) of Computer Science it is used (comma-separated): ").split(',')
            fields = [field.strip() for field in fields]

            unique_fields = set()
            valid_fields = set(f"{i:02}" for i in range(8))

            for field in fields:
                if self.is_valid_field(field) and field not in unique_fields:
                    unique_fields.add(field)

            if unique_fields:
                sorted_fields = sorted([int(field) for field in unique_fields])  # Sort fields
                self.terminologies.put(term.lower(), {'part_of_speech': part_of_speech, 'definition': definition,
                                                    'fields': sorted_fields})
                print("Term added successfully!")
            else:
                print("Invalid or duplicate field number. Please enter valid and unique field numbers (00-07).")

        except ValueError:
            print("Invalid input. Please enter a valid integer for Part of Speech or valid integers for Field(s).")

    def search_term(self):
        if self.terminologies.isEmpty():
            print("Terminology Guide is currently empty. Nothing to search Lmao.")
        else:
            search_term = input("Enter the term to search: ")
            found_terms = self.terminologies.get(search_term.lower())
            if found_terms:
                for term in found_terms:
                    print(f"Term: {search_term}")
                    print(f"Part of Speech: {term['part_of_speech']}")
                    print(f"Definition: {term['definition']}")

                    # Print both field numbers and their corresponding names
                    field_numbers = [str(field) for field in term['fields']]
                    field_names = [self.field_names.get(number, f"Unknown Field {number}") for number in field_numbers]
                    fields_info = [f"{field} ({field_names[i]})" for i, field in enumerate(term['fields'])]
                    print(f"Fields of Computer Science: {', '.join(fields_info)}")

                    print("-" * 30)
            else:
                print(f"The term '{search_term}' does not exist in the guide.")


    def update_term(self):
        if self.terminologies.isEmpty():
            print("Terminology Guide is currently empty. Nothing to update Lmao.")
        else:
            try:
                update_term = input("Enter the term to update: ")
                found_terms = self.terminologies.get(update_term.lower())
                if found_terms:
                    term = found_terms[0]
                    print(f"Current details for term '{update_term}':")
                    print(f"Part of Speech: {term['part_of_speech']}")
                    print(f"Definition: {term['definition']}")
                    print(f"Fields of Computer Science: {', '.join(map(str, term['fields']))}")
                    print("-" * 30)

                    new_part_of_speech = int(input("Enter the new Part of Speech (Noun-1, Verb-2, Adjective-3, N/A-0): "))
                    new_definition = input("Enter the new Definition of Terminology: ")
                    new_fields_input = input("Enter the new Field(s) of Computer Science it is used (comma-separated): ")
                    new_fields = [field.strip() for field in new_fields_input.split(',')]

                    unique_new_fields = set()
                    valid_fields = set(f"{i:02}" for i in range(8))

                    for field in new_fields:
                        if self.is_valid_field(field) and field not in unique_new_fields:
                            unique_new_fields.add(field)

                    if all(self.is_valid_field(field) for field in unique_new_fields):
                        new_fields = sorted([int(field) for field in unique_new_fields])  # Sort fields
                        term['part_of_speech'] = new_part_of_speech
                        term['definition'] = new_definition
                        term['fields'] = new_fields
                        print("Term updated successfully!")
                    else:
                        print("Invalid or duplicate field number. Please enter valid and unique field numbers (00-07).")

                else:
                    print(f"The term '{update_term}' does not exist in the guide.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for Part of Speech or valid integers for Field(s).")


    def remove_term(self):
        if self.terminologies.isEmpty():
            print("Terminology Guide is currently empty. Nothing to remove Lmao.")
        else:
            try:
                remove_term = input("Enter the term to remove: ")
                removed_entry = self.terminologies.remove(remove_term.lower())
                if removed_entry:
                    print(f"Term '{remove_term}' removed successfully!")
                else:
                    print(f"The term '{remove_term}' does not exist in the guide.")
            except ValueError:
                print("Invalid input. Please enter a valid term for removal.")

    def display_guide(self):
        if self.terminologies.isEmpty():
            print("Terminology Guide is currently empty. Nothing to display Lmao.")
        else:
            print("Terminology Guide:")
            for key, term in self.terminologies.entries():
                print("-" * 12 + "ENTRY" + "-" * 12)
                print(f"Term: {key}")
                print(f"Part of Speech: {term['part_of_speech']}")
                print(f"Definition: {term['definition']}")

                field_numbers = [str(field) for field in term['fields']]
                field_names = [self.field_names.get(number, f"Unknown Field {number}") for number in field_numbers]

                # Print both field numbers and their corresponding names
                fields_info = [f"{field} ({field_names[i]})" for i, field in enumerate(term['fields'])]
                print(f"Fields of Computer Science: {', '.join(fields_info)}")
                print("-" * 30)

    def main(self):
        while True:
            print("\nOptions:")
            print("1. Add a Term")
            print("2. Search and Display a Term's Definition")
            print("3. Update a Term or its Definition(s)")
            print("4. Remove a Term from the List")
            print("5. Display Guide")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            try:
                choice = int(choice)
                if choice == 1:
                    self.add_term()
                elif choice == 2:
                    self.search_term()
                elif choice == 3:
                    self.update_term()
                elif choice == 4:
                    self.remove_term()
                elif choice == 5:
                    self.display_guide()
                elif choice == 6:
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the menu choice.")


if __name__ == "__main__":
    guide = Terminology()
    guide.main()