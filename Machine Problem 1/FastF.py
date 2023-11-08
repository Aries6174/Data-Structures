import datetime
import ArrayQueue

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, numberCustomer, foodItems):
        self.numberCustomer = numberCustomer
        self.foodItems = foodItems
        self.dateTime = datetime.datetime.now()

    def getFinalPrice(self):
        finalPrice = 0
        for item in self.foodItems:
            finalPrice += item.price * item.quantity
        return finalPrice
    
    def display_order(self):
        print("Order for Customer/Receipt Number:", self.numberCustomer)
        for item in self.foodItems:
            item_description = "Item: " + item.name + ", Price: $" + str(item.price) + ", Quantity: " + str(item.quantity)
            print(item_description)
        print("Order placed on:", self.dateTime)
        total_price = 0
        for item in self.foodItems:
            total_price += item.price * item.quantity
        print("Total Price: $" + str(total_price))

class FastFoodOrderingSystem:
    def __init__(self, capacity=10):
        self.queue = ArrayQueue.ArrayQueue(capacity)

    def putOrder(self):
        numberCustomer = input("Receipt Number: ")
        foodItemsArray = []
        while True:
            name = input("Food Item Name (or 'done' to finish inputting): ")
            if name == 'done':
                break
            price = float(input("Food Item Price: "))
            quantity = int(input("Food Item Quantity: "))
            item = FoodItem(name, price, quantity)
            foodItemsArray.append(item)
        order = Order(numberCustomer, foodItemsArray)
        self.queue.enqueue(order)  # Enqueue the Order object directly
        print("Order placed.")

    def displayNowOrder(self):
        nowOrderElement = self.queue.front()
        if nowOrderElement is not None and nowOrderElement.value is not None:
            nowOrder = nowOrderElement.value
            nowOrder.display_order()
        else:
            print("No current order available.")

    def removeNowOrder(self):
        if not self.queue.isEmpty():
            removed_element = self.queue.dequeue()
            removed_order = removed_element.value
            print("Removed the recent order:")
            removed_order.display_order()
        else:
            print("No order to remove.")

if __name__ == "__main__":
    ordering_system = FastFoodOrderingSystem()

    while True:
        print("\nFast Food Ordering System Menu:")
        print("1. Place an Order")
        print("2. Display Current Order")
        print("3. Remove Current Order")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ordering_system.putOrder()
        elif choice == '2':
            ordering_system.displayNowOrder()
        elif choice == '3':
            ordering_system.removeNowOrder()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")


