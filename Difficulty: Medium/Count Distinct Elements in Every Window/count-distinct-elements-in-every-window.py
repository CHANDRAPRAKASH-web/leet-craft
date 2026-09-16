class Solution:
    def countDistinct(self, arr, k):
        # code here
        l=0
        res=[]
        a={}
        for r in range(len(arr)):
            a[arr[r]]=1+a.get(arr[r],0)
            if r-l+1>=k:
                res.append(len(a))
                a[arr[l]]-=1
                if a[arr[l]]==0:
                    del a[arr[l]]
                l+=1
        return res
            