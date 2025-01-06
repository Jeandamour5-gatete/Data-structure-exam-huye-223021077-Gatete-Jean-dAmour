#A tree to represent hierarchical data in the smart home automation system
class TreeNode:
    def __init__(self, name, is_item=False):
        self.name = name
        self.is_item = is_item  
        self.children = [] 

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self, level=0):
        indent = " " * (level * 4)
        if self.is_item:
            return f"{indent}- Item: {self.name}"
        else:
            return f"{indent}Category: {self.name}"


class WarehouseInventoryTree:
    def __init__(self):
        self.root = TreeNode("Warehouse")  

    def add_category(self, parent_name, category_name):
        parent_node = self._find_node(self.root, parent_name)
        if parent_node:
            category_node = TreeNode(category_name)
            parent_node.add_child(category_node)
            print(f"Category '{category_name}' added under '{parent_name}'.")
        else:
            print(f"Category '{parent_name}' not found.")

    def add_item(self, category_name, item_name):
        category_node = self._find_node(self.root, category_name)
        if category_node:
            item_node = TreeNode(item_name, is_item=True)
            category_node.add_child(item_node)
            print(f"Item '{item_name}' added to category '{category_name}'.")
        else:
            print(f"Category '{category_name}' not found.")

    def _find_node(self, current_node, name):
        if current_node.name == name:
            return current_node
        for child in current_node.children:
            result = self._find_node(child, name)
            if result:
                return result
        return None

    def display_tree(self):
        print("Warehouse Inventory Tree:")
        print(self.root)
        self._display_children(self.root, level=1)

    def _display_children(self, node, level):
        for child in node.children:
            print(child)
            if not child.is_item:
                self._display_children(child, level + 1)

    def search_item(self, item_name):
        found_node = self._find_node(self.root, item_name)
        if found_node and found_node.is_item:
            print(f"Item Found: {found_node.name}")
        else:
            print(f"Item '{item_name}' not found.")

    def delete_item(self, item_name):
        parent_node = self._find_parent(self.root, item_name)
        if parent_node:
            for child in parent_node.children:
                if child.name == item_name and child.is_item:
                    parent_node.children.remove(child)
                    print(f"Item '{item_name}' deleted from the inventory.")
                    return
        print(f"Item '{item_name}' not found.")

    def _find_parent(self, current_node, name):
        for child in current_node.children:
            if child.name == name:
                return current_node
            if not child.is_item:
                parent = self._find_parent(child, name)
                if parent:
                    return parent
        return None

inventory_tree = WarehouseInventoryTree()
inventory_tree.add_category("Warehouse", "Electronics")
inventory_tree.add_category("Warehouse", "Furniture")

inventory_tree.add_category("Electronics", "Laptops")
inventory_tree.add_category("Electronics", "Smartphones")
inventory_tree.add_category("Furniture", "Chairs")
inventory_tree.add_category("Furniture", "Tables")

inventory_tree.add_item("Laptops", "Laptop Model X")
inventory_tree.add_item("Laptops", "Laptop Model Y")
inventory_tree.add_item("Smartphones", "Smartphone Model A")
inventory_tree.add_item("Chairs", "Office Chair Model 1")
inventory_tree.add_item("Chairs", "Gaming Chair Model 2")

inventory_tree.display_tree()
inventory_tree.search_item("Laptop Model X")
inventory_tree.delete_item("Laptop Model Y")
inventory_tree.display_tree()
inventory_tree.search_item("Laptop Model Y")
