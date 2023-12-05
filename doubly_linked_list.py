class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
    def GetValue(self):
        if self.value is not None:
            return self.value
        else:
            return None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def Append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = self.tail.next
        self.length += 1
        return True

    def Pop(self):
        if self.length == 0:
            return None
        current_node = self.tail
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.length -= 1
        return current_node
    
    def Prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def PopFirst(self):
        if self.length == 0:
            return None
        current_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            current_node.next = None
        self.length -= 1
        return current_node
    
    def Get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.previous
        return current_node
    
    def SetValue(self, index, value):
        current = self.Get(index)
        if(current):
            current.value = value
            return True
        return False
    
    def GetTail(self):
        if self.tail:
            return self.tail
        return None
    
    def GetHead(self):
        if self.head:
            return self.head
        return None
    
    def PrintTailHead(self):
        try:
            print("Head-> " + str(doublyList.GetHead().GetValue()) + 
                " Tail-> " + str(doublyList.GetTail().GetValue()))
        except:
            print("None")
    
    def GetLength(self):
        return self.length

doublyList = DoublyLinkedList(5)


doublyList.PrintTailHead()
doublyList.print_list()
doublyList.Prepend(4)
doublyList.PrintTailHead()
doublyList.Prepend(3)
doublyList.print_list()
doublyList.PrintTailHead()

print(doublyList.Get(0).value)

doublyList.SetValue(2, 55)
doublyList.print_list()
doublyList.PrintTailHead()