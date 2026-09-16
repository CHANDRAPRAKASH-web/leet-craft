class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        l=0
        res=0
        a={}
        for r in range(len(s)):
            a[s[r]]=1+a.get(s[r],0)
            while len(a)!=r-l+1:
                a[s[l]]-=1
                if a[s[l]]==0:
                    del a[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res
            
            