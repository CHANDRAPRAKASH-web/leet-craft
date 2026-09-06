class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=defaultdict(int)
        for i,n in enumerate(nums1):
            a[n]=i
        res=[-1]*(len(nums1))
        stk=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stk and cur>stk[-1]:
                val=stk.pop()
                idx=a[val]
                res[idx]=cur
            if cur in a:
                stk.append(cur)
        return res

      

       


       