#Binary Search Tree (BST) to manage a fixed number of orders in the smart home automation system
class OrderNode:
    def __init__(self, order_id, item_name, quantity, status):
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.status = status
        self.next = None  

class OrderLinkedList:
    def __init__(self, max_size):
        self.head = None 
        self.size = 0 
        self.max_size = max_size  

    def add_order(self, order_id, item_name, quantity, status):
        if self.size >= self.max_size:
            print("Cannot add more orders. The warehouse is at full capacity.")
            return
        
        new_order = OrderNode(order_id, item_name, quantity, status)
        
        if self.head is None:
            self.head = new_order
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_order
        
        self.size += 1
        print(f"Order ID {order_id} added to the inventory.")

    def delete_order(self, order_id):
        current = self.head
        previous = None
    
        if current is None:
            print("No orders to delete.")
            return
        
        if current.order_id == order_id:
            self.head = current.next  
            self.size -= 1
            print(f"Order ID {order_id} deleted from the inventory.")
            return
        
        while current is not None and current.order_id != order_id:
            previous = current
            current = current.next
        
        if current is None:
            print(f"Order ID {order_id} not found.")
        else:
            previous.next = current.next
            self.size -= 1
            print(f"Order ID {order_id} deleted from the inventory.")
    
    def search_order(self, order_id):
        current = self.head
        while current is not None:
            if current.order_id == order_id:
                print(f"Order Found: ID: {current.order_id}, Item: {current.item_name}, Quantity: {current.quantity}, Status: {current.status}")
                return
            current = current.next
        print(f"Order ID {order_id} not found.")

    def display_orders(self):
        if self.head is None:
            print("No orders in the inventory.")
            return
        current = self.head
        print("Warehouse Orders:")
        while current is not None:
            print(f"Order ID: {current.order_id}, Item: {current.item_name}, Quantity: {current.quantity}, Status: {current.status}")
            current = current.next

    def count_orders(self):
        return self.size

warehouse_orders = OrderLinkedList(max_size=5) 

warehouse_orders.add_order(1, "Laptop", 50, "Pending")
warehouse_orders.add_order(2, "Smartphone", 200, "Shipped")
warehouse_orders.add_order(3, "Tablet", 150, "Pending")
warehouse_orders.add_order(4, "Monitor", 80, "Delivered")
warehouse_orders.add_order(5, "Keyboard", 120, "Pending")

warehouse_orders.add_order(6, "Mouse", 100, "Pending")
warehouse_orders.display_orders()
warehouse_orders.search_order(2)
warehouse_orders.delete_order(3)
warehouse_orders.display_orders()
print(f"Total Orders in the system: {warehouse_orders.count_orders()}")
