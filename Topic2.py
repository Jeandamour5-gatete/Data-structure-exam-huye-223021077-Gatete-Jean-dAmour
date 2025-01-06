#Circular Queue and Linked List to manage data in the smart home automation system
class TreeNode:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item_id, name, quantity):
        if self.root is None:
            self.root = TreeNode(item_id, name, quantity)
        else:
            self._insert(self.root, item_id, name, quantity)

    def _insert(self, node, item_id, name, quantity):
        if item_id < node.item_id:
            if node.left is None:
                node.left = TreeNode(item_id, name, quantity)
            else:
                self._insert(node.left, item_id, name, quantity)
        elif item_id > node.item_id:
            if node.right is None:
                node.right = TreeNode(item_id, name, quantity)
            else:
                self._insert(node.right, item_id, name, quantity)

    def search(self, item_id):
        return self._search(self.root, item_id)

    def _search(self, node, item_id):
        if node is None or node.item_id == item_id:
            return node
        if item_id < node.item_id:
            return self._search(node.left, item_id)
        return self._search(node.right, item_id)

    def delete(self, item_id):
        self.root = self._delete(self.root, item_id)

    def _delete(self, node, item_id):
        if node is None:
            return node
        if item_id < node.item_id:
            node.left = self._delete(node.left, item_id)
        elif item_id > node.item_id:
            node.right = self._delete(node.right, item_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.item_id = temp.item_id
            node.name = temp.name
            node.quantity = temp.quantity
            node.right = self._delete(node.right, temp.item_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"Item ID: {node.item_id}, Name: {node.name}, Quantity: {node.quantity}")
            self.inorder(node.right)

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item_id, name, quantity, priority):
        self.heap.append((item_id, name, quantity, priority))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[(index - 1) // 2][3] > self.heap[index][3]:
            self.heap[(index - 1) // 2], self.heap[index] = self.heap[index], self.heap[(index - 1) // 2]
            index = (index - 1) // 2

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_item

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child][3] < self.heap[smallest][3]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][3] < self.heap[smallest][3]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None
bst = BinarySearchTree()
bst.insert(1, "Laptop", 50)
bst.insert(2, "Smartphone", 200)
bst.insert(3, "Tablet", 150)

print("Binary Search Tree (Items by ID):")
bst.inorder(bst.root)
heap = MinHeap()
heap.insert(1, "Laptop", 50, 2) 
heap.insert(2, "Smartphone", 200, 1) 
heap.insert(3, "Tablet", 150, 3)  
print("\nMin-Heap (Items by Priority):")
min_item = heap.get_min()
if min_item:
    print(f"Item with highest priority: {min_item[1]} - Priority: {min_item[3]}")
else:
    print("Heap is empty.")
removed_item = heap.delete_min()
if removed_item:
    print(f"\nRemoved item with priority: {removed_item[1]} - Priority: {removed_item[3]}")
else:
    print("No items to remove.")
