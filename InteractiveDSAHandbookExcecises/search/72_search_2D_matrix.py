"""
https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols
        
        while left < right:
            mid = (left + right) // 2
            # Conver the middle index into a matrix position
            # by dividing the number of cols to get the row 
            # and taking the reminder for the col
            ridx = mid // cols
            cidx = mid % cols
            if matrix[ridx][cidx] == target:
                return True
            if matrix[ridx][cidx] < target:
                left = mid + 1
            else:
                right = mid
        
        return False
        
s = Solution()
a2 = s.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=60)
print(a2)