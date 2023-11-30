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
        current = self.head
        next = None
        previous = None

        self.tail = self.head

        for _ in range(self.length):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_middle_node(self):
        current_node = self.head
        second_node = self.head
        while(second_node is not None and second_node.next is not None):
            current_node = current_node.next
            second_node = second_node.next.next
        return current_node
            
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

    def partition_list(self, x):
        if(self.head is None):
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current_node = self.head
        while current_node is not None:
            if current_node.value < x:
                prev1.next = current_node
                prev1 = current_node
            elif current_node.value >= x:
                prev2.next = current_node
                prev2 = current_node
            prev1.next = None
            prev2.next = None
            
            dummy2.next = prev1
            self.head = dummy1.next
                    
            current_node = current_node.next


#find item from kth to the end
def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
        
    while (fast is not None):
        slow = slow.next
        fast = fast.next
    return slow

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
list1.append(10)
list1.append(7)
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
print(list1.find_middle_node().value)