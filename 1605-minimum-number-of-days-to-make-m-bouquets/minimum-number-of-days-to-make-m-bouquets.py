class Solution:
    def minDays(self, nums: List[int], m: int, k: int) -> int:
        l=min(nums)
        r=max(nums)
        res=float('inf')
        def check(n):
            count=0
            cnt=0
            for i in nums:
                if i<=n:
                    cnt+=1
                else:
                    count+=(cnt//k)
                    cnt=0
            count+=(cnt//k)
            return count
        while l<=r:
            mid=(l+r)//2
            if check(mid)>=m:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return -1 if res==float('inf') else res

            