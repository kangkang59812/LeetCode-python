#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (64.15%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 83.9K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = []
        dp.append([triangle[0][0]])

        for i in range(1, len(triangle)):
            dp_row = [0]*len(triangle[i])
            dp.append(dp_row)
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]

        return min(dp[-1])
        # @lc code=end
