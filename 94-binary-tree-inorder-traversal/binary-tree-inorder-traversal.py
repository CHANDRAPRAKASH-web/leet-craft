# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res=[]
        def inorder(root):
            if not root:
                return
            left=inorder(root.left)
            res.append(root.val)
            right=inorder(root.right)
        inorder(root)
        return res

