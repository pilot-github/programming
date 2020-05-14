################################################
## Given linked list: 1->2->3->4->5, and n = 2.
## After removing the second node from the end, the linked list becomes 1->2->3->5.
################################################

def reverse(self, head):
    if head is None:
        return
    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    head = prev_node

    return head

def print(self, head):
    if head is None:
        return

    curr_node = head
    while curr_node:
        print(curr_node.val)
        curr_node = curr_node.next


def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    rev_head = self.reverse(head)
    self.print(rev_head)

    if rev_head is None:
        return

    curr_node = rev_head
    if curr_node and n==1:
        rev_head = curr_node.next
        curr_node = None
        head = self.reverse(rev_head)
        return head

    while curr_node and n >= 0:
        if n == 1:
            break
        prev_node = curr_node
        curr_node = curr_node.next
        n -= 1

    prev_node.next = curr_node.next

    head = self.reverse(rev_head)
    return head
    
    
def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    for i in range(n+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next
