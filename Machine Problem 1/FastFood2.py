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

def displayNowOrder(self):
    if not self.queue.isEmpty():
        elementNow = self.queue.front()
        orderNow = elementNow.value
        orderNow.display_order()
    else:
        print("No current order available.")

class FastFoodOrderingSystem:
    def __init__(self, capacity=10):
        self.queue = ArrayQueue.ArrayQueue(capacity)

    def putOrder(self):
        numberCustomer = input("Enter Customer/Receipt Number: ")
        foodItemsArray = []
        while True:
            name = input("Enter Food Item Name (or 'done' to finish adding items): ")
            if name == 'done':
                break
            price = float(input("Enter Food Item Price: "))
            quantity = int(input("Enter Food Item Quantity: "))
            item = FoodItem(name, price, quantity)
            foodItemsArray.append(item)
        order = Order(numberCustomer, foodItemsArray)
        self.queue.enqueue(order)  # Enqueue the Order object directly
        print("Order placed successfully.")

    def displayNowOrder(self):
        nowOrder = self.queue.front()
        if nowOrder is not None:
            nowOrder.display_order()
        else:
            print("No current order available.")

    def removeNowOrder(self):
        if not self.queue.isEmpty():
            removed_order = self.queue.dequeue()
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
