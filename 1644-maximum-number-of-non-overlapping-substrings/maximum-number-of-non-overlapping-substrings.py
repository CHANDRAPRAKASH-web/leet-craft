class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        interval={}
        for i,val in enumerate(s):
            if val not in interval:
                interval[val]=[i,i]
            else:
                interval[val][1]=i
        for i in interval:
            l,r=interval[i]
            while True:
                lc,rc=l,r
                for j in range(lc,rc+1):
                    l=min(l,interval[s[j]][0])
                    r=max(r,interval[s[j]][1])
                if (lc,rc)==(l,r):
                    break
                    
            interval[i]=(l,r)
        candidates=sorted(interval.values(),key=lambda x:x[1])
        res=[]
        prev=-1
        for start,end in candidates:
            if start>prev:
                res.append(s[start:end+1])
                prev=end
        return res
        
        