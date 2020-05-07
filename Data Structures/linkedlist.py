class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        print("")

    def add_at_begin(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def add_after(self, prev_data, new_data):
        new_node = Node(new_data)
        curr_node = self.head

        while curr_node:
            if curr_node.data == prev_data:
                new_node.next = curr_node.next
                curr_node.next = new_node
            curr_node = curr_node.next
            
    def remove(self, data):
        curr_node = self.head

        if curr_node:
            if curr_node.data == data:
                self.head = curr_node.next
                curr_node = None
                return
    
        while curr_node:
            if curr_node.data == data:
                break
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = curr_node.next

l = LinkedList(Node("Mon"))
e2 = Node("Tue")
e3 = Node("Wed")
l.head.next = e2
e2.next = e3

# l.print()

l.add_at_begin("Sun")
# l.print()

l.add_at_end("Sat")
# l.print()

l.add_after("Wed", "Thu")
l.add_after("Sat", "Sat1")
l.print()

l.remove("Sat1")
l.print()