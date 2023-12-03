class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list():
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def Append(self, value):
        pass