class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def PrintStack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

    def Push(self, value):
        new_node = Node(value)
        if(self.height == 0):
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def Pop(self):
        if(self.height == 0):
            return None
        popped = self.top
        self.top = popped.next
        popped.next = None
        self.height -= 1
        return popped.value

myStack = Stack(5)
myStack.Push(3)
myStack.Push(8)
myStack.PrintStack()

myStack.Pop()
myStack.PrintStack()