class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node

    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        print("")

    def push(self, data): ## Adds node to the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, prev_data, new_data): ## Add a node in the middle of the list
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node:
            if curr_node.data == prev_data:
                new_node.prev = curr_node
                new_node.next = curr_node.next
                curr_node.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
            curr_node = curr_node.next
    
    def append(self, data): ## Add a node in the end of the list
        new_node = Node(data)
        if self.head is None:
            new_node = self.head
            return
        
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        
        curr_node.next = new_node
        new_node.prev = curr_node

    def remove(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                return
            curr_node = curr_node.next

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            curr_node.prev = next_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

d = DoublyLinkedList()
d.push(11)
d.push(22)
d.push(33)

d.insert(22,25)
d.print()

d.remove(25)
d.print()

d.append(10)
d.print()

d.reverse()
d.print()