class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        d=0
        res=[]
        for i in seq:
            if i=='(':
                res.append(d%2)
                d+=1
            else:
                d-=1
                res.append(d%2)
        return res
                