class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stk=[]
        for i in range(2*n-1,-1,-1):
            while stk and stk[-1]<=nums[i%n]:
                stk.pop()
            if i<n and stk:
                res[i]=stk[-1]
            stk.append(nums[i%n])
        return res
        