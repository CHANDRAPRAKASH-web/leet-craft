class Solution:
    def minMoves(self, nums: list[int]) -> int:
        a=min(nums)
        r=0
        for i in nums:
            r+=i-a
        return r

        