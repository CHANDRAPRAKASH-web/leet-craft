class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stk=[]
        res=[0]*n
    
        for i in range(n-1,-1,-1):
            while stk and nums[stk[-1]]<=nums[i]:
                idx=stk.pop()
            if stk:
                res[i]=stk[-1]-i
            stk.append(i)
        return res
        