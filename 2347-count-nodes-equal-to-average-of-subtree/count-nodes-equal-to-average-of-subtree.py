
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res=0
        def dfs(node):
            if not node:
                return 0,0
            left_sum,left_count=dfs(node.left)
            right_sum,right_count=dfs(node.right)
            n_sum=left_sum+right_sum+node.val
            n_count=left_count+right_count+1
            if n_sum//n_count==node.val:
                self.res+=1
            return n_sum,n_count
        dfs(root)
        return self.res
        