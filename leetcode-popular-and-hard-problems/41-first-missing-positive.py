"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

# runs in O(n) time and uses constant extra space.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        
        # mark the number from 0 to n
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        # mark the number that exists in nums
        for i in range(len(nums)):
            num = abs(nums[i])
            if num <= len(nums):
                nums[num - 1] = -abs(nums[num - 1])
                
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1



# just do the same thing without using extra space
class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1

        for i in range(len(nums)):
            n = nums[i]
            while 0 < n <= len(nums) and n != nums[n-1]:
                nums[i], nums[n-1] = nums[n-1], nums[i]
                n = nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

# Test solution 2
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))