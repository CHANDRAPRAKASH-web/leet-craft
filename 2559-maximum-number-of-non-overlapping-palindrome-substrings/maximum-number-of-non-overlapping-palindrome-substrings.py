class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        res=0
        i=0
        if k==1:
            return n
        while i<=n-k:
            for d in (k,k+1):
                if i+d<=n and s[i:i+d]==s[i:i+d][::-1]:
                    res+=1
                    i+=d
                    break
            else:
                i+=1
        return res
        