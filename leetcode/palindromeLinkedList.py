################################################################
## Given a singly linked list, determine if it is a palindrome.
## 
## Example 1:
## Input: 1->2
## Output: false
## 
## Example 2:
## Input: 1->2->2->1
## Output: true
################################################################

def my_isPalindrome(self, head):
    if head is None:
        return True
    arr = []
    curr_node = head
    while curr_node:
        arr.append(curr_node.val)
        curr_node = curr_node.next

    if arr == arr[::-1]:
        return True
    else:
        return False
        
def isPalindrome(self, head):
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev

def isPalindrome(self, head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    head2 = slow if not fast else slow.next  ## In case of even number of nodes
    
    prev = None
    while slow:
        # nxt = slow.next
        # slow.next = prev
        # prev = slow
        # slow = nxt
        slow.next,slow,prev = prev,slow.next,slow
    
    first = head
    second = prev

    while first and second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True