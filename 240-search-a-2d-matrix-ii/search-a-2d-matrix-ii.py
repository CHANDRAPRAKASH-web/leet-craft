class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=0
        c=len(matrix[0])-1
        while c>=0 and r<len(matrix):
            if matrix[r][c]==target:
                return True
            if matrix[r][c]>target:
                c-=1
            elif matrix[r][c]<target:
                r+=1
        return False