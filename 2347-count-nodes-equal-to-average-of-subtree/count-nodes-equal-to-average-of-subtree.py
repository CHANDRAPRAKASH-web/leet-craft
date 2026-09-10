
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res=0
        def dfs(node):
            if not node:
                return 0,0
            left_sum,left_count=dfs(node.left)
            right_sum,right_count=dfs(node.right)
            if (left_sum+right_sum+node.val)//(left_count+right_count+1)==node.val:
                self.res+=1
            return left_sum+right_sum+node.val,left_count+right_count+1
        dfs(root)
        return self.res
        