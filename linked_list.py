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
        if (self.length == 0):
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
        if (self.length == 0):
            return None
        popped = self.head
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return popped
    
    def get(self, index):
        if (index < 0 or index >= self.length):
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    def set_value(self, index, value):
        current_node = self.get(index)
        if (current_node):
            current_node.value = value
            return True
        return None
    
    def insert(self, index, value):
        if (index < 0 or index > self.length):
            return False
        if (index == 0):
            return self.prepend(value)
        if (index == self.length):
            return self.append(value)
        new_node = Node(value)
        previous_node = self.get(index-1)
        new_node.next = previous_node.next
        previous_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if (index < 0 or index >= self.length):
            return None
        if (index == 0):
            return self.pop_first()
        if (index == self.length - 1):
            return self.pop()
        previous_node = self.get(index - 1)
        current_node = previous_node.next
        previous_node.next = current_node.next
        current_node.next = None
        self.length -= 1
        return current_node
    
    def reverse(self):
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node

        next_node = temp_node.next
        previous_node = None
        for _ in range(self.length):
            next_node = temp_node.next
            temp_node.next = previous_node
            previous_node = temp_node
            temp_node = next_node
            

    def get_head(self):
        if (self.head):
            return self.head.value
        return None
    
    def get_tail(self):
        if (self.tail):
            return self.tail.value
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
print("Tail: " + str(list1.get_tail()))
list1.append(6)
print("Tail: " + str(list1.get_tail()))
list1.append(99)
print("Length: " + str(list1.get_length()))
list1.print_list()
print(list1.get(2).value)
list1.set_value(0, 49503)
list1.insert(2, 223)
print("####")
list1.print_list()
print("Head: " + str(list1.get_head()))
print("Length: " + str(list1.get_length()))
list1.remove(3)
print("####")
list1.print_list()
print("Head: " + str(list1.get_head()))
print("Length: " + str(list1.get_length()))
print("Tail: " + str(list1.get_tail()))
print("####")
list1.reverse()
list1.print_list()
print("Head: " + str(list1.get_head()))
print("Length: " + str(list1.get_length()))
print("Tail: " + str(list1.get_tail()))