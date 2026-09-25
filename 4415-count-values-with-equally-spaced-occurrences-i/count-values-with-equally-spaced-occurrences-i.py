class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        a=defaultdict(list)
        for i,val in enumerate(nums):
            a[val].append(i)
        count=0
        for i in a:
            if len(a[i])==3:
                if a[i][1]-a[i][0]==a[i][2]-a[i][1]:
                    count+=1
        return count


        