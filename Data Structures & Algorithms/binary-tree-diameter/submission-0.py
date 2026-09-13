# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter(root)
        return self.result



    def diameter(self, root: Optional[TreeNode]) -> int:
        global result
        if not root:
            return 0
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        self.result = max(self.result, left + right)

        return 1 + max(left, right)
