class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        target=sum(nums)-x
        max_array=-1
        l=0
        prefix_sum=0
        if target<0:
            return -1
        for r in range(n):
            prefix_sum+=nums[r]
            while prefix_sum>target:
                prefix_sum-=nums[l]
                l+=1
            if prefix_sum==target:
                max_array=max(max_array,r-l+1)

        return -1 if max_array==-1 else n-max_array

        