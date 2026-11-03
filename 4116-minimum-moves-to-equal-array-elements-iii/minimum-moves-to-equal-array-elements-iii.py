class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a=max(nums)
        r=0
        for i in nums:
            r+=a-i
        return r
        