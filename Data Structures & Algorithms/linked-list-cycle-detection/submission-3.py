# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        if head:
            current2 = head.next
        else:
            current2 = None
        
        while current and current2:
            if current.val == current2.val:
                return True
            current = current.next
            if current2.next:
                current2 = current2.next.next
            else:
                current2 = None
        

        return False
        