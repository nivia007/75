"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
"""

import unittest
from typing import List

class Solution:        
    def climbStairs(self, n: int) -> int:
        # Time: O(n), Space: O(n)
        if n <= 2:
            return n
        
        ways_so_far = {1: 1, 2: 2}
        for i in range(3, n + 1):
            ways_so_far[i] = ways_so_far[i-1] + ways_so_far[i-2] 
        
        return ways_so_far[n]

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = 2
        # output
        r = 2
        self.assertEqual(Solution().climbStairs(n), r)

if __name__ == "__main__":
    unittest.main()