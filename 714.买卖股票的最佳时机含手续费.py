#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (62.39%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 19.4K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 示例 1:
#
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
# 注意:
#
#
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
#
#
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp_0 = 0
        dp_1 = float('-inf')
        for i in range(0, n):
            tmp = dp_0
            dp_0 = max(dp_0, dp_1+prices[i]-fee)
            dp_1 = max(dp_1, tmp-prices[i])
        
        return dp_0
# @lc code=end
