# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        while current:
            current = current.next
            count += 1
        countFromStart = count - n
        if countFromStart == 0:
            return head.next
        current = head
        
        while countFromStart-1 > 0:
            current = current.next
            countFromStart -= 1
        
        current.next = current.next.next
        return head
        