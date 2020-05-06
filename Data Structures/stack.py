
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def print(self):
        print (self.items)
    
    def is_empty(self):
        return not bool(len(self.items))

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()


s = Stack()
print(s.is_empty())
s.push(5)
s.push('H')
s.push('e')
s.push('l')
s.push('l')
s.push('o')

s.print()
print(s.is_empty())
print(s.size())
s.pop()
s.print()
print(s.size())

