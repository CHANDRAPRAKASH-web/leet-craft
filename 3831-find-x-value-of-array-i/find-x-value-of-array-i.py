class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        dp=[[0]*k for _ in range(n)]
        for i in range(n):
            r=nums[i]%k
            dp[i][r]+=1
            if i==0:
                continue
            for j in range(k):
                value=(j*nums[i])%k
                dp[i][value]+=dp[i-1][j]
        for i in range(k):
            s=0
            for j in range(n):
                s+=dp[j][i]
            res.append(s)
        return res