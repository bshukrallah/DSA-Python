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
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if (self.length == 1):
            self.tail = new_node
        return True

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
    
    def pop(self):
        if self.length == 0:
            return None
        
        current_node = self.head
        previous_node = self.head
        while(current_node.next):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        self.tail = previous_node
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_node

    def pop_first(self):
        if self.length == 0:
            return None
        popped = self.head
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return popped

            
    def get_head(self):
        if (self.head):
            return self.head.value
        else:
            return None
    
    def get_tail(self):
        if(self.tail):
            return self.tail.value
        else:
            return None
    
    def get_length(self):
        return self.length
    
    def print_list(self):
        temp_node = self.head
        while(temp_node):
            print(temp_node.value)
            temp_node = temp_node.next

list1 = LinkedList(4)
print("Head: " + str(list1.get_head()))
list1.prepend(62)
print(list1.pop_first().value)
print("Head: " + str(list1.get_head()))
list1.pop()
print("Tail: " + str(list1.get_tail()))
list1.append(6)
print("Tail: " + str(list1.get_tail()))
list1.append(99)
print("Length: " + str(list1.get_length()))
list1.print_list()
list1.append(49)
list1.prepend(102)
list1.print_list()
print("Tail: " + str(list1.get_tail()))
print("Length: " + str(list1.get_length()))

list1.pop()
print("Head: " + str(list1.get_head()))
print("Tail: " + str(list1.get_tail()))
print("Length: " + str(list1.get_length()))

list1.pop()
list1.pop()
list1.pop()
list1.pop()
print("Length: " + str(list1.get_length()))
print("Tail: " + str(list1.get_tail()))

list1.prepend(55)
print("Head: " + str(list1.get_head()))
print("Length: " + str(list1.get_length()))
print("Tail: " + str(list1.get_tail()))

list1.pop_first()

print("Head: " + str(list1.get_head()))
print("Length: " + str(list1.get_length()))
print("Tail: " + str(list1.get_tail()))