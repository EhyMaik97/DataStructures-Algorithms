"""
https://leetcode.com/problems/sort-colors/
Difficulty: Medium
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1   
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
        return nums
                
s = Solution()
a = s.sortColors([1,0,0,2,2,1,1,2,2,0,1])
a2 = s.sortColors([1,2,0])
print(a)
print(a2)
        