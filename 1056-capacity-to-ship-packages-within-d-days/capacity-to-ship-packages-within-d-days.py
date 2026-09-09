class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        l=max(nums)
        r=sum(nums)
        res=r
        def canShip(mid):
            ship=1
            curr_load=mid
            for w in nums:
                if curr_load-w<0:
                    ship+=1
                    curr_load=mid
                curr_load-=w
            return ship

        while l<=r:
            mid=(l+r)//2
            if canShip(mid)<=days:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
        