class Solution:
    def countCommas(self, n: int) -> int:
        comma=0
        start=1000
        while start<=n:
            comma+=n-start+1
            start=start*1000
        return comma
        