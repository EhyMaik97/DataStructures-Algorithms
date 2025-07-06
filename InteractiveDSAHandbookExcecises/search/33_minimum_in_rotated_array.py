"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def linear_search(self, nums: list[int], target: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, v in enumerate(nums):
            if v == target:
                return i
        return -1

    def binary_search(self, nums: list[int], target: int) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

s = Solution()
a1 = s.linear_search([6,7,8,0,1,2,3], 7)
a2 = s.binary_search([6,7,8,0,1,2,3], 1)

print(a1)
print(a2)