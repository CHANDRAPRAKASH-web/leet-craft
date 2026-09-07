class Solution:
    def countRotations(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            rs=s[i:]+s[:i+1]
            count=0
            for j in range(len(s)-1):
                if rs[j]==rs[j+1]:
                    count+=1
            if count==k:
                res+=1
        return res
        