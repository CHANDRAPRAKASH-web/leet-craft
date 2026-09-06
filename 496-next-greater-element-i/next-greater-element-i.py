class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=defaultdict(int)
        for i,n in enumerate(nums1):
            a[n]=i
        res=[-1]*(len(nums1))
        for i in range(len(nums2)):
            cur=nums2[i]
            if cur in a:
                for j in range(i+1,len(nums2)):
                    if nums2[j]>nums2[i]:
                        res[a[cur]]=nums2[j]
                        break
        return res


       