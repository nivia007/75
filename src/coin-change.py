"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
 
Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

import unittest
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time: O(m*n), Space: O(n)
        if not amount : return 0

        dp  = [float('inf')]*(amount+1)
        dp[0] = 0
    
        for coin in coins:   
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1) 
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
            
            
### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [1,2,5]
        amount = 11
        # output
        r = 3
        self.assertEqual(Solution().coinChange(n, amount), r)

if __name__ == "__main__":
    unittest.main()