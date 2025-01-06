#Heap for smart home automation system processing
class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

class WarehouseInventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item_id, name, quantity):
        for item in self.inventory:
            if item.item_id == item_id:
                print(f"Item with ID {item_id} already exists. Use update_item to modify the quantity.")
                return
        new_item = Item(item_id, name, quantity)
        self.inventory.append(new_item)
        print(f"Item '{name}' added to the inventory.")

    def update_item(self, item_id, quantity):
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity += quantity
                print(f"Item '{item.name}' quantity updated to {item.quantity}.")
                return
        print(f"Item with ID {item_id} not found in the inventory.")

    def search_item(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                print(f"Item Found: ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}")
                return
        print(f"Item with ID {item_id} not found in the inventory.")

    def delete_item(self, item_id):
        for i, item in enumerate(self.inventory):
            if item.item_id == item_id:
                del self.inventory[i]
                print(f"Item with ID {item_id} has been deleted from the inventory.")
                return
        print(f"Item with ID {item_id} not found in the inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("The inventory is empty.")
        else:
            print("Warehouse Inventory:")
            for item in self.inventory:
                print(f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}")

warehouse = WarehouseInventory()

warehouse.add_item(1, "Laptop", 50)
warehouse.add_item(2, "Smartphone", 200)
warehouse.add_item(3, "Tablet", 150)

warehouse.display_inventory()
warehouse.update_item(1, 20)
warehouse.search_item(2)
warehouse.delete_item(3)
warehouse.display_inventory()
