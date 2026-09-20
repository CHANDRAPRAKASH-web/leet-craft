class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i,c in enumerate(s):
            index=ord('z')-ord(c)+1
            product=index*(i+1)
            res+=product
        return res
        