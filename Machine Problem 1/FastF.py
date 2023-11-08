import datetime         #importing Time
import ArrayQueue       #importing Queue

class FoodItem:         #for the Item that will be manually inputted
    def __init__(self, name, price, quantity):  #The name, price, and quantity
        self.name = name    #assigning name
        self.price = price  #assigning price
        self.quantity = quantity    #assigning quantity

class Order:            # for the actual order
    def __init__(self, numberCustomer, foodItems):  #The Order will Contain the Customer's Number(Like in jollibee), the Items ordered, and the date it was ordered.
        self.numberCustomer = numberCustomer    #assigning numberCustomer
        self.foodItems = foodItems  #assigning FoodItem
        self.dateTime = datetime.datetime.now() #Assigning DateTime as the current DateTime now
 
    def display_order(self):    #when choice number 2 is chosen
        print("Order for Customer/Receipt Number:", self.numberCustomer) #printing the Reciept Number
        for item in self.foodItems: #for Prints each item ordered by the customer
            item_description = "Item: " + item.name + ", Price: $" + str(item.price) + ", Quantity: " + str(item.quantity)  #Prints the Name, price and Quantity of the Item ordered
            print(item_description) #Printing happens here
    
        print("Order placed on:", self.dateTime)    #Prints the dateTime which is a requirement
        total_price = 0 #everytime when displaying it equates to 0 and calculates for the total price
        for item in self.foodItems: #for every item in the customers order, is calculates for their total price
            total_price += item.price * item.quantity
        print("Total Price: $" + str(total_price)) #Prints the total Price

class FastFoodOrderingSystem:   #For Putting the Orders and removing them (Queues)
    def __init__(self, capacity=10):    
        self.queue = ArrayQueue.ArrayQueue(capacity)    #calling ArrayQueue

    def putOrder(self): #when we are putting an order
        foodItemsArray = [] #stores the foodItems
        while True:
            name = input("Food Item Name (or 'done' to finish inputting): ")    #request for food name
            if name == 'done':  
                break   #Stops if done was inputted
            price = float(input("Food Item Price: ")) #Since its possible to have decimals on price we use float
            quantity = int(input("Food Item Quantity: ")) #Quantity is Discrete so we use int
            item = FoodItem(name, price, quantity)  #Stores all necessary
            foodItemsArray += [item]    #adds the Item inside FoodItemsArray
        order = Order("Customer/Receipt Number: "+ foodItemsArray)  #printing the order
        self.queue.enqueue(order)  # Enqueue the Order object directly
        print("Order placed.")  # signifies that the order has been made

    def displayNowOrder(self):  #for showing the order
        nowOrderElement = self.queue.front()    #Takes the info of the first Order
        if nowOrderElement is not None and nowOrderElement.value is not None:   #if there is an order and its value exists
            nowOrder = nowOrderElement.value    #storing the value inside nowOrder
            nowOrder.display_order()    #print each order
        else:
            print("No current order available.")   

    def removeNowOrder(self):   #when removing an order
        if not self.queue.isEmpty():    
            removed_element = self.queue.dequeue() #dequeue the element
            removed_order = removed_element.value #storing the element value
            print("Removed the recent order:")
            removed_order.display_order()   #reshowing the removed order
        else:
            print("No order to remove.")

#Printing system
if __name__ == "__main__":  
    ordering_system = FastFoodOrderingSystem()  #Initiating the system inside ordering_system

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


