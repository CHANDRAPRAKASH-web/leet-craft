class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=n
        b=n
        for a in range(1,n):
            b=b-1
            if '0' not in str(a) and '0' not in str(b) and a+b==n:
                return [a,b]
        