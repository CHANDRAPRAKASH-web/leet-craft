class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        l=1
        r=max(nums)
        res=r
        while l<=r:
            mid=(l+r)//2
            time=0
            for i in range(len(nums)):
                time+=math.ceil(nums[i]/mid)
            if time<=h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res