class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        for i in range(len(nums)):
            for j in range(i+1,i+n):
                index=j%n
                if nums[index]>nums[i]:
                    res[i]=nums[index]
                    break
        return res
                 
        