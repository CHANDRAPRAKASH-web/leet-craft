class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n=len(digits)
        res=set()
        count=0
        for i in range(n):
            if digits[i]!=0:
                for j in range(n):
                    if i!=j:
                        for k in range(n):
                            if i!=k and j!=k and digits[k]%2==0:
                                num=digits[i]*100+digits[j]*10+digits[k]
                                res.add(num)
        nums=sorted(res)
        return nums


            
        