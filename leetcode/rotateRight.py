###########################################################
## Given a linked list, rotate the list to the right by k places, where k is non-negative.
## 
## Example 1:
## 
## Input: 1->2->3->4->5->NULL, k = 2
## Output: 4->5->1->2->3->NULL
## Explanation:
## rotate 1 steps to the right: 5->1->2->3->4->NULL
## rotate 2 steps to the right: 4->5->1->2->3->NULL
##  
###########################################################
def my_rotateRight(self, head: ListNode, k: int) -> ListNode:
    if head is None or head.next is None or k == 0:
        return head
    length = 1
    curr_node = head
    while curr_node.next:
        curr_node = curr_node.next
        length += 1

    curr_node.next = head
    k = k%length
    for i in range(length-k):
        curr_node = curr_node.next

    head = curr_node.next
    curr_node.next = None
    return head

def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None
    
    if head.next == None:
        return head
        
    pointer = head
    length = 1
    
    while pointer.next:
        pointer = pointer.next
        length += 1
    
    rotateTimes = k%length
    
    if k == 0 or rotateTimes == 0:
        return head
    
    fastPointer = head
    slowPointer = head
    
    for a in range (rotateTimes):
        fastPointer = fastPointer.next
    
    
    while fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    
    temp = slowPointer.next
    
    slowPointer.next = None
    fastPointer.next = head
    head = temp
    
    return head
