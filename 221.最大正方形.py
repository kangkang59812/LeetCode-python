#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (39.36%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    32.4K
# Total Submissions: 81.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        # 防止一行，需要多次判断，麻烦
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1 if int(matrix[0][0]) else 0
        max_len = 0
        for i in range(2, m+1):
            dp[i][1] = int(matrix[i-1][0])
        for i in range(2, n+1):
            dp[1][i] = int(matrix[0][i-1])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if int(matrix[i-1][j-1]):
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                    max_len = max(max_len, dp[i][j])
        return max_len**2
        # @lc code=end
