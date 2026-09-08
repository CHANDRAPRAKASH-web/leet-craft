class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        a=defaultdict(int)
        for i in nums:
            a[i]+=1
        y=float('inf')
        res_x=-1
        x=min(nums)
        for i in a:
            if a[x]!=a[i]:
                res_x=x
                y=min(y,i)
        return [-1,-1] if res_x==-1 else[res_x,y]