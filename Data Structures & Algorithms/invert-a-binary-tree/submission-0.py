# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeUtil(root)


    def invertTreeUtil(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            t = root.left
            root.left = root.right
            root.right = t
            self.invertTreeUtil(root.left)
            self.invertTreeUtil(root.right)
            return root
        else:
            None
        