"""
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n) -> depends on the sorting algorithm
        """
        # if the len of nums is less of 3, no triplets could exsits
        if len(nums) < 3:
            return []
        answer = []
        # First, we sort the array to make it easier to find pairs
        # that sum up to a specific value
        nums.sort()
        # Then for each element in the array, we fix that element 
        # as the 1st number of a potential triplet
        for curr in range(len(nums) - 2):
            if curr > 0 and nums[curr] == nums [curr - 1]:
                continue
            # Next, we set up 2 pointer: one starting just after the 
            # fixed number and the other at the end of the array. We
            # calculate the sum of the 2 nums at these pointers. If 
            # the sum equals 0, we've found a valid triplet
            left = curr + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[curr] + nums[left] + nums[right]
                if summ == 0:
                    answer.append((nums[curr], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    # After each triplet is found, we skip over any
                    # duplicate elements to avoid continuing the same
                    # triplet multiple times.
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                # If the sum is too small we move the left pointer to the right
                # If the sum is too large we move the right poiner to the left
                elif summ < 0:
                    left += 1
                else:
                    right -=1
        return answer
            
                        
s = Solution()
a = s.threeSum([-1,0,1,2,-1,-4])
a2 = s.threeSum([0,1,1])
a3 = s.threeSum([0,0,0])
a4 = s.threeSum([1,2,-2,-5,-3,3,0,4])
print(a)
print(a2)
print(a3)
print(a4)