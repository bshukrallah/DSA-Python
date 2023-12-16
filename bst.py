#Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        current_node = self.root
        while(True):
            if new_node.value is current_node.value:
                return False
            if (value < current_node.value):
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                current_node = current_node.right
        
    def Contains(self, value):
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif value > current.value:
                current = current.right
            else:
                current = current.left
        return False
                

BST = BinarySearchTree()

BST.Insert(5)
BST.Insert(1)
BST.Insert(7)
print(BST.root.value)
print(BST.root.left.value)
print(BST.root.right.value)
print(BST.Contains(0))