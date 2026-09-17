class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        res=float('inf')
        dp=[inf]*n
        l=0
        p=0
        for r in range(n):
            p+=arr[r]
            while p>target:
                p-=arr[l]
                l+=1
            dp[r]=dp[r-1] if r-1>=0 else inf
            if p==target:
                res=min(res,r-l+1+dp[l-1] if l-1>=0 else inf)
                dp[r]=min(dp[r-1],r-l+1)
        return -1 if res==inf else res

        