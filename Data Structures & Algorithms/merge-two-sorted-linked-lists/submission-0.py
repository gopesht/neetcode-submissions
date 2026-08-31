# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        current3,newHead = None, None

        while current1 or current2:
            value = None
            if current1 and current2:
                if current1.val <= current2.val:
                    value = current1.val
                    current1 = current1.next
                else:
                    value = current2.val
                    current2 = current2.next
            elif current1:
                value = current1.val
                current1 = current1.next
            else:
                value = current2.val
                current2 = current2.next
            temp = ListNode(value)
            if current3:
                current3.next = temp
                current3 = current3.next
            else:
                newHead = temp
                current3 = temp
        return newHead
                            