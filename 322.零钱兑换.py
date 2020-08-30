#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (38.77%)
# Likes:    560
# Dislikes: 0
# Total Accepted:    78K
# Total Submissions: 199.3K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
#
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @functools.lru_cache(amount)
        # def dp(res_amount):
        #     if res_amount < 0:
        #         return -1
        #     if res_amount == 0:
        #         return 0
        #     min_number = float('inf')
        #     for coin in coins:
        #         res = dp(res_amount-coin)
        #         if res >= 0 and res < min_number:
        #             min_number = res+1
        #     return min_number if min_number != float('inf') else -1
        # if amount < 1:
        #     return 0
        # return dp(amount)
        @functools.lru_cache(amount)
        def dp(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            num = float('inf')
            for coin in coins:
                res = dp(n-coin)
                if res >= 0 and res < num:
                    num = res+1
            return num if num != float('inf') else -1
        return dp(amount)

# @lc code=end
