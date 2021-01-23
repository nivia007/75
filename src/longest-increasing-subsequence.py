"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""

import unittest
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2), Space: O(n)
        dp = [1]*len(nums)
        max_ans = 1
        for i in range(len(nums)):
            m_len = 0
            for j in range(i):
                if nums[i]>nums[j]:
                    m_len = max(dp[j], m_len)
            dp[i] = m_len+1
            max_ans = max(max_ans, dp[i])
            
        return max_ans
            

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [0,1,0,3,2,3]
        # output
        r = 4
        self.assertEqual(Solution().lengthOfLIS(n), r)

if __name__ == "__main__":
    unittest.main()

