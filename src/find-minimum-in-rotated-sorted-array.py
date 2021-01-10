"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

import unittest
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(log n), Space: O(1)
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            middle = left + (right - left)//2
            if middle >= 1 and nums[middle-1] > nums[middle]:
                return nums[middle]
            elif nums[left] > nums[middle]:
                # the minimum element must be in the left part
                right = middle - 1
            elif nums[middle] > nums[right]:
                # the minimum element must be in the right part
                left = middle + 1
            else:
                # every element is in ascending order, the minimum element is the leftmost element
                return nums[left]
        

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [11,13,15,17]
        # output
        r = 11
        self.assertEqual(Solution().findMin(n), r)

if __name__ == "__main__":
    unittest.main()
