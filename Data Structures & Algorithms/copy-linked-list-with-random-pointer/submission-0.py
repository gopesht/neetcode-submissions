"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        hm = dict()
        while current:
            node = Node(current.val)
            hm[current] = node
            current = current.next
        current = head
        newListCurrent = hm.get(head)
        
        while current:
            node = hm.get(current)
            node.next = hm.get(current.next) 
            node.random = hm.get(current.random)
            current = current.next

        return newListCurrent

        