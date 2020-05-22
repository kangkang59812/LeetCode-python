#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (29.23%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 46.1K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
#
# 示例 2:
#
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
#
#
#

# @lc code=start


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if k == 0:
            return 0
        if k > n/2:
            dp_0 = 0
            dp_1 = float('-inf')
            for i in range(0, n):
                tmp = dp_0
                dp_0 = max(dp_0, dp_1+prices[i])
                dp_1 = max(dp_1, tmp-prices[i])
            return dp_0
        else:
            dp_ik0 = [0 for _ in range(k+1)]
            dp_ik1 = [float('-inf') for _ in range(k+1)]
            for i in range(0, n):
                for j in range(k, 0, -1):
                    if j != 1:
                        dp_ik0[j] = max(dp_ik0[j], dp_ik1[j] + prices[i])
                        dp_ik1[j] = max(dp_ik1[j], dp_ik0[j-1]-prices[i])
                    else:
                        dp_ik0[j] = max(dp_ik0[j], dp_ik1[j] + prices[i])
                        dp_ik1[j] = max(dp_ik1[j], -prices[i])
            return dp_ik0[k]
# @lc code=end
