# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = prev = None
        c = 0
        while l1 and l2:
            s = (l1.val + l2.val) % 10
            node = ListNode(s + c)
            c = (l1.val + l2.val) // 10
            if prev:
                prev.next = node
            if not newHead:
                newHead = node
            prev = node
            l1 = l1.next
            l2 = l2.next
        print(c)
        while l1:
            s = (l1.val + c) % 10
            node = ListNode(s)
            c = (l1.val + c) // 10
            prev.next = node
            prev = node
            l1 = l1.next
        while l2:
            s = (l2.val + c) % 10
            node = ListNode(s)
            c = (l2.val + c) // 10
            prev.next = node
            prev = node
            l2 = l2.next
        if c != 0:
            prev.next = ListNode(c)
        return newHead
        