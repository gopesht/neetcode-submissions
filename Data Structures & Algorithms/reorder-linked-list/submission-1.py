# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        fast = head

        while fast and fast.next:
            current = current.next
            fast = fast.next.next
        

        split = current.next

        prev = current.next = None

        while split:
            temp = split.next
            split.next = prev
            prev = split
            split = temp
        
        list1 = head
        list2 = prev
        newHead = list1
        while list2:
            temp = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp
            list1 = temp
            list2 = temp2
        

        