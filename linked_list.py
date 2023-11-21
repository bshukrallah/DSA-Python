class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def prepend(self, value):
        pass

    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def get_head(self):
        return self.head.value
    
    def get_tail(self):
        return self.tail.value
    
    def get_length(self):
        return self.length
    
    def print_list(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

list1 = LinkedList(4)
print("Tail: " + str(list1.get_tail()))
list1.append(6)
print("Tail: " + str(list1.get_tail()))
list1.append(99)
print("Length: " + str(list1.get_length()))
list1.print_list()
list1.append(49)
list1.print_list()
print("Tail: " + str(list1.get_tail()))
print("Length: " + str(list1.get_length()))