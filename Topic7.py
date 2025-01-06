#Selection Sort to sort the smart home automation system data based on priority
class Item:
    def __init__(self, item_id, name, priority):
        self.item_id = item_id
        self.name = name
        self.priority = priority  

    def __repr__(self):
        return f"Item(ID: {self.item_id}, Name: {self.name}, Priority: {self.priority})"


def selection_sort(items):
    n = len(items)
    for i in range(n):
    
        min_index = i
        for j in range(i + 1, n):
            if items[j].priority < items[min_index].priority:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

if __name__ == "__main__":
    inventory_items = [
        Item(1, "Laptop", 2),
        Item(2, "Smartphone", 3),
        Item(3, "Tablet", 1),
        Item(4, "Smartwatch", 4),
        Item(5, "Headphones", 5)
    ]
    
    print("Before Sorting:")
    for item in inventory_items:
        print(item)
    selection_sort(inventory_items)
    
    print("\nAfter Sorting by Priority:")
    for item in inventory_items:
        print(item)
