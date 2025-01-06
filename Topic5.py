#Circular Queue to track data dynamically in smart home automation system
class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Item(ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity})"


class InventoryStack:
    def __init__(self):
        self.stack = []

    def push(self, item_id, name, quantity):
        new_item = Item(item_id, name, quantity)
        self.stack.append(new_item)
        print(f"Added: {new_item}")

    def pop(self):
        if self.is_empty():
            print("No items to remove.")
            return None
        removed_item = self.stack.pop()
        print(f"Removed: {removed_item}")
        return removed_item

    def peek(self):
        if self.is_empty():
            print("No items in the stack.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display_stack(self):
        if self.is_empty():
            print("No items in the inventory.")
        else:
            print("Current Inventory Stack:")
            for item in reversed(self.stack):
                print(item)

    def undo(self):
        if self.is_empty():
            print("No actions to undo.")
            return
        self.pop()

inventory = InventoryStack()

inventory.push(1, "Laptop", 50)
inventory.push(2, "Smartphone", 200)
inventory.push(3, "Tablet", 150)

inventory.display_stack()

last_item = inventory.peek()
print(f"\nLast added item: {last_item}")

inventory.pop()
inventory.display_stack()
inventory.undo()
inventory.display_stack()
inventory.undo()
