class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        l=1
        r=10**7
        min_speed=float('inf')
        n=len(dist)
        def calc(speed):
            total_time=0
            for i in range(n):
                time=dist[i]/speed
                if i!=n-1:
                    total_time+=math.ceil(time)
                else:
                    total_time+=time
            return total_time

        while l<=r:
            mid=(l+r)//2
            if calc(mid)>hour:
                l=mid+1
            else:
                min_speed=min(min_speed,mid)
                r=mid-1
        return -1 if min_speed==float('inf') else min_speed
        