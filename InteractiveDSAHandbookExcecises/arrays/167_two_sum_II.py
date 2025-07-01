"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(numbers)-1
        
        while left <= right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left + 1, right + 1]
            elif summ > target:
                right -= 1
            else:
                left += 1
            
s = Solution()
a = s.twoSum([2,7,11,15], 9)
a2 = s.twoSum([2,3,4], 6)
a3 = s.twoSum([-1,0], -1)
print(a)
print(a2)
print(a3)