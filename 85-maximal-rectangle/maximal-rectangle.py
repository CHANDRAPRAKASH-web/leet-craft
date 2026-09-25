class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        def calculate_area(nums):
            n=len(nums)
            stack=[]
            max_area=0
            for i,val in enumerate(nums):
                if stack and val<stack[-1][0]:
                    while stack and val<stack[-1][0]:
                        a=stack.pop()
                        max_area=max(max_area,a[0]*(i-a[1]))
                    stack.append((val,a[1]))
                if not stack or val>stack[-1][0]:
                    stack.append((val,i))
            for i in stack:
                max_area=max(max_area,i[0]*(n-i[1]))
            
            return max_area

        prefix_sum=[[0]*(len(matrix[0])) for _ in range(len(matrix))]
        for j in range(len(matrix[0])):
            prefix=0
            for i in range(len(matrix)):
                num=matrix[i][j]
                if num=='1':
                    prefix+=1
                    prefix_sum[i][j]=prefix
                else:
                    prefix=0
                    prefix_sum[i][j]=prefix
        max_area=0
        for i in prefix_sum:
            max_area=max(max_area,calculate_area(i))

        return max_area
    