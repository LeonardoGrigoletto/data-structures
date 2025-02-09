from typing import Any

class Node:
    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self) -> bool:
        if self.root is None:
            return True
        return False
    
    def contains(self, value: int) -> bool:
        # if self.is_empty(): # we don't need this.
        #     return False
        current_pointer = self.root
        while current_pointer is not None:
            if current_pointer.value == value:
                return True
            if value < current_pointer.value:
                current_pointer = current_pointer.left
            else:
                current_pointer = current_pointer.right
        return False
        
    
    def insert(self, value: int) -> bool: # O(logn)
        new_node = Node(value=value)
        current_pointer = self.root
        if self.is_empty():
            self.root = new_node
            return True
        while current_pointer is not None:
            if new_node.value == current_pointer.value:
                return False
            if new_node.value < current_pointer.value:
                if current_pointer.left is None:
                    current_pointer.left = new_node
                    return True
                current_pointer = current_pointer.left
            else:
                if current_pointer.right is None:
                    current_pointer.right = new_node
                    return True
                current_pointer = current_pointer.right 


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(value=50)

    tree.insert(value=35)
    tree.insert(value=75)
    tree.insert(value=62)
    tree.insert(value=80)
    tree.insert(value=10)
    tree.insert(value=42)

    print(tree.contains(value=50))
    print(tree.contains(value=35))
    print(tree.contains(value=62))
    print(tree.contains(value=80))
    print(tree.contains(value=10))
    print(tree.contains(value=42))
    print(tree.contains(value=79))
                
