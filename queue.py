#Queues are FIFO

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def PrintQueue(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def Enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1

    def Dequeue(self): #FIFO
        if self.first is None:
            return None
        removed = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next 
            removed.next = None
        self.length -= 1
        return removed

myQueue = Queue(4)
myQueue.Enqueue(5)
myQueue.Enqueue(6)
myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Enqueue(7)
myQueue.Dequeue()
myQueue.PrintQueue()