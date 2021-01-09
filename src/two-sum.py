"""
1. Two Sum
==========

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n),​ Space: O(n)
        dic = {}
        for i in range(len(nums)) :
            if nums[i] in dic :
                return [dic.get(nums[i]), i]
            else :
                dic[target-nums[i]] = i
        
### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [3,2,4]
        t = 6
        # output
        r = [1,2]
        self.assertEqual(Solution().twoSum(n, t), r)

if __name__ == "__main__":
    unittest.main()