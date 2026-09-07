class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stk=[]
        res=[0]*n
    
        for i in range(n):
            while stk and nums[stk[-1]]<nums[i]:
                idx=stk.pop()
                res[idx]=i-idx
            stk.append(i)
        return res
        