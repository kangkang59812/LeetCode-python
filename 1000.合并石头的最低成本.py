#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#
# https://leetcode-cn.com/problems/minimum-cost-to-merge-stones/description/
#
# algorithms
# Hard (31.06%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 4.6K
# Testcase Example:  '[3,2,4,1]\n2'
#
# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
#
# 每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
#
# 找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：stones = [3,2,4,1], K = 2
# 输出：20
# 解释：
# 从 [3, 2, 4, 1] 开始。
# 合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
# 合并 [4, 1]，成本为 5，剩下 [5, 5]。
# 合并 [5, 5]，成本为 10，剩下 [10]。
# 总成本 20，这是可能的最小值。
#
#
# 示例 2：
#
# 输入：stones = [3,2,4,1], K = 3
# 输出：-1
# 解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
#
#
# 示例 3：
#
# 输入：stones = [3,5,1,2,6], K = 3
# 输出：25
# 解释：
# 从 [3, 5, 1, 2, 6] 开始。
# 合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
# 合并 [3, 8, 6]，成本为 17，剩下 [17]。
# 总成本 25，这是可能的最小值。
#
#
#
#
# 提示：
#
#
# 1 <= stones.length <= 30
# 2 <= K <= 30
# 1 <= stones[i] <= 100
#
#
#

# @lc code=start


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if not stones:
            return 0
        if K == 0:
            return 0
        n = len(stones)
        while n >= K:
            a, b = divmod(n, K)
            n = a+b
        if n != 1:
            return -1
        n = len(stones)
        prefix_sum = [0]
        dp = [[0]*(n+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][i] = 0

        for i in range(stones):
            prefix_sum.append(prefix_sum[-1]+stones[i])
        for r in range(3, n+1, 3):
            for i in range(1, r):
                j = r
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+s[j]-s[i-1])

                if k % K == 0:
                    dp[i]

                    # @lc code=end
