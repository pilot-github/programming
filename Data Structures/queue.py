class Queue:
    def __init__(self):
        self.items = list()

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return not bool(self.items)
    
    def print(self):
        print(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
q = Queue()
print(q.is_empty())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size())
q.print()

q.dequeue()
print(q.size())
q.print()
print(q.is_empty())
